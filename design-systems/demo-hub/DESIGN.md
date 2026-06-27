---
version: "2.0"
name: "Demo Hub · 作品集导航页"
description: "工具/导航类作品集门户，专业蓝紫渐变（#667eea→#764ba2）+白卡片，Inter 字体，面试官视角指标卡片+双栏Demo陈列+快速入口。"
product-type: 工具/导航类
last-updated: 2026-06-19
colors:
  canvas: "#fafbfd"
  canvas2: "#f0f4f8"
  surface: "#ffffff"
  surface-hover: "#f8fafc"
  surface-glass: "rgba(255,255,255,0.8)"
  primary: "#4f46e5"
  primary-light: "#818cf8"
  primary-soft: "rgba(79,70,229,0.08)"
  primary-glow: "rgba(79,70,229,0.15)"
  success: "#10b981"
  success-soft: "rgba(16,185,129,0.08)"
  warning: "#f59e0b"
  warning-soft: "rgba(245,158,11,0.08)"
  text-primary: "#1a1a2e"
  text-secondary: "#4a5568"
  text-tertiary: "#718096"
  text-inverse: "#ffffff"
  border: "rgba(0,0,0,0.06)"
  border-light: "rgba(0,0,0,0.04)"
  shadow-sm: "0 1px 2px rgba(0,0,0,0.05)"
  shadow-md: "0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06)"
  shadow-lg: "0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05)"
  shadow-xl: "0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04)"
  gradient-brand: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
typography:
  family: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
  hero-title:
    fontSize: 32px
    fontWeight: 800
    letterSpacing: -0.02em
    background: "linear-gradient(135deg, var(--text-primary), var(--accent))"
    webkitBackgroundClip: text
    webkitTextFillColor: transparent
  section-title:
    fontSize: 24px
    fontWeight: 700
  card-title:
    fontSize: 16px
    fontWeight: 600
  metric-value:
    fontSize: 28px
    fontWeight: 800
    color: accent
  body:
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
  caption:
    fontSize: 12px
    fontWeight: 500
rounded:
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
spacing:
  unit: 4px
  container-max: 1200px
  hero-padding: 40px
  wrap-padding: "40px 24px 80px"
components:
  hero:
    backgroundColor: surface
    border: "1px solid border"
    rounded: xl
    padding: 40px
    boxShadow: shadow-lg
    topBar: "4px gradient-brand bar"
  metric-card:
    backgroundColor: surface
    border: "1px solid border"
    rounded: lg
    padding: 24px
    hover: "translateY(-4px) + shadow-md"
  demo-card:
    display: grid
    gridTemplateColumns: "200px 1fr"
    hover: "translateY(-2px) + shadow-lg"
  tag:
    backgroundColor: "primary-soft"
    color: primary
    rounded: 20px
    fontSize: 12px
    fontWeight: 600
  button-primary:
    backgroundColor: primary
    color: text-inverse
    rounded: md
    height: 44px
    hover: "brightness(1.1) + translateY(-1px)"
responsive:
  touch-target-min: 44px
  mobile-nav: "底部固定网格导航"
  breakpoints:
    mobile: "< 640px — 单列卡片、堆叠指标"
    tablet: "640-1024px — 双列指标"
    desktop: "> 1024px — 四列指标 + 双栏Demo"
motion:
  micro: "200ms cubic-bezier(.4,0,.2,1)"
  card-hover: "translateY(-2px) + shadow-lg"
  stagger: "+50ms"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# Demo Hub · 作品集导航页 Design System

## Overview

Demo Hub 是王天娇 AI 产品经理作品集的**统一导航门户**（demo/work/demo-hub.html），面向面试官/招聘方，展示 13 个从 0 到 1 的可交互产品 Demo。

### 设计原则

- **面试官优先**：Hero 区域用核心指标（项目数、用户数、AI功能覆盖率）建立第一印象
- **快速扫描**：双栏 Demo 卡片（缩略图+描述），支持按产品类型筛选
- **品牌一致性**：蓝紫渐变与主作品集（[index.html](../../index.html)）保持视觉延续
- **分层信息**：Hero → 指标 → 筛选 → Demo列表 → 页脚

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#fafbfd` | 主画布，冷白底色 |
| Canvas2 | `#f0f4f8` | 次级区域背景 |
| Surface | `#ffffff` | 卡片、Hero |
| Primary | `#4f46e5` | CTA、强调色 |
| Primary Light | `#818cf8` | 悬停态 |
| Success | `#10b981` | 正向指标、完成态 |
| Warning | `#f59e0b` | 开发中标签 |
| Text Primary | `#1a1a2e` | 主文字 |
| Text Secondary | `#4a5568` | 描述文字 |
| Text Tertiary | `#718096` | 辅助信息 |

### 品牌渐变

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

用于 Hero 顶部装饰条、标题渐变文字、CTA 按钮悬停态。

## Typography

| 层级 | 规格 | 用途 |
|---|---|---|
| Hero Title | 32px / 800 / -0.02em | 页面主标题（渐变文字） |
| Section Title | 24px / 700 | 区块标题 |
| Card Title | 16px / 600 | Demo 卡片名称 |
| Body | 16px / 400 / 1.7 | 描述段落 |
| Metric Value | 28px / 800 | 核心指标数字 |
| Caption | 12px / 500 | 标签、辅助文字 |

## Components

| 组件 | 规格 |
|---|---|
| Hero Card | 白卡片，顶部 4px 渐变条，圆角 20px，阴影 lg |
| Metric Card | 4 列网格，图标+数字+标签，hover 上浮 4px |
| Demo Card | 双栏 Grid（200px+1fr），缩略图+元信息+快速入口 |
| Filter Tags | 圆角 20px 药丸标签，accent-soft 背景 |
| CTA Button | 高度 44px，圆角 12px，primary 背景，hover 提亮+上浮 |
| Back to Top | 固定右下角 FAB，圆形 48px，渐变背景 |

## Layout

| 断点 | 布局 |
|---|---|
| Mobile (< 640px) | 单列卡片 + 2 列指标 + 底部导航 |
| Tablet (640-1024px) | 双列指标 + 单列 Demo |
| Desktop (> 1024px) | 四列指标 + 双栏 Demo（缩略图+描述） |

## Page Structure

```
Hero（面试官第一印象）
├── 渐变装饰条
├── 标题 + 副标题
├── 4 个核心指标卡片（项目数/用户数/AI功能/可用性评分）
└── 3 个快速入口 CTA

筛选区
├── 产品类型标签（全部/工具效率/消费娱乐/企业服务）
└── Demo 卡片网格（双栏布局）
    ├── 项目缩略图（左侧 200px）
    └── 项目信息（右侧）
        ├── 名称 + 阶段徽章
        ├── 一句话描述
        ├── 技术标签
        └── [查看Demo] 按钮

页脚
└── 联系信息 + 版权
```

## Motion

| 动效 | 规格 |
|---|---|
| 卡片悬停 | 200ms ease，translateY(-2px)，shadow-xl |
| 指标入场 | stagger 50ms，fade-up |
| 标签点击 | 缩放反馈 0.95 |
| 页面滚动 | smooth scroll-behavior |
