# -*- coding: utf-8 -*-
"""一次性/批量替换 dev-flow 块时使用：当前 index 与各 Demo 的 aria-label 已升级为「简历*时间线」版。
若需再次全量替换，请先检查本文件 REPLACEMENTS 的匹配键是否与 HTML 一致。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # demo/work
IDX = ROOT / "index.html"

REPLACEMENTS = [
    (
        "宠伴·开发流程",
        '''<div class="dev-flow" aria-label="宠伴·健康台账（2025年9月起）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">先统一阶段目标与指标口径，再用分组实验验证提醒策略，把结论沉淀进可追踪的 backlog —— 全程围绕「提醒 + 记录」主线迭代。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">口径 → 验证 → backlog；2025.09 起。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">2025-09 界定</span><span class="dev-flow-note">深访+商店差评，定「提醒+记录」主线（非社交）</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">2025-09 MVP</span><span class="dev-flow-note">砍掉社区/商城；档案·疫苗日历·花费·提醒 四主线</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">9-10 月 信任</span><span class="dev-flow-note">OCR 三方案比选→本地路径（本地优先，降低上传顾虑）</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">2025-10 验证</span><span class="dev-flow-note">提醒策略分组观察：配置意愿与回访同向</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">2025-10 迭代</span><span class="dev-flow-note">种子回访→自动算有效期、按月花费视图</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">10-11 月 交付</span><span class="dev-flow-note">可安装 PWA；口径写进指标说明；与版本记录一致</span></li></ol></div>''',
    ),
    (
        "会议舱·开发流程",
        '''<div class="dev-flow" aria-label="会议·反刍舱（2025年11月起）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">不做大而全协作台：会后先结构化产出，再落到待办台账，按周节拍迭代；用整理耗时 + 短周期完成趋势（示意指数）判断是否继续加码。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">结构化产出→台账→周节拍；耗时与完成趋势验收。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">2025-11 初 锚定</span><span class="dev-flow-note">访谈「会后失忆」（research/2025-11-08）</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">2025-11 初 MVP</span><span class="dev-flow-note">转写→待办→状态流，拒绝大而全协作台</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">2025-11 中 结构化</span><span class="dev-flow-note">Prompt/字段迭代 + 漏项抽检清单</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">持续 周节拍</span><span class="dev-flow-note">Backlog 优先级与版本切片，固定周内评审节奏</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">验证侧</span><span class="dev-flow-note">会后整理耗时↓、短周期完成率趋势↑</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">沉淀侧</span><span class="dev-flow-note">示意指数 + 演练记录，材料自洽可复盘</span></li></ol></div>''',
    ),
    (
        "创作舱·开发流程",
        '''<div class="dev-flow" aria-label="星途·创作舱（2025 秋起）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">种子访谈把模块优先级排清 → 交付可点 MVP → 走查把摩擦收回需求池；写作主路径优先于堆功能。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">访谈→MVP→走查；反馈定优先级。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">2025 秋 种子</span><span class="dev-flow-note">访谈定标题库/目标/进度优先级</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">IA 冻结</span><span class="dev-flow-note">一桌式：大纲·角色·正文·离线</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">MVP 可点</span><span class="dev-flow-note">单文件 HTML，先跑通写作主路径</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">走查</span><span class="dev-flow-note">卡文/断更/查找摩擦登记进反馈池</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">模块迭代</span><span class="dev-flow-note">目标·时间线·快照·健康分·周报</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">发版复盘</span><span class="dev-flow-note">PWA 与导出链，与版本迭代表同步</span></li></ol></div>''',
    ),
    (
        "冷启动·开发流程",
        '''<div class="dev-flow" aria-label="Cold Start · 冷启动（规则 + AI 双模）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">规则引擎保障离线可用，联网时用多平台模型增强个性化；用「纯规则 vs 接入 API Key」做双模体验对照。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">离线保底 + API 增强；双模对照。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">场景界定</span><span class="dev-flow-note">拖延=想得多动的少，拆成可执行颗粒</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">规格冻结</span><span class="dev-flow-note">诊断+启动任务+递进计划 三段式</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">v1 规则引擎</span><span class="dev-flow-note">离线可用，对应「保底」</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">验证</span><span class="dev-flow-note">自用+熟人试跑，主观耗时与完成率感受</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">AI 迭代</span><span class="dev-flow-note">OpenRouter/DeepSeek 等多 Key 路径</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">Tab 闭环</span><span class="dev-flow-note">任务勾选与进度总览，形成可用闭环</span></li></ol></div>''',
    ),
    (
        "剧本舱·开发流程",
        '''<div class="dev-flow" aria-label="剧本·复盘舱（剧本-进度-复盘）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">先锁定「剧本–进度–复盘」信息架构，再叠加热力图、标签与多格式导出；每次改稿留痕，方便回溯与交接。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">结构优先；热力图 / 标签 / 可导出回溯。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">问题界定</span><span class="dev-flow-note">长改稿「为何删这场戏」易失忆</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">模型</span><span class="dev-flow-note">剧本-进度-复盘 三位一体</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">MVP</span><span class="dev-flow-note">快照·标签·本地记录流</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">验证</span><span class="dev-flow-note">回溯一问一答能否答上</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">迭代</span><span class="dev-flow-note">写作热力图·场景看板·streak</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">交付</span><span class="dev-flow-note">Word/CSV/JSON 导出，方便制片协同</span></li></ol></div>''',
    ),
    (
        "Prompt 库·开发流程",
        '''<div class="dev-flow" aria-label="Prompt Library（协作提效）"><div class="dev-flow-kicker"><span class="dev-flow-kicker-text dev-flow-kicker-text--full">把散落指令收成可检索、可一键复制的模板，按 PRD / UI / 调试等场景分类，发版时同步更新条目。</span><span class="dev-flow-kicker-text dev-flow-kicker-text--short">场景分类 · 一键复制 · 随版本维护。</span></div><ol class="dev-flow-track"><li class="dev-flow-step"><span class="dev-flow-num">1</span><span class="dev-flow-title">素材归集</span><span class="dev-flow-note">Chat/备忘录/IDE 碎片统一归档</span></li><li class="dev-flow-step"><span class="dev-flow-num">2</span><span class="dev-flow-title">场景分类</span><span class="dev-flow-note">PRD/UI/代码/调试/复盘…</span></li><li class="dev-flow-step"><span class="dev-flow-num">3</span><span class="dev-flow-title">单页交付</span><span class="dev-flow-note">筛选+一键复制，Vibe Coding 工作流</span></li><li class="dev-flow-step"><span class="dev-flow-num">4</span><span class="dev-flow-title">验证</span><span class="dev-flow-note">「30 秒内找到」自测打勾</span></li><li class="dev-flow-step"><span class="dev-flow-num">5</span><span class="dev-flow-title">随项目迭代</span><span class="dev-flow-note">与宠伴/会议发版同步更新条目</span></li><li class="dev-flow-step"><span class="dev-flow-num">6</span><span class="dev-flow-title">版本留痕</span><span class="dev-flow-note">更新日期写入页眉，可追溯维护节拍</span></li></ol></div>''',
    ),
]


def _pat(mkey: str) -> str:
    return '<div class="dev-flow" aria-label="' + re.escape(mkey) + r'"[\s\S]*?</ol></div>'


def patch_text(s: str, mkey: str, new_block: str) -> str:
    s2, n = re.subn(_pat(mkey), new_block, s, count=1)
    if n != 1:
        raise ValueError(f"replace failed for aria-label={mkey!r} count={n}")
    return s2


def main():
    s = IDX.read_text(encoding="utf-8")
    for mkey, block in REPLACEMENTS:
        s = patch_text(s, mkey, block)
    IDX.write_text(s, encoding="utf-8")
    print("index.html OK")

    demos = [
        ROOT / "pet-vaccine.html",
        ROOT / "meeting-ruminant.html",
        ROOT / "creation-cabin.html",
        ROOT / "cold-start.html",
        ROOT / "script-review.html",
        ROOT / "prompt-library.html",
    ]
    for p, (mkey, block) in zip(demos, REPLACEMENTS):
        t = p.read_text(encoding="utf-8")
        t = patch_text(t, mkey, block)
        p.write_text(t, encoding="utf-8")
        print(p.name, "OK")


if __name__ == "__main__":
    main()
