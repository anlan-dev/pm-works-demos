# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
for s in ["时间线自简历", "对齐简历 2025", "与简历", "泾阳", "实习互证", "需求池宠伴"]:
    if s in t:
        i = t.find(s)
        print(s, i, t[i:i+80])
