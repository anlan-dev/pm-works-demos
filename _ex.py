# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
i = t.find('冷启动（简历补充')
print(t[i:i+550])
