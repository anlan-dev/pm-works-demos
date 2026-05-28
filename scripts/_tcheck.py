# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
for s in ["冷启动（简历", "剧本舱（简历", "Prompt库（简历", "与简历一句", "呼应简历", "对应简历"]:
    print(s, s in t)
