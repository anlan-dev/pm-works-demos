# DESIGN.md · 王天娇作品集设计系统

> 基于 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 的理念，为每个项目创建 DESIGN.md 文件。
> 将 DESIGN.md 放入项目根目录，AI 编码工具即可生成一致的 UI。

---

## 什么是 DESIGN.md？

[DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) 是 Google Stitch 提出的概念——一份给 AI 看的纯文本设计系统说明书。

| 文件 | 谁读 | 定义什么 |
|------|------|---------|
| `AGENTS.md` | 编码 Agent | 如何构建项目 |
| `DESIGN.md` | 设计 Agent | 项目应该长什么样 |

**本仓库为 14 篇 DESIGN.md 提供即用设计规范（覆盖 13 个项目 + 1 个 UIwork 合集）。**

---

## 统一设计语言

### Token 三层体系

```
Layer 1: Global Tokens（全局原始值）
├── --color-blue-500: #0071e3
├── --color-gray-100: #f5f5f7（画布）
├── --color-gray-50: #ffffff（卡片）
├── --color-gray-900: #1d1d1f（主文字）
├── --color-gray-600: #6e6e73（辅助文字）
├── --font-sans: 'Inter', 'Noto Sans SC', system-ui
├── --font-mono: 'JetBrains Mono', monospace
├── --space-unit: 4px（4/8/12/16/24/32/48）
├── --radius-sm: 8px / --radius-md: 12px / --radius-lg: 16px
└── --shadow: 0 2px 8px rgba(0,0,0,.06)

Layer 2: Alias Tokens（语义化别名）
├── --color-primary: 按产品类型分配
├── --color-surface: #ffffff
├── --color-background: #f5f5f7
└── --color-text-primary: #1d1d1f

Layer 3: Component Tokens（组件级）
├── --button-height: 44px
├── --card-padding: 16-24px
├── --input-height: 44px
└── --nav-height: 56px
```

### 通用规范

| 规范 | 标准 |
|------|------|
| **字体** | Inter + Noto Sans SC（正文），JetBrains Mono（代码） |
| **字号** | 标题 18-24px/600，正文 14px/400，辅助 12px/500 |
| **画布** | `#f5f5f7`（浅灰） |
| **卡片** | `#ffffff`（纯白）+ `0 2px 8px rgba(0,0,0,.06)` |
| **圆角** | sm=8px / md=12px / lg=16px / pill=9999px |
| **间距** | 4px 基准（4/8/12/16/24/32/48） |
| **触控** | 最小 44×44px |
| **动效** | 200ms ease-out 微交互，300ms ease-out 页面切换 |
| **可访问性** | WCAG AA 对比度，prefers-reduced-motion 支持 |

---

## 📁 项目设计系统

### 🏥 健康医疗类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **宠伴·健康台账** | [pet-vaccine/DESIGN.md](./pet-vaccine/DESIGN.md) | 工具效率类 | `#0071e3` | 白卡片+浅灰画布，Inter 字体，宠物疫苗/驱虫/体检记录 |
| **会议·反刍舱** | [meeting-ruminant/DESIGN.md](./meeting-ruminant/DESIGN.md) | 工具效率类 | `#0071e3` | 白卡片+浅灰画布，Inter 字体，录音转写+会议复盘 |

### 🏠 生活服务类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **住值·租房决策** | [zhuzhi-rent/DESIGN.md](./zhuzhi-rent/DESIGN.md) | 工具效率类 | `#10b981` | 白卡片+浅灰画布，双轴图表，滑块输入，租房计算器 |
| **冷启动·行动引擎** | [cold-start/DESIGN.md](./cold-start/DESIGN.md) | 工具效率类 | `#0071e3` | 白卡片+浅灰画布，极简风格，倒计时启动器 |

### 🎨 创作工具类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **星途·创作舱** | [creation-cabin/DESIGN.md](./creation-cabin/DESIGN.md) | 消费娱乐类 | `#667eea` | 品牌渐变+白卡片，4 套主题，角色管理+大纲+多格式导出 |
| **剧本·进度复盘** | [script-review/DESIGN.md](./script-review/DESIGN.md) | 消费娱乐类 | `#e74c3c` | 剧场红+白卡片，热力图看板+词云+场景卡片 |

### 🌐 跨境电商类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **GlobalFUN·跨境拼团** | [cross-border-ai/DESIGN.md](./cross-border-ai/DESIGN.md) | 企业服务类 | `#1e4a6b` | 深蓝专业+白卡片，中/英/日三语 i18n，双币价格 |

### 🛠 工具效率类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **Prompt Library** | [prompt-library/DESIGN.md](./prompt-library/DESIGN.md) | 工具效率类 | `#0071e3` | 白卡片+浅灰画布，JetBrains Mono 代码块，搜索+收藏+使用统计 |

### 🎮 游戏/叙事类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **Mistlamp · 雾灯残页** | [mistlamp/DESIGN.md](./mistlamp/DESIGN.md) | 消费娱乐类 | `#b8905e` | 哥特暗色文字冒险游戏，衬线正文+古铜金强调，属性条+分支选择+存档 |
| **雾灯残页 · AIGC 展示** | [vn-game/DESIGN.md](./vn-game/DESIGN.md) | 消费娱乐类 | `#c49a6c` | AIGC 开发过程展示页，三主题切换（dark/ink/default），Stats Grid |
| **Branch Tree · 结构图** | [branch-tree/DESIGN.md](./branch-tree/DESIGN.md) | 数据可视化类 | `#7d5b2a` | 羊皮纸手稿风格叙事分支图，Georgia 衬线+做旧质感，Timeline+结局谱系 |

### 🎨 创作工具类 · 扩展

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **PixelPick · AI 影像精选** | [pixelpick/DESIGN.md](./pixelpick/DESIGN.md) | 创作工具类 | `#0071e3` | 暗房接触印相风格，Apple HIG 暗色+琥珀蓝，Best 算法+ Contact Sheet 网格+放大镜预览 |

### 🧭 导航/门户类

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **Demo Hub · 导航页** | [demo-hub/DESIGN.md](./demo-hub/DESIGN.md) | 工具/导航类 | `#4f46e5` | 面试官视角门户，蓝紫渐变+白卡片，指标卡片+双栏Demo陈列+快速入口 |

### 🖼 UI 设计作品集

| 项目 | DESIGN.md | 产品类型 | 主色 | 描述 |
|------|-----------|---------|------|------|
| **UIwork · 11 风格 Demo** | [UIwork/DESIGN.md](./UIwork/DESIGN.md) | UI 设计展示类 | `#a78bfa` | 暗色画廊框架，11 个风格 Demo（玻璃态/赛博朋克/日式极简/粗野主义等） |

---

## 🎨 四类产品设计风格

### A. 工具效率类（pet-vaccine / meeting-ruminant / zhuzhi-rent / cold-start / prompt-library）

```
画布：#f5f5f7 | 卡片：#ffffff | 主色：#0071e3（或按产品定制）
阴影：0 2px 8px rgba(0,0,0,.06) | 圆角：8/12/16px
字体：Inter + Noto Sans SC | 动效：200ms ease-out
```

### B. 消费娱乐类（creation-cabin / script-review）

```
画布：#f5f5f7 | 卡片：#ffffff | 主色：品牌定制
阴影：0 2px 8px rgba(0,0,0,.06) | 圆角：8/12/16px
字体：Inter + Noto Sans SC + Display 字体 | 动效：弹性 cubic-bezier(.34,1.56,.64,1)
```

### C. 企业服务类（cross-border-ai）

```
画布：#f8fafc | 卡片：#ffffff | 主色：#1e4a6b
阴影：0 2px 8px rgba(0,0,0,.06) | 圆角：8/12/16px
字体：Inter + Noto Sans SC | 动效：克制，仅功能性
```

### D. 暗色沉浸类（PixelPick / Mistlamp / 雾灯残页 / Branch Tree）

```
画布：#000000 ~ #0f0e0c | 卡片：暗色调 | 主色：琥珀蓝/古铜金
阴影：0 4px 16px rgba(0,0,0,.4) | 圆角：8/10/12px
字体：Noto Sans SC / Noto Serif SC / JetBrains Mono | 动效：克制，仅功能性
```

### E. 创新实验类（UIwork 08-11）

```
按风格定制（玻璃拟态/赛博朋克/日式极简/粗野主义）
详见 UIwork/DESIGN.md
```

### F. 导航/门户类（Demo Hub）

```
画布：#fafbfd | 卡片：#ffffff | 主色：#4f46e5（蓝紫渐变）
阴影：多层 shadow（sm→md→lg→xl） | 圆角：8/12/16/20px
字体：Inter | 动效：200ms cubic-bezier(.4,0,.2,1)

---

## 📦 每个 DESIGN.md 包含

| 章节 | 内容 |
|------|------|
| 1. Overview | 产品定位、设计原则 |
| 2. Colors | 语义色 + 功能角色（已对齐实际 CSS 变量） |
| 3. Typography | 字体栈、层级表（Inter + Noto Sans SC） |
| 4. Components | 按钮、卡片、输入框、导航（标准阴影+圆角） |
| 5. Layout | 间距（4px 基准）、网格、留白 |
| 6. Responsive | 断点、触控目标（44px）、viewport 配置 |
| 7. Motion | 动效规范、prefers-reduced-motion |
| 8. Accessibility | WCAG AA、键盘导航、焦点状态 |

---

## 🚀 使用方法

1. 选择一个项目的 `DESIGN.md`
2. 复制到你的项目根目录
3. 告诉 AI Agent："按照 DESIGN.md 的规范构建 UI"

### 示例 Prompt

```
请按照 DESIGN.md 的设计规范，构建一个宠物健康记录页面。
要求：
- 使用白卡片+浅灰画布风格（参考 DESIGN.md 中的色彩系统）
- 主色调使用 #0071e3
- 卡片圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06)
- 字体使用 Inter + Noto Sans SC
- 移动端优先，响应式布局，最小触控目标 44px
```

---

## 🔗 相关资源

- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - 62.8k stars，55+ 大厂设计系统
- [Google Stitch](https://stitch.withgoogle.com/) - AI 驱动的 UI 生成工具
- [DESIGN.md 格式文档](https://stitch.withgoogle.com/docs/design-md/format/)

---

**作者**：王天娇 · PM Portfolio
**GitHub**：[anlan-dev/pm-works-demos](https://github.com/anlan-dev/pm-works-demos)
**最后更新**：2026-06-28
