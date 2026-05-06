/**
 * One-off: merge title-paste.txt + existing ORIGINAL/EXTRA → dedupe CJK-only → shuffle → stdout JSON array line
 */
import fs from 'fs';
import crypto from 'crypto';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'creation-cabin.html');
const html = fs.readFileSync(htmlPath, 'utf8');

function extractArray(name) {
  const re = new RegExp(`const ${name} = (\\[[\\s\\S]*?\\]);`);
  const m = html.match(re);
  if (!m) throw new Error('missing ' + name);
  return new Function('return ' + m[1])();
}

const ORIGINAL_BUILTIN = extractArray('ORIGINAL_BUILTIN');
const EXTRA_TITLES_FROM_EXCEL = extractArray('EXTRA_TITLES_FROM_EXCEL');

const pasteRaw = fs.readdirSync(__dirname)
  .filter((f) => /^title-paste.*\.txt$/i.test(f))
  .sort()
  .map((f) => fs.readFileSync(path.join(__dirname, f), 'utf8'))
  .join('\n');

function stripTrailingLatinParen(s) {
  let t = s.trim();
  for (;;) {
    const m1 = t.match(/^(.+?)\s*\(([^)]*)\)\s*$/);
    if (m1 && !/[\u4e00-\u9fff]/.test(m1[2])) {
      t = m1[1].trim();
      continue;
    }
    const m2 = t.match(/^(.+?)\s*（([^）]*)）\s*$/);
    if (m2 && !/[\u4e00-\u9fff]/.test(m2[2])) {
      t = m2[1].trim();
      continue;
    }
    break;
  }
  return t;
}

function hasCjk(s) {
  return /[\u4e00-\u9fff]/.test(s);
}

const seen = new Set();
const out = [];

function add(t) {
  if (!t || !hasCjk(t)) return;
  if (seen.has(t)) return;
  seen.add(t);
  out.push(t);
}

for (const x of ORIGINAL_BUILTIN) add(String(x).trim());
for (const x of EXTRA_TITLES_FROM_EXCEL) add(String(x).trim());

for (const line of pasteRaw.split(/\r?\n/)) {
  const trimmed = line.trim();
  if (!trimmed || /^把这些/.test(trimmed)) continue;
  add(stripTrailingLatinParen(trimmed));
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const buf = new Uint32Array(1);
    crypto.getRandomValues(buf);
    const j = buf[0] % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const shuffled = shuffle(out);
process.stdout.write(JSON.stringify(shuffled));
