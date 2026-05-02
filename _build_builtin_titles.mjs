import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'creation-cabin.html');
const seedPath = path.join(__dirname, '_titles_seed.txt');
const html = fs.readFileSync(htmlPath, 'utf8');
const seed = fs.readFileSync(seedPath, 'utf8');

function parseArrayLiteral(name) {
  const re = new RegExp(`const ${name} = (\\[[\\s\\S]*?\\]);`, 'm');
  const m = html.match(re);
  if (!m) return [];
  try {
    return Function('"use strict"; return ' + m[1])();
  } catch {
    return [];
  }
}

const ORIGINAL_BUILTIN = parseArrayLiteral('ORIGINAL_BUILTIN');
const EXTRA_TITLES_FROM_EXCEL = parseArrayLiteral('EXTRA_TITLES_FROM_EXCEL');

const hasCJK = (s) => /[\u4e00-\u9fff]/.test(s);
const LATIN_OK = new Set(
  'Soulmate seeyouagain echo kilig last night One last kiss love letter Young And Beautiful'.split(' ')
);

function normalizeLine(s) {
  let t = String(s).trim();
  if (!t) return '';
  t = t.replace(/\r/g, '');
  t = t.replace(/（[A-Za-z][^）]*）/g, (m) => (hasCJK(m) ? m : ''));
  t = t.replace(/\s*\([A-Za-z][^)]*\)\s*$/g, '');
  if (/^防灾演练/.test(t) && /[A-Za-z]/.test(t)) t = '防灾演练';
  t = t.replace(/\s+/g, ' ').trim();
  return t;
}

function keepTitle(t) {
  if (!t) return false;
  if (hasCJK(t)) return true;
  return LATIN_OK.has(t);
}

const fromSeed = seed.split(/\n/).map(normalizeLine).filter(keepTitle);

const merged = [...ORIGINAL_BUILTIN, ...EXTRA_TITLES_FROM_EXCEL, ...fromSeed];
const seen = new Set();
const out = [];
for (const raw of merged) {
  const t = normalizeLine(raw);
  if (!keepTitle(t)) continue;
  if (seen.has(t)) continue;
  seen.add(t);
  out.push(t);
}

function shuffleFY(arr) {
  const a = [...arr];
  const buf = new Uint32Array(1);
  for (let i = a.length - 1; i > 0; i--) {
    const lim = Math.floor(0x100000000 / (i + 1)) * (i + 1);
    let r;
    do {
      crypto.getRandomValues(buf);
      r = buf[0];
    } while (r >= lim);
    const j = r % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const shuffled = shuffleFY(out);

console.error('count', shuffled.length);
console.log(JSON.stringify(shuffled));
