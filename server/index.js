/**
 * Portfolio Demos API — Node + SQLite
 * - 会议 CRUD + POST /api/analyze（服务端 DeepSeek）
 * - GET/PUT /api/demo/:appKey — 其它 HTML Demo 的 JSON 快照备份
 */
require('dotenv').config();
const path = require('path');
const fs = require('fs');
const express = require('express');
const cors = require('cors');
const Database = require('better-sqlite3');

const PORT = Number(process.env.PORT) || 3789;
const DATABASE_PATH = process.env.DATABASE_PATH || path.join(__dirname, 'data', 'meetings.db');
const API_TOKEN = process.env.API_TOKEN || '';
const DEEPSEEK_KEY = process.env.DEEPSEEK_API_KEY || '';

fs.mkdirSync(path.dirname(DATABASE_PATH), { recursive: true });
const db = new Database(DATABASE_PATH);
db.exec(`
  CREATE TABLE IF NOT EXISTS meetings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transcript TEXT NOT NULL DEFAULT '',
    analysis TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
  );
  CREATE TABLE IF NOT EXISTS demo_data (
    app_key TEXT PRIMARY KEY,
    payload TEXT NOT NULL,
    updated_at TEXT NOT NULL
  );
`);

const DEMO_APP_KEYS = new Set(['pet-vaccine', 'creation-cabin', 'script-review']);

const app = express();
app.use(cors({ origin: true, credentials: true }));
app.use(express.json({ limit: '15mb' }));

function authMiddleware(req, res, next) {
  if (!API_TOKEN) return next();
  const key = req.header('x-api-key') || req.header('authorization')?.replace(/^Bearer\s+/i, '') || '';
  if (key !== API_TOKEN) return res.status(401).json({ error: 'Unauthorized' });
  next();
}
app.use(authMiddleware);

app.get('/api/health', (req, res) => {
  res.json({
    ok: true,
    service: 'portfolio-demos-api',
    hasDeepSeekKey: Boolean(DEEPSEEK_KEY),
    demoBlobApps: [...DEMO_APP_KEYS],
    time: new Date().toISOString()
  });
});

function rowToMeeting(row) {
  let analysis = null;
  if (row.analysis) {
    try {
      analysis = JSON.parse(row.analysis);
    } catch {
      analysis = null;
    }
  }
  return {
    id: row.id,
    transcript: row.transcript || '',
    analysis,
    createdAt: row.created_at,
    updatedAt: row.updated_at
  };
}

app.get('/api/meetings', (req, res) => {
  const rows = db.prepare('SELECT * FROM meetings ORDER BY id DESC').all();
  res.json(rows.map(rowToMeeting));
});

app.get('/api/meetings/:id', (req, res) => {
  const row = db.prepare('SELECT * FROM meetings WHERE id = ?').get(req.params.id);
  if (!row) return res.status(404).json({ error: 'Not found' });
  res.json(rowToMeeting(row));
});

app.post('/api/meetings', (req, res) => {
  const { transcript = '', analysis = null, createdAt } = req.body || {};
  const now = new Date().toISOString();
  const ca = createdAt && String(createdAt).trim() ? String(createdAt) : now;
  const analysisStr = analysis != null ? JSON.stringify(analysis) : null;
  const info = db
    .prepare('INSERT INTO meetings (transcript, analysis, created_at, updated_at) VALUES (?,?,?,?)')
    .run(transcript, analysisStr, ca, now);
  const row = db.prepare('SELECT * FROM meetings WHERE id = ?').get(info.lastInsertRowid);
  res.status(201).json(rowToMeeting(row));
});

app.put('/api/meetings/:id', (req, res) => {
  const id = req.params.id;
  const existing = db.prepare('SELECT * FROM meetings WHERE id = ?').get(id);
  if (!existing) return res.status(404).json({ error: 'Not found' });
  const { transcript, analysis } = req.body || {};
  const now = new Date().toISOString();
  const nextTranscript = transcript !== undefined ? transcript : existing.transcript;
  let analysisStr = existing.analysis;
  if (analysis !== undefined) {
    analysisStr = analysis != null ? JSON.stringify(analysis) : null;
  }
  db.prepare('UPDATE meetings SET transcript = ?, analysis = ?, updated_at = ? WHERE id = ?').run(
    nextTranscript,
    analysisStr,
    now,
    id
  );
  const row = db.prepare('SELECT * FROM meetings WHERE id = ?').get(id);
  res.json(rowToMeeting(row));
});

app.delete('/api/meetings/:id', (req, res) => {
  const r = db.prepare('DELETE FROM meetings WHERE id = ?').run(req.params.id);
  if (!r.changes) return res.status(404).json({ error: 'Not found' });
  res.json({ ok: true });
});

app.delete('/api/meetings', (req, res) => {
  db.exec('DELETE FROM meetings');
  res.json({ ok: true });
});

app.get('/api/demo/:appKey', (req, res) => {
  const key = req.params.appKey;
  if (!DEMO_APP_KEYS.has(key)) return res.status(400).json({ error: '未知的 demo 标识' });
  const row = db.prepare('SELECT * FROM demo_data WHERE app_key = ?').get(key);
  if (!row) return res.json({ appKey: key, payload: null, updatedAt: null });
  let payload = null;
  try {
    payload = JSON.parse(row.payload);
  } catch {
    payload = null;
  }
  res.json({ appKey: key, payload, updatedAt: row.updated_at });
});

app.put('/api/demo/:appKey', (req, res) => {
  const key = req.params.appKey;
  if (!DEMO_APP_KEYS.has(key)) return res.status(400).json({ error: '未知的 demo 标识' });
  const { payload } = req.body || {};
  if (payload === undefined) return res.status(400).json({ error: '缺少 payload' });
  const now = new Date().toISOString();
  const str = typeof payload === 'string' ? payload : JSON.stringify(payload);
  db.prepare('INSERT OR REPLACE INTO demo_data (app_key, payload, updated_at) VALUES (?,?,?)').run(
    key,
    str,
    now
  );
  res.json({ appKey: key, updatedAt: now });
});

const ANALYSIS_PROMPT_PREFIX = `你是一个专业的会议纪要分析助手。请严格按以下JSON格式输出（不要包含任何额外解释）：
{
  "topics": ["议题1", "议题2", ...],
  "todos": [
    { "task": "具体任务描述", "owner": "负责人姓名(若未提及留空)", "deadline": "截止时间(如'明天'、'2026-04-20'，未提及留空)", "completed": false, "status": "待办" }
  ],
  "questions": ["需要跟进的问题1", ...]
}

会议记录内容如下：
`;

async function callDeepSeekAnalyze(transcript) {
  if (!DEEPSEEK_KEY) {
    const err = new Error('服务端未配置 DEEPSEEK_API_KEY');
    err.statusCode = 503;
    throw err;
  }
  const prompt = ANALYSIS_PROMPT_PREFIX + String(transcript).substring(0, 12000);
  const controller = new AbortController();
  const t = setTimeout(() => controller.abort(), 60000);
  const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${DEEPSEEK_KEY}`
    },
    body: JSON.stringify({
      model: 'deepseek-chat',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.2,
      response_format: { type: 'json_object' }
    }),
    signal: controller.signal
  });
  clearTimeout(t);
  if (!response.ok) {
    const err = new Error(`DeepSeek HTTP ${response.status}`);
    err.statusCode = 502;
    throw err;
  }
  const data = await response.json();
  let content = data.choices?.[0]?.message?.content || '';
  const jsonMatch = content.match(/\{[\s\S]*\}/);
  if (!jsonMatch) {
    const err = new Error('模型返回非 JSON');
    err.statusCode = 502;
    throw err;
  }
  const parsed = JSON.parse(jsonMatch[0]);
  parsed.todos = (parsed.todos || []).map((t) => ({
    task: t.task || '未命名任务',
    owner: t.owner || '',
    deadline: t.deadline || '',
    completed: Boolean(t.completed),
    status: t.status || (t.completed ? '完成' : '待办')
  }));
  parsed.topics = parsed.topics || [];
  parsed.questions = parsed.questions || [];
  return parsed;
}

app.post('/api/analyze', async (req, res) => {
  const { transcript = '' } = req.body || {};
  if (!String(transcript).trim()) {
    return res.status(400).json({ error: 'transcript 不能为空' });
  }
  try {
    const analysis = await callDeepSeekAnalyze(transcript);
    res.json({ analysis });
  } catch (e) {
    const code = e.statusCode || 500;
    res.status(code).json({ error: e.message || '分析失败' });
  }
});

app.listen(PORT, () => {
  console.log(`Portfolio Demos API 监听 http://127.0.0.1:${PORT}`);
  console.log(`健康检查 GET /api/health  DeepSeek 已配置: ${Boolean(DEEPSEEK_KEY)}`);
});
