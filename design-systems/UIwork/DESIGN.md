---
version: "2.0"
name: "UIwork · UI 设计作品集（11 风格 Demo）"
description: "产品经理视角的 UI 设计作品集展示页，暗色画廊框架（#050507 画布）+ 11 个独立风格 Demo，涵盖玻璃态/赛博朋克/日式极简/粗野主义/新拟物等前沿设计风格。"
product-type: UI 设计展示类
last-updated: 2026-06-19
colors:
  canvas: "#050507"
  canvas2: "#0c0c10"
  card: "#111115"
  card-hover: "#16161c"
  text-primary: "#f0f0f5"
  text-secondary: "#8b8b9e"
  text-tertiary: "#5a5a6e"
  accent: "#a78bfa"
  accent2: "#60a5fa"
  accent3: "#34d399"
  border: "#1e1e28"
  border-hover: "#2a2a3a"
  glow: "rgba(167,139,250,0.12)"
  nav-bg: "rgba(5,5,7,0.7)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  hero-title:
    fontSize: "clamp(2.4rem, 6vw, 4rem)"
    fontWeight: 900
    letterSpacing: -0.05em
    lineHeight: 1.1
  hero-gradient:
    background: "linear-gradient(135deg, accent, accent2, accent3)"
  section-title:
    fontSize: "clamp(1.5rem, 3vw, 2.2rem)"
    fontWeight: 800
    letterSpacing: -0.03em
  section-eyebrow:
    fontSize: "0.75rem"
    fontWeight: 600
    textTransform: uppercase
    letterSpacing: 0.15em
    color: accent
  project-title:
    fontSize: "1.5rem"
    fontWeight: 800
    letterSpacing: -0.03em
  project-subtitle:
    fontSize: "0.9rem"
    color: text2
    lineHeight: 1.7
rounded:
  card: 20px
  tag: 999px
  iframe: inherit
spacing:
  container-max: 1100px
  nav-height: 64px
  hero-padding: "160px 0 100px"
  section-padding: "80px 0"
  card-gap: 32px
components:
  nav:
    position: fixed
    top: 0
    height: 64px
    background: "rgba(5,5,7,0.7)"
    backdropFilter: "blur(20px) saturate(1.8)"
    borderBottom: "1px solid border"
  nav-logo:
    fontSize: "1.1rem"
    fontWeight: 800
    gradient: "accent → accent2"
  hero:
    textAlign: center
    radialGlow: "accent radial gradient"
    badge: "暗色胶囊 + 绿点脉冲动画"
  project-card:
    display: grid
    gridTemplateColumns: "1fr 1fr"
    border: "1px solid border"
    rounded: 20px
    overflow: hidden
    preview: "200% iframe + scale(0.5) 模拟真实渲染"
    hover: "border-hover + shadow 0 24px 80px + scale(1.02)"
  flow-card:
    backgroundColor: "#0f0f14"
    border: "1px solid border"
    rounded: 16px
  design-principle-card:
    backgroundColor: card
    border: "1px solid border"
    rounded: 16px
responsive:
  touch-target-min: 44px
  breakpoints:
    mobile: "< 768px — 单列展示卡、Hero 缩小、Nav 折叠"
    tablet: "768-1024px — 双列展示卡"
    desktop: "> 1024px — 双列 iframe + 信息"
motion:
  fadeUp: "0.8s ease, translateY(24px)→0, opacity 0→1, staggered delays"
  gradientShift: "6s infinite gradient background-position shift"
  pulse: "2s infinite opacity pulse on green dot"
  card-hover: "0.4s cubic-bezier(.4,0,.2,1), shadow + border + preview scale(1.02)"
---

# UIwork · UI 设计作品集 Design System

## Overview

UIwork 是王天娇的 **UI 设计能力展示页**（[UIwork/index.html](../../UIwork/index.html)），包含 11 个独立风格的 UI Demo，以 PM 视角呈现每个设计背后的商业逻辑与用户场景。

### 设计原则

- **暗色画廊**：深色框架让彩色 Demo 更突出，noise texture 增加质感
- **PM 视角**：每个 Demo 附带设计决策文档（为什么选这个风格/配色/交互）
- **iframe 预览**：双栏卡片（1:1）通过 iframe scale 技巧展示真实渲染效果
- **分层呈现**：Hero（第一印象）→ Design Process（方法论）→ Projects（案例）→ Principles（原则）

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#050507` | 深色画布 |
| Card | `#111115` | 项目卡片背景 |
| Card Hover | `#16161c` | 卡片悬停态 |
| Text | `#f0f0f5` | 主文字 |
| Text2 | `#8b8b9e` | 辅助文字 |
| Accent | `#a78bfa` | 紫色强调（Hero 渐变、标签） |
| Accent2 | `#60a5fa` | 蓝色辅助（渐变配合） |
| Accent3 | `#34d399` | 绿色点缀（状态点、成功标记） |
| Border | `#1e1e28` | 默认边框 |
| Glow | `rgba(167,139,250,0.12)` | 紫色辉光 |

## Typography

| 层级 | 规格 | 用途 |
|---|---|---|
| Hero Title | 2.4-4rem / 900 / -0.05em | 页面大标题（多色渐变） |
| Section Title | 1.5-2.2rem / 800 / -0.03em | 区块标题 |
| Section Eyebrow | 0.75rem / 600 / uppercase | 区块分类标签 |
| Project Title | 1.5rem / 800 | 项目卡片标题 |
| Project Subtitle | 0.9rem / 400 | 项目描述 |
| Tag | 0.7rem / 600 | 胶囊标签 |

## Gallery Components

| 组件 | 规格 |
|---|---|
| Nav | 固定顶部 64px，毛玻璃 blur(20px) saturate(1.8) |
| Project Card | 双栏 Grid（1:1），20px 圆角，hover 辉光+阴影 |
| iFrame Preview | 200% 缩放 + scale(0.5)，模拟 360px 高度预览 |
| Design Flow Card | 暗色卡片 16px 圆角，展示 PM 设计流程 |
| Design Principles | 4 列 Grid 原则卡片 |

---

## 11 个 UI 风格 Demo 设计规范

### 01 · Finance Dashboard（金融数据看板）

| 属性 | 值 |
|---|---|
| **风格** | 专业深色数据看板 |
| **画布** | `#0f111a` |
| **卡片** | `#1a1d2e` |
| **主色** | `#3b82f6`（蓝） |
| **强调** | `#10b981`（绿·涨）/ `#ef4444`（红·跌） |
| **字体** | Inter + JetBrains Mono（数据） |
| **特点** | 网格背景 + 渐变走势图 + KPI 卡片 |
| **目标用户** | 金融从业者、数据分析师 |
| **设计决策** | 深色减少眼疲劳，等宽数字确保数据对齐 |

### 02 · Health Tracker（健康追踪）

| 属性 | 值 |
|---|---|
| **风格** | 清新浅色健康风 |
| **画布** | `#f8fafc` |
| **主色** | `#0ea5e9`（蓝） / `#10b981`（绿） |
| **字体** | Inter + Noto Sans SC |
| **特点** | 圆环图表 + 步数/心率/睡眠三指标 |
| **目标用户** | 健康意识强的都市白领 |
| **设计决策** | 圆环提供进度直观感知，三指标一屏呈现减少切换 |

### 03 · SaaS Pricing（SaaS 定价页）

| 属性 | 值 |
|---|---|
| **风格** | B2B 专业定价页 |
| **画布** | `#ffffff` |
| **主色** | `#6366f1`（紫） |
| **字体** | Inter |
| **特点** | 三栏定价对比 + Feature 对比表 + FAQ |
| **目标用户** | SaaS 采购决策者 |
| **设计决策** | 中栏高亮（视觉锚点），功能对比表降低决策成本 |

### 04 · Pet Vaccine（毛孩疫苗本）

| 属性 | 值 |
|---|---|
| **风格** | 新拟物（Neumorphism） |
| **画布** | `#e6e6e6` |
| **主色** | `#0071e3`（蓝） |
| **字体** | Inter + Noto Sans SC |
| **特点** | 凸起/凹陷阴影 + 48px+ 触控区域 |
| **目标用户** | 宠物主人 |
| **设计决策** | 柔软质感降低医疗感，大触控适配单手操作 |
| **详细规范** | → [pet-vaccine/DESIGN.md](../pet-vaccine/DESIGN.md) |

### 05 · Cross-Border AI（跨境电商 AI）

| 属性 | 值 |
|---|---|
| **风格** | 专业企业蓝 |
| **画布** | `#f8fafc` |
| **主色** | `#1e4a6b`（深蓝） |
| **字体** | Inter |
| **特点** | 4 Agent 并行卡片 + 翻转动画 + 双币价格 |
| **目标用户** | 跨境购物消费者 |
| **设计决策** | 深蓝传递信任，翻转动画增加交互趣味 |
| **详细规范** | → [cross-border-ai/DESIGN.md](../cross-border-ai/DESIGN.md) |

### 06 · Creation Cabin（创作舱）

| 属性 | 值 |
|---|---|
| **风格** | 创意工具 |
| **画布** | `#f5f5f7` |
| **主色** | `#667eea`（品牌渐变） |
| **字体** | Inter |
| **特点** | 4 套主题 + 角色管理 + 大纲树 + 多格式导出 |
| **目标用户** | 小说创作者 |
| **设计决策** | 4 主题切换适配不同创作心境 |
| **详细规范** | → [creation-cabin/DESIGN.md](../creation-cabin/DESIGN.md) |

### 07 · Prompt Library（Prompt 库）

| 属性 | 值 |
|---|---|
| **风格** | 开发者工具风 |
| **画布** | `#f5f5f7` |
| **主色** | `#0071e3` |
| **字体** | Inter + JetBrains Mono（代码） |
| **特点** | 搜索+收藏+使用统计+代码高亮 |
| **目标用户** | AI 开发者/Prompt 工程师 |
| **设计决策** | 代码块 JetBrains Mono，收藏功能降低重复搜索 |
| **详细规范** | → [prompt-library/DESIGN.md](../prompt-library/DESIGN.md) |

### 08 · Glassmorphism（玻璃态音乐播放器）

| 属性 | 值 |
|---|---|
| **风格** | 玻璃拟态（Glassmorphism） |
| **画布** | `#0a0a12` |
| **玻璃** | `rgba(255,255,255,0.06)` + `backdrop-filter: blur(24px)` |
| **主色** | `#e94560`（霓虹红） |
| **字体** | Inter（300-900 全字重） |
| **圆角** | 32px（播放器）/ 16px（卡片）/ 999px（按钮） |
| **动效** | 黑胶旋转 20s / 音波跳跃 / scroll-reveal |
| **目标用户** | Z 世代音乐爱好者 |
| **设计决策** | 玻璃层叠营造深度感，韵律波动画提供感官反馈，大封面聚焦音乐本身 |

### 09 · Cyberpunk（赛博朋克数据看板）

| 属性 | 值 |
|---|---|
| **风格** | 赛博朋克 / 霓虹暗色 |
| **画布** | `#050508` + 网格线纹理 |
| **卡片** | `rgba(18,18,26,0.8)` + 品红边框 |
| **主色** | `#ff00ff`（品红）/ `#00ffff`（青）/ `#00ff88`（绿） |
| **字体** | Inter + JetBrains Mono（数据） |
| **圆角** | 4px（锐角）/ 8px（卡片）/ 12px（面板） |
| **动效** | 渐变移位 6s / 霓虹 text-shadow 辉光 |
| **目标用户** | 游戏运营、数据分析师 |
| **设计决策** | 网格线背景营造工业感，霓虹色增强数据层级，JetBrains Mono 等宽数字 |

### 10 · Japanese Minimalism（日式极简任务管理）

| 属性 | 值 |
|---|---|
| **风格** | 日式极简 / 侘寂美学 |
| **画布** | `#f5f3ef`（米白） |
| **卡片** | `#ffffff`（纯白） |
| **主色** | `#c0392b`（朱红·唯一强调色） |
| **字体** | Noto Serif SC（标题）+ Inter（正文） |
| **圆角** | 4px（微妙）/ 8px（卡片） |
| **特色** | 大量留白（Ma/间）、衬线标题人文温度、虚线添加按钮 |
| **目标用户** | 追求品质感的创意工作者 |
| **设计决策** | 留白减少认知负荷，红色唯一强调精准引导注意，米白画布模拟纸张质感 |

### 11 · Brutalism（粗野主义品牌展示）

| 属性 | 值 |
|---|---|
| **风格** | 粗野主义（Brutalism） |
| **画布** | `#ffffff` |
| **文字** | `#000000` 纯黑 + `#ff0000` 正红 |
| **字体** | Inter（800/900 超粗字重） |
| **圆角** | 0px（无圆角，全部直角） |
| **边框** | 3px solid black（厚重边框） |
| **特色** | 超大字号排版即图形、故意粗糙、高对比、红色点缀 |
| **目标用户** | 先锋品牌/潮牌/艺术机构 |
| **设计决策** | 不妥协的态度（无圆角+粗边框），纯黑白+红最极端对比，反精致=记忆点 |

---

## PM 设计流程（Gallery 页面展示）

```
Empathize → Define → Ideate → Prototype → Test → Iterate
    ↓           ↓          ↓          ↓         ↓         ↓
 用户研究    需求定义    方案发散    高保真    可用性    数据驱动
  Persona    JTBD       Crazy 8    Figma    测试      迭代
```

## Layout

| 断点 | 布局 |
|---|---|
| Mobile (< 768px) | 单列卡片，Hero 文字缩小，Nav 简化 |
| Tablet (768-1024px) | 双列项目卡 |
| Desktop (> 1024px) | 双栏项目卡（1:1 iframe+信息），四列方法论 |

## Motion

| 动效 | 规格 |
|---|---|
| Hero Fade Up | 0.8s ease，stagger 延迟（0s / 0.1s / 0.2s / 0.3s） |
| Gradient Shift | Hero 渐变文字 6s 无限循环位移 |
| Pulse | 绿色状态点 2s 无限闪烁 |
| Card Hover | 0.4s cubic-bezier(.4,0,.2,1)，预览区 scale(1.02) |
| Noise Texture | SVG feTurbulence 全屏覆盖叠加（opacity 0.03） |

---

## 相关规范文件

- [设计规范_色彩与字体系统.md](../../设计参考/设计规范_色彩与字体系统.md) — 全 11 Demo 统一色彩与字体 Token
- [设计规范_组件与布局系统.md](../../设计参考/设计规范_组件与布局系统.md) — 布局系统与组件规范
- [设计规范_交互逻辑与动效.md](../../设计参考/设计规范_交互逻辑与动效.md) — 手势交互与动效系统
- [modao-annotations.css](../../UIwork/modao-annotations.css) — 墨刀标注样式（PM 评审用）
- [modao-annotations.js](../../UIwork/modao-annotations.js) — 墨刀标注交互逻辑
