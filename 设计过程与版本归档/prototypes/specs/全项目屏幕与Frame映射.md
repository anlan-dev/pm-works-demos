# 全项目 · 屏幕清单与 Frame 映射

> **时间线锚点**：政企侧活动运营实习 **2024.08–2025.08**；**宠伴** **2025.09 起**、**会议舱** **2025.11 起**。与 PDF 投递材料对齐时在仓库内改主档后再同步各页；流程条矢量见 `../flows/svg/`。

## 宠伴·健康台账 (`pet-vaccine.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 宠伴-首页 | `#page-home`、宠物卡片、月份选择 | 多宠切换、空态 |
| 宠伴-疫苗表单 | `#addVaccineForm` 展开 | 选苗、日期、OCR |
| 宠伴-花费 | 花费 Tab/页面跳转链 | 与 `gotoExpenseLink` 一致 |
| 宠伴-设置/云同步 | `header-cloud-details` | 可选云端 |

**PRD**：`../PRD_01_宠伴健康台账.md`

---

## 会议·反刍舱 (`meeting-ruminant.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 会议-配置区 | API、本地模型、云端勾选 | Mock / 实网 |
| 会议-录音 | 录制控制条 | 未录/录制中 |
| 会议-纪要结构 | 提取后的议题/待办/问题 | 编辑与确认 |
| 会议-待办追踪 | 列表与状态流 | 筛选、优先级 |

**PRD**：`../PRD_02_会议反刍舱.md`

---

## 星途·创作舱 (`creation-cabin.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 创作-侧栏项目 | `#scriptListContainer` | 新建/切换 |
| 创作-大纲 | `#outlineTextArea` | 折叠预览 |
| 创作-角色与世界观 | 角色网格、世界观 | 空态/已填 |
| 创作-正文 | 主编辑区 | 与当前章节绑定 |
| 创作-回顾 | 月度回顾弹层/页 | 与按钮入口一致 |

**PRD**：`../PRD_04_创作舱.md`

---

## Cold Start (`cold-start.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 冷启动-输入 | `#page-launch`、`#goalInput` | 字数提示 |
| 冷启动-结果 | `#resultArea` 三段 | 规则/AI |
| 冷启动-任务 | 任务 Tab 页 | 勾选进度 |
| 冷启动-设置 | 设置弹层 | Key、模式 |

**PRD**：`../PRD_03_冷启动.md`

---

## 剧本·复盘舱 (`script-review.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 剧本-侧栏 | `#scriptListContainer` | 当前高亮 |
| 剧本-记录流 | 记录列表与编辑 | 标签筛选 |
| 剧本-热力图 | `#heatmapBtn` 打开 | 26 周视图 |
| 剧本-看板 | `#kanbanBtn` 打开 | 分列卡片 |

**PRD**：`../PRD_05_剧本复盘舱.md`

---

## Prompt Library (`prompt-library.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| Prompt-导航 | `#catNav` | 分类 active |
| Prompt-卡片流 | `.prompt-card` | 复制后反馈态（若需可截） |

**PRD**：`../PRD_06_Prompt_Library.md`

---

## Figma 操作建议（极简）

1. 新建 File：**PM 作品集 · Demo 映射**。  
2. Page  per project，先 **Place** 对应 `flow_*.svg` 到顶栏。  
3. 每行 Frame 按上表命名，**宽高校验**见 `manifest.json` 的 `suggested_frame_size`。  
4. 高保真：浏览器 **全屏截屏** 或合规 **HTML 导入插件** 放入 Frame（标注「以 HTML 为准」）。

---

## 跨境电商·AI Agent (`cross-border-ai.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 跨境-Agent面板 | 4 Agent 并行卡片 | 比价/关税/物流/推荐 |
| 跨境-拼团 | 阶梯拼团 3/5/10 人 | 价格递减动画 |
| 跨境-到手价 | Hero 到手价计算器 | 商品+运费+关税+汇率 |
| 跨境-下单链路 | 5 步下单（规格→地址→支付→确认→成功） | 物流追踪 |
| 跨境-MCP面板 | 长按 Logo 激活 | 面试官模式 |

**PRD**：`../PRD_08_跨境电商.md`

---

## 住值·租房决策 (`zhuzhi-rent.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 住值-预算 | 贪心预算 + 双层 Bmax | 滑块输入 |
| 住值-AI顾问 | AI 租房建议对话 | Mock 回复 |

**PRD**：`../PRD_07_住值.md`

---

## PixelPick·AI影像精选 (`pixelpick.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| PixelPick-上传 | 拖拽/点击上传区 + Film Strip | 5 步进度条 |
| PixelPick-精选横幅 | Best Banner（大缩略图+评分+维度） | ★ 脉冲动画 |
| PixelPick-网格 | Contact Sheet 网格 + Best 标记 | hover 放大镜波纹 |
| PixelPick-对比 | 放大镜分屏对比 | 全屏模式 |

**架构**：`../architecture/ARCHITECTURE_PixelPick.md`

---

## 雾灯残页·游戏本体 (`mistlamp.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 雾灯-主菜单 | `#menu-overlay`（径向渐变背景） | 新游戏/继续/存档 |
| 雾灯-游戏中 | Header + 属性条 + 叙事 + 分支选择 | 属性门槛可见 |
| 雾灯-存档 | 多槽位存档面板 | 保存/读取/删除 |
| 雾灯-设置 | 三主题切换 | 暗色/更深/羊皮纸 |

**架构**：`../architecture/ARCHITECTURE_Mistlamp.md`

---

## 雾灯残页·AIGC展示 (`vn-game.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 雾灯展示-Hero | Hero + Stats Grid（万字/调用/结局） | 三主题可选 |
| 雾灯展示-过程 | 6 个 AIGC 阶段 Details 面板 | 折叠展开 |
| 雾灯展示-文件 | 文件溯源链接列表 | 可点击 |
| 雾灯展示-架构 | 4 Agent 协作模式说明 | 引用块 + 故事块 |

**架构**：`../architecture/ARCHITECTURE_Mistlamp.md`

---

## 分支树·游戏结构图 (`branch_tree.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| 分支树-展板 | Board 羊皮纸主展板 | 世界观/角色/轴线 |
| 分支树-时间线 | Timeline 章节时序 | 移动端 accordion |
| 分支树-结局 | Ending Grid 结局谱系 | 接入条件+描述 |

**架构**：`../architecture/ARCHITECTURE_分枝树.md`

---

## Demo Hub·导航页 (`demo-hub.html`)

| 建议 Frame 名 | 对应 Demo 区域 | 状态/备注 |
|---------------|----------------|-----------|
| Hub-Hero | Hero + 4 个指标卡片 | 渐变装饰条 |
| Hub-DemoGrid | Demo 双栏卡片列表 | 筛选切换 |
| Hub-Footer | 联系信息 | CTA 按钮 |

**架构**：`../architecture/ARCHITECTURE_DemoHub.md`
