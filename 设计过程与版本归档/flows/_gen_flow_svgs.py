# -*- coding: utf-8 -*-
"""Generate flow SVGs into 设计过程与版本归档/flows/svg

与 `demo/work` 各页 dev-flow 步骤一致；改步骤后运行本脚本同步 SVG。
"""
import os

DATA = [
    (
        "flow_01_宠伴.svg",
        "宠伴·健康台账｜关键阶段（2025.09 起）",
        [
            ("25-09·界定", "深访+差评主线"),
            ("25-09·MVP", "砍社区四主线"),
            ("9-10·信任", "本地OCR决案"),
            ("25-10·验证", "分组×提醒"),
            ("25-10·迭代", "有效期·月花费"),
            ("10-11·交付", "PWA·口径"),
        ],
    ),
    (
        "flow_02_会议舱.svg",
        "会议·反刍舱｜关键阶段（2025.11 起）",
        [
            ("25-11·锚定", "会后失忆访谈"),
            ("25-11·MVP", "转写待办状态"),
            ("25-11·结构化", "Prompt抽检"),
            ("持续·节拍", "Backlog排期"),
            ("验证·侧", "耗时与7日"),
            ("沉淀·侧", "示意指数"),
        ],
    ),
    (
        "flow_03_创作舱.svg",
        "创作舱·种子驱动迭代",
        [
            ("25秋·种子", "访谈定优先级"),
            ("IA冻结", "一桌式工作台"),
            ("MVP可点", "单文件离线"),
            ("走查", "摩擦进池"),
            ("模块迭代", "目标·健康分"),
            ("发版复盘", "周报·PWA"),
        ],
    ),
    (
        "flow_04_冷启动.svg",
        "冷启动·规则+AI",
        [
            ("场景界定", "拖延可执行"),
            ("规格冻结", "三段式输出"),
            ("v1规则", "离线保底"),
            ("验证", "自用试跑"),
            ("AI迭代", "多Key路径"),
            ("Tab闭环", "任务进度"),
        ],
    ),
    (
        "flow_05_剧本舱.svg",
        "剧本舱·留痕交付",
        [
            ("界定痛点", "改稿失忆"),
            ("模型", "三位一体"),
            ("MVP", "快照·标签"),
            ("验证", "回溯抽检"),
            ("迭代", "热力·看板"),
            ("交付导出", "Word/CSV"),
        ],
    ),
    (
        "flow_06_Prompt库.svg",
        "Prompt库·模板资产",
        [
            ("归集", "PRD到原型链"),
            ("分类", "场景标签"),
            ("单页", "检索复制"),
            ("验证", "30秒找到"),
            ("随项目", "同步发版"),
            ("留痕", "日期维护"),
        ],
    ),
]


def build_svg(aria, steps):
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="990" height="90" viewBox="0 0 990 90" role="img" aria-label="{aria}">',
        "<defs><marker id=\"a\" markerWidth=\"8\" markerHeight=\"8\" refX=\"7\" refY=\"4\" orient=\"auto\"><path d=\"M0,0 L0,8 L8,4 z\" fill=\"#94a3b8\"/></marker></defs>",
        '<rect width="990" height="90" fill="#f1f5f9"/>',
        "<g font-family=\"system-ui,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif\">",
    ]
    widths = [148] * 5 + [164]
    x0 = 8
    xs = []
    for w in widths:
        xs.append(x0)
        x0 += w + 12
    for i, ((title, sub), w, x) in enumerate(zip(steps, widths, xs)):
        cx = x + w // 2
        lines.append(
            f'<rect x="{x}" y="10" width="{w}" height="68" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>'
        )
        lines.append(
            f'<text x="{cx}" y="36" text-anchor="middle" font-size="11" font-weight="650" fill="#0f172a">{title}</text>'
        )
        lines.append(
            f'<text x="{cx}" y="56" text-anchor="middle" font-size="9" fill="#64748b">{sub}</text>'
        )
    for i in range(len(xs) - 1):
        x_right = xs[i] + widths[i] + 2
        x_next_left = xs[i + 1] - 2
        lines.append(
            f'<line x1="{x_right}" y1="44" x2="{x_next_left}" y2="44" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#a)"/>'
        )
    lines.append("</g></svg>")
    return "\n".join(lines)


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(root, "svg")
    os.makedirs(out, exist_ok=True)
    for fn, aria, steps in DATA:
        path = os.path.join(out, fn)
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_svg(aria, steps))
        print("wrote", path)


if __name__ == "__main__":
    main()
