# Portfolio Demos API（前后端分离 · 单仓示例）

Node.js + Express + **SQLite**（`better-sqlite3`），同一份服务支撑：

- **会议反刍舱**：会议 **CRUD** + **POST /api/analyze**（服务端 DeepSeek，`DEEPSEEK_API_KEY` 仅存服务器）
- **其余 Demo 云端备份**：`GET/PUT /api/demo/:appKey` 存任意 JSON 快照（与浏览器 localStorage 双向可选同步）

适用页面：`meeting-ruminant.html`，以及 `pet-vaccine.html` / `creation-cabin.html` / `script-review.html` 顶部「云端同步」模块。

## 本地运行

```bash
cd server
cp .env.example .env
# 编辑 .env，填入 DEEPSEEK_API_KEY
npm install
npm start
```

默认端口 **3789**。健康检查：<http://localhost:3789/api/health>

## 环境变量

| 变量 | 说明 |
|------|------|
| `PORT` | 端口，默认 3789 |
| `DEEPSEEK_API_KEY` | DeepSeek API，用于 `/api/analyze` |
| `API_TOKEN` | 可选。若设置，请求需带 `X-API-Key: <token>` |
| `DATABASE_PATH` | SQLite 文件路径，默认 `./data/meetings.db` |

## Docker 部署示例

在项目 `server` 目录：

```bash
docker build -t meeting-ruminant-api .
docker run -d -p 3789:3789 \
  -e DEEPSEEK_API_KEY=sk-xxx \
  -e API_TOKEN=可选密钥 \
  -v meeting-data:/app/data \
  meeting-ruminant-api
```

将公网域名反向代理到容器 **3789**，前端「云端 API」填写 `https://你的域名` 即可。

## API 摘要

- `GET /api/health` — 服务状态、是否已配置 DeepSeek、`demoBlobApps` 列表
- `GET /api/meetings` — 会议列表
- `GET /api/meetings/:id` — 单条
- `POST /api/meetings` — 新建（body: `transcript`, `analysis`, `createdAt` 可选）
- `PUT /api/meetings/:id` — 更新
- `DELETE /api/meetings/:id` — 删除
- `DELETE /api/meetings` — 清空全部
- `POST /api/analyze` — body: `{ "transcript": "..." }` → `{ "analysis": { topics, todos, questions } }`

### Demo 数据快照（JSON Blob）

`appKey` 仅允许：`pet-vaccine` | `creation-cabin` | `script-review`

- `GET /api/demo/:appKey` → `{ appKey, payload, updatedAt }`（无记录时 `payload` 为 `null`）
- `PUT /api/demo/:appKey` — body: `{ "payload": <任意可 JSON 序列化的对象> }`

请求体上限默认 **15MB**（整站 `express.json`）。

## 与静态页联调

1. 先启动本服务 `npm start`
2. 用浏览器打开 `meeting-ruminant.html`（或任意静态服务器）
3. 在「云端 API」输入 `http://localhost:3789`，点「测连接」
4. 勾选「服务端 AI 分析」后点「AI 深度分析」；或勾选「会议存云端库」后「保存会议」

其它 Demo：启动同一服务后，在对应页面填写同一 API 根地址，勾选「启用云端备份」，保存即会上传 JSON 快照。

若遇 CORS 问题，本服务已 `cors({ origin: true })` 允许跨域；生产环境建议用同域 Nginx 反代前后端。
