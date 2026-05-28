# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(__file__).resolve().parent.joinpath("index.html").read_text(encoding="utf-8")
import re
print("与简历" in t, "简历项目" in t, "泾阳" in t, "主档" in t)
for m in re.finditer("简历", t):
    if m.start() > 87000 and m.start() < 93000:
        print("near", m.start(), t[m.start()-15:m.start()+40])
