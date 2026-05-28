# 开发流程图（Figma · 墨刀 双适配）

与 **`index.html` 及各 Demo 页内嵌 `<details class="dev-flow">`** 同源：**阶段口径 → 对比或分组验证 → 台账式复盘**。墨刀与 Figma 均推荐 **先矢量后标注**：本目录 **SVG** 为通用交换格式，**Mermaid** 可再导出 PNG 高清贴图。

## 文件说明

| 路径 | Figma | 墨刀 MockingBot |
|------|--------|------------------|
| `svg/*.svg` | 画布 **Import** 或拖入；`Outline` 里可解组改字（视导入设置） | **流程图/标注页** → 插入 **图片** → 选 SVG（或先转 PNG）；或用「形状」对照重建连接线 |
| `mermaid/流程图源码.md` | [mermaid.live](https://mermaid.live) 导出 **SVG** 再 Import | 同上导出 **PNG（2x）** 插入，避免小屏糊 |

## Figma 推荐工作流（面试/作品集一页）

1. 新建 Page：**宠伴 / 会议 / 补充项目**。  
2. **Import** 对应 `svg/flow_*.svg` 置于画板顶部作为**时间线条**。  
3. 下方用 Frame 放高保真截屏或 `prototypes/tool_export/figma_frame_import_template.csv` 规划尺寸；线上 HTML 见 `prototypes/manifest.json`。

## 墨刀推荐工作流（国内团队常交付）

1. **流程/说明页**：插入 `svg` 或 mermaid 导出的 **PNG**；旁注用**产品语言**写清每步结论与产出（勿写「对应简历第几句」类对内说明）。  
2. **高保真演示**：新建 **页面** → 组件选 **Web 嵌入 / 网页**（以墨刀当前版本为准）→ URL 填已部署的 `https://anlan-bot.github.io/pm-works-demos/xxx.html`；无公网时用浏览器全屏截图做多状态 Frame。  
3. **版本说明**：在墨刀「备注」里写 **时间锚点**（政企侧活动运营实习 2024.08–2025.08；宠伴 2025.09–；会议 2025.11–），与 PDF 作品集 / 投递材料一致，避免口头与材料不符。

## 其他工具（简述）

- **Sketch / MasterGo / Pixso**：与 Figma 相同，**导入 SVG**。  
- **Axure RP**：SVG 作母版 + **内联框架** 指向本地/线上 `*.html`。  
- **摹客**：类墨刀，**图片 + 网页演示**。

## 维护顺序（避免分叉）

1. 若需与投递用 PDF 对齐：**先改**仓库内简历主档时间线或方法表述，再同步下面各层。  
2. 改 **`demo/work/index.html`**、各 Demo 内 `<details>` 流程（搜 `dev-flow`）；**`dev-flow-kicker`** 需同时维护 **长文案**（`--full`）与 **窄屏短文案**（`--short`，≤640px 显示），并与 **`prototypes/manifest.json`** 里同项目 **`resume_anchor.kicker_*` 对齐**；**各设计文档卡内 `📜 查看完整迭代历史` 列表与嵌入式图表（如会议趋势横轴）**须与 dev-flow 月份一致。  
3. 改 **`mermaid/流程图源码.md`** 与本目录 **`_gen_flow_svgs.py` 内 `DATA`** → 运行 `python _gen_flow_svgs.py` 重写 `svg/*.svg`。  
4. 大段可用脚本 **`_patch_timeline_flows.py`** 做多文件替换（需按当下 `aria-label` 维护脚本内的锚点）。

## 索引

| 项目 | SVG | 案例定位（仓库内） |
|------|-----|-------------------|
| 宠伴 | `svg/flow_01_宠伴.svg` | 主案例 · 2025.09 起 |
| 会议舱 | `svg/flow_02_会议舱.svg` | 主案例 · 2025.11 起 |
| 创作舱 | `svg/flow_03_创作舱.svg` | 补充 |
| 冷启动 | `svg/flow_04_冷启动.svg` | 补充 |
| 剧本舱 | `svg/flow_05_剧本舱.svg` | 补充 |
| Prompt 库 | `svg/flow_06_Prompt库.svg` | 协作向 |

高保真 HTML 与 Frame 尺寸见 `../prototypes/manifest.json`。
