---
version: "2.0"
name: "PixelPick · AI 影像精选"
description: "创作工具类 AI 影像优选工作台，暗房接触印相（Contact Sheet）风格，Apple HIG 暗色（#000000 画布）+琥珀蓝强调（#0071e3），Noto Sans SC + JetBrains Mono，Best 算法+放大镜预览+胶片齿孔进度条。"
product-type: 创作工具类
last-updated: 2026-06-27
colors:
  canvas: "#000000"
  surface: "#1c1c1e"
  card: "#2c2c2e"
  border: "rgba(255,255,255,0.1)"
  border-glow: "rgba(0,113,227,0.3)"
  text-primary: "#f5f5f7"
  text-secondary: "#98989d"
  text-muted: "#6e6e73"
  text-inverse: "#000000"
  accent: "#0071e3"
  accent-glow: "#2997ff"
  accent-dark: "#005bb5"
  success: "#30d158"
  warn: "#ff9f0a"
  danger: "#ff453a"
  chrome: "#3a3a3c"
  chrome-lt: "#636366"
  shadow-card: "0 1px 3px rgba(0,0,0,.3)"
  shadow-elevated: "0 4px 12px rgba(0,0,0,.4)"
  shadow-loupe: "0 0 0 2px var(--accent-glow), 0 8px 24px rgba(0,0,0,.5)"
typography:
  family-sans: "'Noto Sans SC', -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
  family-mono: "'SF Mono', 'Cascadia Code', 'Fira Code', 'JetBrains Mono', Consolas, monospace"
  app-title:
    fontSize: "clamp(1.2rem, 2.5vw, 1.6rem)"
    fontWeight: 700
    letterSpacing: -0.01em
    color: accent-glow
  title:
    fontSize: "0.9rem"
    fontWeight: 600
  body:
    fontSize: "0.68rem"
    fontWeight: 400
    lineHeight: 1.6
  score:
    fontSize: "2.2rem"
    fontWeight: 700
    fontFamily: family-mono
    color: accent-glow
  caption:
    fontSize: "0.6rem"
    fontFamily: family-mono
    color: text-muted
rounded:
  sm: 10px
  md: 14px
  lg: 18px
  pill: 999px
spacing:
  unit: 8px
  sm: 8px
  md: 12px
  lg: 20px
  container-max: 960px
components:
  app-container:
    maxWidth: 960px
    padding: "clamp(16px,3vw,28px) clamp(14px,4vw,32px)"
  header:
    borderBottom: "1px solid border"
    paddingBottom: 14px
  film-strip:
    display: flex
    gap: 0
    notch-active: "accent bg + glow shadow"
    notch-done: "success bg"
  upload-zone:
    backgroundColor: surface
    border: "2px dashed rgba(0,113,227,.18)"
    hover: "border accent-glow + radial glow"
    padding: "clamp(28px,6vw,44px) 24px"
  contact-sheet:
    display: grid
    gridTemplateColumns: "repeat(auto-fill, minmax(clamp(140px,30vw,200px), 1fr))"
    gap: 8px
  print:
    backgroundColor: card
    rounded: sm
    hover: "translateY(-2px) + shadow-loupe"
    aspectRatio: "4/3"
  best-banner:
    background: "linear-gradient(135deg, accent-soft, transparent)"
    border: "1px solid accent-glow"
    padding: "clamp(14px,2.5vw,20px)"
responsive:
  touch-target-min: 44px
  breakpoints:
    mobile: "< 480px — 单列 Header、单列 Contact Sheet"
    tablet: "480-768px — 双列 Contact Sheet"
    desktop: "> 768px — 多列 Contact Sheet、桌面栅格背景"
motion:
  micro: "350ms cubic-bezier(.2,0,0,1)"
  spring: "cubic-bezier(.34,1.56,.64,1)"
  best-pulse: "2s infinite pulse animation on ★ badge"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# PixelPick · AI 影像精选 Design System

## Overview

PixelPick 是一款面向**专业设计师/内容创作者/摄影师**的 AI 影像优选工作台。核心功能：批量上传照片 → Best 算法评分 → 放大镜对比预览 → 一键导出精选集。

### 设计隐喻：暗房接触印相（Contact Sheet）

- **暗室炭黑底**（`#000000` canvas）还原暗房放大机环境
- **琥珀蓝安全灯光**（`#0071e3` accent）模拟暗房 safelight
- **胶片齿孔进度条**（film-strip）暗示摄影工艺流程
- **接触印相网格**（contact-sheet）复刻底片排版方式

### 设计原则

- **专业信任**：深色专业工具风格，Apple HIG 暗色模式规范
- **精度展示**：JetBrains Mono 等宽字体用于评分/尺寸/比例数据
- **聚焦内容**：最小化 chrome，让图片本身成为主角
- **Best 算法可视化**：锯齿切角 + 琥珀标记明确标识最佳选择

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#000000` | 画布底色（暗房） |
| Surface | `#1c1c1e` | 面板层、上传区背景 |
| Card | `#2c2c2e` | 图片卡片、卡片层 |
| Accent | `#0071e3` | Apple Blue 主强调色 |
| Accent Glow | `#2997ff` | 悬停发光、选中态 |
| Success | `#30d158` | 完成态、进度条完成 |
| Chrome | `#3a3a3c` | 金属导轨（分隔线、次要控件） |

## Typography

| 层级 | 字体 | 规格 | 用途 |
|---|---|---|---|
| App Title | Noto Sans SC | 1.2-1.6rem / 700 | 页面标题 |
| Score | JetBrains Mono | 2.2rem / 700 | Best 评分数字 |
| Body | Noto Sans SC | 0.68rem / 400 | 描述文字 |
| Caption | JetBrains Mono | 0.6rem | 尺寸/比例/标签数据 |

## Components

| 组件 | 规格 |
|---|---|
| Header | 底部分割线，左侧标题+副标题 |
| Film Strip | 横向 5 步进度条，active=蓝色发光，done=绿色 |
| Upload Zone | 虚线上传区，hover 蓝色边框 + 径向辉光，44px+ 触控区域 |
| Contact Sheet | 自适应网格，4:3 缩略图，hover 放大镜波纹 + 上浮 |
| Best Print | 蓝色边框 + 右上角 ★ 脉冲动画 + 锯齿切角标记 |
| Best Banner | 渐变背景精选横幅，大缩略图+评分+维度标签 |
| Darkroom Panel | 半透明面板，圆角 14-18px，shadow-elevated |

## Layout

| 断点 | 布局 |
|---|---|
| Mobile (< 480px) | 单列 Header（垂直排列），单列 Contact Sheet |
| Tablet (480-768px) | 双列 Contact Sheet |
| Desktop (> 768px) | 多列 Contact Sheet + 栅格背景纹理 |

## Page Structure

```
Header（暗房门牌）
├── App Title + 副标题

Film Strip（5 步进度）
├── 上传 → 分析 → 精选 → 对比 → 导出

Toolbar（操作栏）
├── 全选/取消 + Best筛选 + 网格/列表切换

Best Banner（精选横幅）
├── 最佳图片缩略图
├── AI 评分数字
├── 入选理由
└── 维度标签（构图/曝光/对焦/色彩）

Contact Sheet（接触印相网格）
├── 每张照片: 缩略图 + 文件名 + 尺寸
├── Best: ★ 标记 + 蓝色边框
└── 悬停: 放大镜波纹 + 上浮

Empty State（暗房空态）
├── 放大机图标
└── 引导上传文字
```

## Motion

| 动效 | 规格 |
|---|---|
| Best Pulse | ★ 标记 2s 脉冲动画，缩放 1→1.2→1 |
| Card Hover | 350ms ease-out，上浮 2px + 蓝色辉光 |
| Upload Zone | hover 径向辉光扩散 + 边框变色 |
| Notch Active | ease-spring 弹性动画 |
| Stagger Delay | +50ms per card in contact sheet |
