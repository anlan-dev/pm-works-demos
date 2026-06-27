---
version: "2.0"
name: "Mistlamp · 雾灯残页（交互游戏本体）"
description: "消费娱乐类哥特暗色文字冒险游戏，深褐羊皮纸底色（#0c0b09）+古铜金强调（#b8905e），Noto Serif SC 衬线正文 + Noto Sans SC UI，属性条+叙事文本+分支选择+存档系统。"
product-type: 消费娱乐类
last-updated: 2026-06-27
colors:
  canvas: "#0c0b09"
  canvas2: "#161412"
  surface: "#1a1816"
  text-primary: "#d8cfc0"
  text-muted: "#7a7060"
  accent: "#b8905e"
  accent2: "#d4a868"
  danger: "#9e7a7a"
  success: "#7a9e7e"
  border: "rgba(184,144,94,0.12)"
  shadow: "0 4px 16px rgba(0,0,0,0.4)"
  radius: 10px
typography:
  font-body: "'Noto Serif SC', Georgia, serif"
  font-ui: "'Noto Sans SC', system-ui, sans-serif"
  menu-title:
    fontSize: "clamp(2rem, 6vw, 3.2rem)"
    fontWeight: 700
    color: accent
    letterSpacing: 0.15em
    textShadow: "0 2px 12px rgba(184,144,94,0.3)"
  subtitle:
    fontSize: "clamp(0.65rem, 1.5vw, 0.85rem)"
    fontWeight: 500
    letterSpacing: 0.4em
    textTransform: uppercase
  tagline:
    fontSize: "clamp(0.82rem, 1.8vw, 0.95rem)"
    fontStyle: italic
  narrative:
    fontSize: 16px
    lineHeight: 1.8
    fontFamily: font-body
  game-header:
    fontSize: "clamp(1rem, 2.5vw, 1.3rem)"
    fontWeight: 600
    color: accent
    letterSpacing: 0.08em
rounded:
  btn: 10px
  stat: 6px
spacing:
  game-max-width: 680px
  menu-btn-max: 280px
  stats-gap: "clamp(6px, 1.5vw, 10px)"
components:
  menu-overlay:
    background: "radial-gradient(ellipse at 50% 30%, #1a1610 0%, canvas 70%)"
    minHeight: "100dvh"
    textAlign: center
  menu-btn:
    height: "clamp(12px, 2.5vw, 16px) 24px"
    minHeight: 48px
    backgroundColor: surface
    border: "1px solid border"
    rounded: btn
    hover: "accent bg + accent border + accent text"
    active: "scale(0.97)"
  menu-btn-primary:
    background: "linear-gradient(135deg, accent, #8a6838)"
    color: "#ffffff"
    fontWeight: 600
  game-container:
    maxWidth: 680px
    padding: "clamp(12px, 3vw, 24px) clamp(12px, 3vw, 20px)"
  header:
    display: flex
    gap: 12px
    borderBottom: "1px solid border"
    position: sticky
    top: 0
    zIndex: 10
    background: canvas
  stats-bar:
    display: flex
    flexWrap: wrap
    gap: stats-gap
  narrative-block:
    lineHeight: 1.8
    fontFamily: font-body
  choice-btn:
    display: block
    width: 100%
    minHeight: 48px
    backgroundColor: surface
    border: "1px solid border"
    hover: "accent bg accent border accent text"
    active: "scale(0.98)"
responsive:
  touch-target-min: 48px
  safe-area: "env(safe-area-inset-*) for notch/bar"
  breakpoints:
    mobile: "全宽单列，菜单文字缩小"
    desktop: "max-width 680px 居中"
motion:
  micro: "0.2s ease"
  active: "scale(0.97)"
  reduced-motion: "prefers-reduced-motion: reduce"
---

# Mistlamp · 雾灯残页 Design System

## Overview

Mistlamp 是一款哥特暗色调的**文字冒险游戏**（Interactive Fiction），全程 AIGC 辅助开发。通过属性条管理、分支叙事和存档读档系统，玩家在雾灯世界中进行选择和探索。

### 设计隐喻：古旧手稿

- **深褐底色**（`#0c0b09`）模拟陈旧羊皮纸暗部
- **古铜金强调**（`#b8905e`）呼应烛光/雾灯光泽
- **衬线正文**（Noto Serif SC）增强手稿感
- **菜单背景渐变**暗示哥特教堂拱顶光线

### 设计原则

- **沉浸叙事**：最小化 UI 干扰，让文字成为主角
- **触觉反馈**：按钮 active 缩放（0.97），模拟物理按压
- **暗色保护**：深色背景减少长时间阅读疲劳
- **移动友好**：所有交互元素 ≥ 48px，支持安全区域适配

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#0c0b09` | 深褐画布底色 |
| Canvas2 | `#161412` | 次级背景 |
| Surface | `#1a1816` | 卡片/按钮背景 |
| Text | `#d8cfc0` | 正文暖米色 |
| Muted | `#7a7060` | 辅助文字、副标题 |
| Accent | `#b8905e` | 古铜金强调色 |
| Accent2 | `#d4a868` | 悬停/渐变亮金 |
| Danger | `#9e7a7a` | 负面属性/警示 |
| Success | `#7a9e7e` | 正面属性/增益 |

## Typography

| 层级 | 字体 | 规格 | 用途 |
|---|---|---|---|
| Menu Title | Noto Serif SC | 2-3.2rem / 700 / 0.15em | 主菜单标题（金色发光） |
| Subtitle | Noto Sans SC | 0.65-0.85rem / 500 / 0.4em | 英文副标题（大写） |
| Narrative | Noto Serif SC | 16px / 1.8 | 叙事正文 |
| UI Element | Noto Sans SC | 0.72-0.88rem / 500 | 按钮、标签、属性 |

## Components

| 组件 | 规格 |
|---|---|
| Menu Overlay | 全屏垂直居中，径向渐变背景，3 个入口按钮 |
| Menu Button | 高度 ≥48px，圆角 10px，card-bg，hover 金色边框+文字 |
| Primary Button | 渐变金背景（accent→#8a6838），白色文字 |
| Game Header | sticky 定位，底部分割线，标题+副标题+保存按钮 |
| Stats Bar | flex-wrap 属性面板，图标+数值 |
| Narrative Block | 衬线正文 1.8 行高 |
| Choice Button | 全宽按钮，≥48px，hover 金色 |
| Footer Menu | 底部固定，保存/读档/设置 |

## Layout

| 规则 | 值 |
|---|---|
| 游戏容器最大宽度 | 680px |
| 菜单按钮最大宽度 | 280px |
| 最小触控区域 | 48px |
| 安全区域 | env(safe-area-inset-*) |

## Page Structure

```
主菜单（Menu Overlay）
├── 标题 "雾灯残页" + 英文副标题
├── 斜体 tagline
├── [新游戏] Primary Button
├── [继续游戏] Secondary Button
├── [存档管理] Secondary Button
└── 页脚版权

游戏界面（Game）
├── Header（sticky）
│   ├── 游戏标题
│   ├── 副标题/章节名
│   └── [保存] 按钮
├── Stats Bar（属性栏）
│   ├── 属性1（图标+数值）
│   ├── 属性2
│   └── ...
├── Narrative（叙事文本）
│   └── 衬线正文段落
└── Choices（分支选择）
    ├── 选项1
    ├── 选项2
    └── ...

底部菜单
├── [保存] [读档] [设置]
```

## Motion

| 动效 | 规格 |
|---|---|
| 按钮悬停 | 0.2s ease，金色边框+文字 |
| 按钮按下 | scale(0.97) |
| 页面切换 | 直接替换（无转场，保持沉浸） |
| 属性变化 | 即时更新（无动画，避免干扰阅读） |
