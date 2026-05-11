# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
out = []
for key in ["剧本舱（简历补充", "Prompt库（简历"]:
    i = t.find(key)
    out.append(f"=== {key} ===\n{t[i - 35 : i + 520]}\n")
Path(__file__).resolve().parent.joinpath("_ex2.txt").write_text("\n".join(out), encoding="utf-8")
