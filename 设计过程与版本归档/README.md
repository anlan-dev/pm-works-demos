# 作品集 · 设计过程与版本归档（索引）

本目录与线上作品集**同期维护**：记录需求取舍、验证思路、口径与迭代节点，便于自己复盘，也方便答辩或沟通时快速翻到对应材料（纸质打印或平板均可）。所有项目均为**轻量化 Demo / 小范围验证**，文中已标明样本规模与指标性质，避免被误读为大规模生产业务数据。

**作品集入口**：https://anlan-bot.github.io/pm-works-demos/

## 文档清单

### 产品与过程材料

| 文件 | 用途（复盘 / 沟通） |
|------|-------------------------|
| `用户与实验数据_总册.md` | **用户与实验数据**文档的索引导读 + 30 秒口径 |
| `共用_指标与数据口径.md` | 示意指数、饼图/条图计数含义 |
| `共用_用户研究与数据采集说明.md` | 种子用户、方法、伦理与归档 |
| `摘录_用户与实验数据一览表.md` | 一页总表：项目 × 样本 × 图表数字 |
| `数据字典_本地事件与字段.md` | 埋点/本地事件命名与字段（设计草案） |
| `合成指数计算说明_宠伴与会议.md` | 多路信号→示意指数的合成逻辑 |
| `需求池与反馈台账_结构说明.md` | 17 条工单状态与主题计数规则 |
| `验证记录_AB与分组观察.md` | 宠伴/会议假设、分组、观察、局限 |
| `模板_受访者名册与知情说明.md` | 名册 + 知情话术（填后脱敏） |
| `模板_访谈与可用性记录表.md` | 单次访谈/走查记录 |
| `模板_实验与分组台账.md` | 实验一行账 + 附录 |
| **`research/`** | **已生成**脱敏访谈 3 篇（宠伴×2、会议×1） |
| **`ux_tasks/宠伴_tasklist.md`** | **已生成**可用性任务 T1～T5 |
| **`backlog/tickets_2025Q4.csv`** | **已生成**17 条工单；说明见 `backlog/README_backlog.md` |
| **`flows/`** | **流程图**：`svg/` 可导入 Figma/Sketch/Axure；`mermaid/` 可导出 SVG（[mermaid.live](https://mermaid.live)） |
| **`flows/_gen_flow_svgs.py`** | 可选：改流程文案后运行，批量重生成 `svg/*.svg` |
| **`prototypes/`** | **原型映射**：`manifest.json`（机读）+ `specs/`（屏幕–Frame 对照）+ `tool_export/*.csv`（规划表） |
| `共用_迭代复盘与版本摘要.md` | 迭代节奏摘要 |
| `PRD_01_宠伴健康台账.md` ~ `PRD_06_Prompt_Library.md` | 各项目短 PRD |
| `PRD_07_住值.md` | 住值·租房生命成本计算器 PRD |
| `PRD_08_跨境电商.md` | 跨境电商·AI Agent PRD |
| **`architecture/`** | **架构文档**：宠伴/会议/创作/冷启动/剧本/Prompt/跨境/住值 + 新增 PixelPick/Mistlamp/分支树/DemoHub（共 12 篇） |
| **`changelog/`** | **迭代日志**：宠伴/会议/创作/冷启动/剧本/Prompt/跨境/住值 + 新增 PixelPick/雾灯残页系列/设计系统梳理/UIUX全项目审计 |
| `AIGC能力矩阵.md` | 全项目 AI 能力矩阵（含 2026-06 新增雾灯残页 AIGC 开发、PixelPick AI 优选） |
| `研究备忘_社交媒体内容洞察.md` | 研究能力迁移 |
| `附录_高频追问与应答要点.md` | 答辩 / 沟通时的高频追问 |

## 使用建议（复盘 / 答辩 / 沟通）

1. **被问「数据真的吗」**：先交代 Demo 边界，再打开 `共用_指标与数据口径.md` + `合成指数计算说明_宠伴与会议.md`。
2. **被问「需求从哪来」**：`research/*.md`（已生成样例）+ `共用_用户研究与数据采集说明.md` + 可选 `模板_访谈与可用性记录表.md`。
3. **被问「你怎么迭代」**：`版本记录_与作品集同步.md` + `backlog/tickets_2025Q4.csv` + `共用_迭代复盘与版本摘要.md`。
4. **被问「A/B 怎么做」**：`验证记录_AB与分组观察.md` + `模板_实验与分组台账.md`。
5. **被问「埋点怎么设计」**：`数据字典_本地事件与字段.md`。
6. **被问「流程图 / 原型搁哪」**：打开 `flows/README.md`（矢量+Mermaid）与 `prototypes/README.md`（HTML 高保真 + Figma/Axure 对齐说明）。

---

## 项目导航（按开发时间）

### 2025 Q3-Q4 · 核心项目

| 项目 | 架构 | PRD | 迭代日志 | 流程SVG | 上线体验 |
|------|------|-----|----------|---------|----------|
| 宠伴·健康台账 | `architecture/ARCHITECTURE_宠伴.md` | `prd/PRD_01_*` | `changelog/CHANGELOG_宠伴.md` | `flows/svg/flow_01_*` | `../pet-vaccine.html` |
| 会议·反刍舱 | `architecture/ARCHITECTURE_会议舱.md` | `prd/PRD_02_*` | `changelog/CHANGELOG_会议舱.md` | `flows/svg/flow_02_*` | `../meeting-ruminant.html` |
| 冷启动·行动引擎 | `architecture/ARCHITECTURE_冷启动.md` | `prd/PRD_03_*` | `changelog/CHANGELOG_冷启动.md` | `flows/svg/flow_04_*` | `../cold-start.html` |
| 创作舱 | `architecture/ARCHITECTURE_创作舱.md` | `prd/PRD_04_*` | `changelog/CHANGELOG_创作舱.md` | `flows/svg/flow_03_*` | `../creation-cabin.html` |
| 剧本复盘舱 | `architecture/ARCHITECTURE_剧本舱.md` | `prd/PRD_05_*` | `changelog/CHANGELOG_剧本舱.md` | `flows/svg/flow_05_*` | `../script-review.html` |
| Prompt Library | `architecture/ARCHITECTURE_Prompt库.md` | `prd/PRD_06_*` | `changelog/CHANGELOG_Prompt库.md` | `flows/svg/flow_06_*` | `../prompt-library.html` |

### 2026 Q1-Q2 · 扩展项目

| 项目 | 架构 | PRD | 迭代日志 | 上线体验 |
|------|------|-----|----------|----------|
| 跨境电商·AI Agent | `architecture/ARCHITECTURE_跨境电商.md` | `prd/PRD_08_*` | `changelog/CHANGELOG_跨境电商.md` | `../cross-border-ai.html` |
| 住值·租房决策 | `architecture/ARCHITECTURE_住值.md` | `prd/PRD_07_*` | `changelog/CHANGELOG_住值.md` | `../zhuzhi-rent.html` |

### 2026 Q2 · 新增项目（6月）

| 项目 | 架构 | DESIGN.md | 上线体验 | 类型 |
|------|------|-----------|----------|------|
| **PixelPick · AI 影像精选** | `architecture/ARCHITECTURE_PixelPick.md` | `../design-systems/pixelpick/DESIGN.md` | `../pixelpick.html` | 创作工具 · AI 优选 |
| **Mistlamp · 雾灯残页** | `architecture/ARCHITECTURE_Mistlamp.md` | `../design-systems/mistlamp/DESIGN.md` | `../mistlamp.html` | 游戏 · 文字冒险 |
| **雾灯残页 · AIGC 展示** | `architecture/ARCHITECTURE_Mistlamp.md` | `../design-systems/vn-game/DESIGN.md` | `../vn-game.html` | AIGC 能力展示 |
| **Branch Tree · 结构图** | `architecture/ARCHITECTURE_分枝树.md` | `../design-systems/branch-tree/DESIGN.md` | `../branch_tree.html` | 数据可视化 · 游戏架构 |
| **Demo Hub · 导航页** | `architecture/ARCHITECTURE_DemoHub.md` | `../design-systems/demo-hub/DESIGN.md` | `../demo-hub.html` | 导航 · 面试门户 |
| **UIwork · 11 风格 Demo** | — | `../design-systems/UIwork/DESIGN.md` | `../UIwork/index.html` | UI 设计展示 |

### 全项目设计系统

| 交付物 | 路径 | 说明 |
|--------|------|------|
| **DESIGN.md 合集** | `../design-systems/` | 14 项目完整设计规范，含 YAML frontmatter + 组件 Token |
| **设计规范 · 三件套** | `../设计参考/` | 色彩字体系统 / 组件布局系统 / 交互动效系统 |
| **年度更新日志** | `changelog/CHANGELOG_设计系统梳理.md` | 2026-06-28 设计系统全面梳理记录 |

---

维护：重大改版后同步改主档 `简历/00_草稿文本/简历填充主档_王天娇.txt` 与本目录中相关段落；**若改开发流程步骤**：同步 `index.html` 内流程条、`flows/` 下 SVG/Mermaid，并运行 `flows/_gen_flow_svgs.py`。流程与**简历 [C][D][F]** 对齐说明见 `flows/README.md`。
