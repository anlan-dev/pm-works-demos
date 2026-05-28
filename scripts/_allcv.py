# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
idx = 0
while True:
    i = t.find("简历", idx)
    if i == -1:
        break
    print(i, repr(t[max(0,i-8):i+30]))
    idx = i + 1
