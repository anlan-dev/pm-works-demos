# 原型交付说明（与高保真 HTML 对齐）

本目录说明如何把仓库里的 **可交互高保真**（`demo/work/*.html`）与主流**原型工具**对齐；**不是**替代 `.fig` / `.rp` 源文件——那些需在本机工具里另存，但面试官/协作方通常更关心 **可点 Demo + 口径文档**。

## 高保真原型（主交付）

| 项目 | 本地文件（相对 `demo/work`） | 线上（若已部署） |
|------|-----------------------------|------------------|
| 宠伴 | `pet-vaccine.html` | `https://anlan-bot.github.io/pm-works-demos/pet-vaccine.html` |
| 会议舱 | `meeting-ruminant.html` | …/meeting-ruminant.html |
| 创作舱 | `creation-cabin.html` | …/creation-cabin.html |
| 冷启动 | `cold-start.html` | …/cold-start.html |
| 剧本舱 | `script-review.html` | …/script-review.html |
| Prompt 库 | `prompt-library.html` | …/prompt-library.html |
| 跨境电商 | `cross-border-ai.html` | …/cross-border-ai.html |
| 住值 | `zhuzhi-rent.html` | …/zhuzhi-rent.html |
| **PixelPick** | `pixelpick.html` | …/pixelpick.html |
| **雾灯残页·游戏** | `mistlamp.html` | …/mistlamp.html |
| **雾灯残页·AIGC展示** | `vn-game.html` | …/vn-game.html |
| **分支树·结构图** | `branch_tree.html` | …/branch_tree.html |
| **Demo Hub·导航** | `demo-hub.html` | …/demo-hub.html |

细节清单见 **`manifest.json`**（可被脚本读取）与 **`specs/全项目屏幕与Frame映射.md`**（人类可读）。**时间线**与各页 `dev-flow`、`manifest.json` 一致；流程顶栏用 `../flows/svg/`。

## Figma · 墨刀（并荐）

| 工具 | 流程图 | 高保真交互 |
|------|--------|------------|
| **Figma** | Import `../flows/svg/*.svg` 置顶 | Frame 内贴**全页截屏**；或合规 HTML 插件 |
| **墨刀** | 插入 SVG / mermaid 导出的 **2x PNG** | **网页/嵌入** 填 GitHub Pages 上表 URL；备注区写**时间锚点**（实习 / 宠伴 / 会议） |

若团队要求只交 `.rp` / `.fig` 源文件：请在本地工具中 **另存**，并以本目录 **manifest + flows** 为命名与页面顺序依据。

**其他**：Sketch / MasterGo / Pixso 同 **Figma 导入 SVG**；Axure 用 **内联框架** + SVG 母版；Miro / Whimsical 贴 mermaid 导出图。

## 工具无关交换格式

- **`manifest.json`**：项目 ID、HTML 文件名、建议画板尺寸、主要页面/状态；每项目含 **`resume_anchor`**（`cv_section_tags`、`portfolio_slot_zh`、`flow_aria_label`、`timeline`、`kicker_full_zh` / `kicker_short_zh`），与页内 `dev-flow` 顶栏一致，供 Figma/墨刀备注与脚本消费。
- **`tool_export/figma_frame_import_template.csv`**：方便在表格里规划 Frame 名称与路径，再 **手动** 在 Figma 中批量建页（Figma 不原生导入 CSV 为 Frame，此为**协作规划用**）。
- **`../flows/mermaid/流程图源码.md`**：与流程 SVG 同源，可进 mermaid.live 再导出矢量。

## 维护

HTML 改版后：同步改 **`manifest.json`**（含各项目 **`resume_anchor.kicker_*`** 与 `flow_aria_label`）、`specs/全项目屏幕与Frame映射.md`，并运行 `flows/_gen_flow_svgs.py` 重生成流程 SVG（若步骤文案有变）；各页 **`dev-flow-kicker`** 长/短两档与 manifest 保持一致。
