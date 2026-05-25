"""从 index.html 抽取各项目「📜 查看完整迭代历史」中的 <li>，用于对照 dev-logs。"""
import re

INDEX = r"g:\POLYU\2026-2027找工作\demo\work\index.html"
ORDER = ["pet", "creation", "cold", "script", "meeting", "prompt"]


def main():
    t = open(INDEX, encoding="utf-8").read()
    blocks = re.findall(r'<details class="doc-iteration">.*?</details>', t, re.DOTALL)
    assert len(blocks) == len(ORDER), (len(blocks), ORDER)
    for i, b in enumerate(blocks):
        ul = re.search(r"<ul[^>]*>(.*?)</ul>", b, re.DOTALL)
        inner = ul.group(1) if ul else ""
        items = re.findall(r"<li>(.*?)</li>", inner, re.DOTALL)
        print("###", ORDER[i])
        for it in items:
            print("-", re.sub(r"\s+", " ", it.strip()))
        print()


if __name__ == "__main__":
    main()
