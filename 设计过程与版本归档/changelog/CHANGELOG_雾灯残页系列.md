# 雾灯残页 · 系列项目 — 迭代日志

> 记录雾灯残页系列（游戏本体 + AIGC 展示页 + 结构示意图）各版本关键决策与验证结果。

---

## v1.0 (2026-06-18) — 游戏本体 MVP + AIGC 展示

**决策依据**：展示「PM 指导 AI 完成复杂创意项目」的核心能力——世界观、角色、分支叙事全部由 AI 生成，人类 PM 负责决策与品控。

**游戏本体（mistlamp.html）**：
- 主菜单（新游戏/继续/存档管理）+ 径向渐变背景
- 属性系统（意志/洞察/共鸣/暗蚀）
- 属性门槛分支选择
- 叙事引擎（Noto Serif SC 衬线正文，1.8 行高）
- localStorage 存档系统（多槽位）
- 三种主题（默认暗色/更深/羊皮纸浅色）
- 所有交互元素 ≥ 48px（移动端友好）

**AIGC 展示页（vn-game.html）**：
- Hero + Stats Grid（生成字数/AI调用/结局数）
- 6 个 AIGC 应用阶段展示（世界观/角色/分支/润色/导出/翻译）
- 折叠 Details 面板
- 文件溯源链接（直接链接生成资产）
- 技术架构说明
- dark / ink / default 三主题

**AIGC 资产**：
- `script.rpy` — Ren'Py 脚本
- `story_text.txt` — 叙事全文
- `story_overview.md` — 故事大纲
- `worldbuilding.md` — 世界观设定
- `character_profiles.md` — 角色档案

**AI 协作模式**：
- Agent 1：世界观构建（设定/规则/历史）
- Agent 2：角色设计（档案/关系/动机）
- Agent 3：对话生成（场景/分支/语气）
- Agent 4：品质审查（一致性/节奏/情感弧线）

**验证结果**：
- 游戏可玩，含 4 章分支叙事
- AIGC 展示页完整呈现 AI 协作过程
- 文件溯源提供可验证证据链

---

## v1.1 (2026-06-20) — 结构示意图

**决策依据**：面试中常被问到「游戏结构怎么设计的」，需要一个可视化工具快速讲解。

**branch_tree.html 新增**：
- 羊皮纸手稿风格展板
- 世界观/角色/分支轴线/章节 Timeline/结局谱系
- 移动端 accordion 折叠 + 桌面端多列 Grid
- Legend 图例 + 药丸 Chip 标签
- 三条轴线可视化（命运/自我/未知）

---

## v1.2 (2026-06-27) — 设计系统规范化

**决策依据**：与全项目设计系统梳理同步，为雾灯残页系列建立独立 DESIGN.md。

**核心改动**：
- 创建 `design-systems/mistlamp/DESIGN.md`（游戏本体）
- 创建 `design-systems/vn-game/DESIGN.md`（AIGC 展示页）
- 创建 `design-systems/branch-tree/DESIGN.md`（结构示意图）
- 创建 `architecture/ARCHITECTURE_Mistlamp.md`
- 创建 `architecture/ARCHITECTURE_分枝树.md`
- 统一三文件色彩 Token 命名（accent/muted/surface 一致）

---

## 未来规划

- [ ] 更多章节和分支（当前 4 章可扩展到 8 章）
- [ ] 成就系统（收集全部结局徽章）
- [ ] 音频叙事（AI TTS 旁白朗读）
- [ ] 导出阅读版本（纯文本/PDF）
- [ ] 多语言版本（当前 AIGC 生成已含翻译 Agent 设计）
