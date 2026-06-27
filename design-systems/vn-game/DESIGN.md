---
version: "2.0"
name: "雾灯残页 · AIGC 游戏开发展示页"
description: "消费娱乐类 AIGC 能力展示页，哥特暗色叙事风（#0f0e0c 画布）+古铜金强调（#c49a6c），Noto Serif SC 衬线正文 + Inter UI，支持 dark/ink/default 三主题切换，展示 AIGC 全流程协作成果。"
product-type: 消费娱乐类
last-updated: 2026-06-27
colors:
  canvas: "#0f0e0c"
  text-primary: "#e8ddd0"
  text-muted: "#8a7e72"
  accent: "#c49a6c"
  accent-soft: "rgba(196,154,108,0.12)"
  surface: "#1a1816"
  border: "rgba(196,154,108,0.1)"
  shadow: "0 4px 16px rgba(0,0,0,.4)"
  shadow-hover: "0 8px 24px rgba(0,0,0,.5)"
  shadow-inset: "inset variant"
  danger: "#a04040"
  btn-radius: 8px
  card-radius: 12px
  # dark theme
  dark-canvas: "#0a0908"
  dark-text: "#e0d5c8"
  dark-accent: "#b8905e"
  dark-surface: "#151311"
  # ink theme（羊皮纸浅色）
  ink-canvas: "#f5f0e8"
  ink-text: "#2f2418"
  ink-muted: "#5f4b34"
  ink-accent: "#7d5b2a"
  ink-surface: "#ead9bc"
  ink-border: "rgba(125,91,42,0.15)"
  ink-shadow: "0 2px 8px rgba(0,0,0,.08)"
typography:
  font-body: "'Noto Serif SC', Georgia, serif"
  font-ui: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  hero-title:
    fontSize: "clamp(1.3rem, 2.5vw, 1.8rem)"
    fontWeight: 700
    fontFamily: font-body
    color: accent
  section-title:
    fontSize: "clamp(1rem, 1.4vw, 1.2rem)"
    fontWeight: 600
    fontFamily: font-body
    borderLeft: "3px solid accent"
    paddingLeft: 12px
  stat-num:
    fontSize: "clamp(1.4rem, 2.5vw, 2rem)"
    fontWeight: 700
    color: accent
  body:
    fontSize: "clamp(0.78rem, 0.95vw, 0.88rem)"
    lineHeight: 1.7
rounded:
  btn: 8px
  card: 12px
spacing:
  container-max: 760px
components:
  hero:
    textAlign: center
    backgroundColor: surface
    border: "1px solid border"
    rounded: card-radius
    boxShadow: shadow
    padding: "clamp(20px, 3vw, 30px)"
  stats-grid:
    display: grid
    gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))"
    gap: "clamp(8px, 1.5vw, 14px)"
  stat-card:
    backgroundColor: surface
    border: "1px solid border"
    rounded: card-radius
    boxShadow: shadow
    textAlign: center
    hover: "shadow-hover + translateY(-2px)"
  story-block:
    backgroundColor: surface
    border: "1px solid border"
    rounded: card-radius
    boxShadow: shadow
    padding: "clamp(16px, 2.5vw, 24px)"
    hover: "shadow-hover + accent border"
  details-summary:
    cursor: pointer
    backgroundColor: surface
    border: "1px solid border"
    rounded: btn-radius
    boxShadow: shadow
    padding: "clamp(8px, 1.5vw, 12px) clamp(12px, 2vw, 16px)"
    hover: shadow-hover
  quote-block:
    backgroundColor: surface
    border: "1px solid border"
    borderRadius: "clamp(14px, 2vw, 18px)"
    fontStyle: italic
    lineHeight: 1.8
    decoration: "accent 引号"
  file-link:
    display: inline-flex
    alignItems: center
    gap: 6px
    padding: "8px 14px"
    rounded: btn-radius
    backgroundColor: surface
    border: "1px solid border"
    hover: "shadow-hover + scale(0.98)"
responsive:
  touch-target-min: 44px
  container-max: 760px
  breakpoints:
    mobile: "< 640px — 单列 Stats Grid"
    desktop: "> 640px — 自适应 Stats Grid"
motion:
  micro: "0.2s ease"
  card-hover: "0.2s ease, shadow-hover + translateY(-2px)"
  reduced-motion: "prefers-reduced-motion: reduce"
---

# 雾灯残页 · AIGC 游戏开发展示页 Design System

## Overview

此页面（vn-game.html）是《雾灯残页》文字冒险游戏的 **AIGC 能力展示页**，面向 PM/技术面试官，展示全程 AIGC 辅助开发的协作成果。区别于 mistlamp.html（可玩游戏本体），此页面侧重于过程和成果的呈现。

### 设计原则

- **叙事一致**：与 mistlamp.html 共享哥特暗色调色彩体系，保持项目视觉统一
- **过程透明**：通过 stat-card 展示 AIGC 协作数据（生成字数/Agent调用/IP资源），建立可信度
- **三主题适配**：default（暗色）/ dark（更深）/ ink（羊皮纸浅色）满足不同场景
- **文件溯源**：直接链接到生成的文件（script.rpy, story_text.txt 等），提供可验证的证据链

## Colors

| Token | Default | Dark | Ink | Usage |
|---|---|---|---|---|
| Canvas | `#0f0e0c` | `#0a0908` | `#f5f0e8` | 画布底色 |
| Text | `#e8ddd0` | `#e0d5c8` | `#2f2418` | 正文 |
| Muted | `#8a7e72` | `#7a6e62` | `#5f4b34` | 辅助文字 |
| Accent | `#c49a6c` | `#b8905e` | `#7d5b2a` | 古铜金/深棕强调 |
| Surface | `#1a1816` | `#151311` | `#ead9bc` | 卡片背景 |

## Typography

| 层级 | 字体 | 规格 | 用途 |
|---|---|---|---|
| Hero Title | Noto Serif SC | 1.3-1.8rem / 700 | 页面标题 |
| Section Title | Noto Serif SC | 1-1.2rem / 600 + 金色左边框 | 区块标题 |
| Stat Number | Noto Serif SC | 1.4-2rem / 700 / accent | 数据大数字 |
| Body | Noto Sans SC | 0.78-0.88rem / 1.7 | 正文段落 |
| Quote | Noto Serif SC | 0.78-0.85rem / 1.8 / italic | 引用块（金色引号装饰） |

## Components

| 组件 | 规格 |
|---|---|
| Hero | 居中卡片，标题+tagline+副标题，card-bg + card-radius + shadow |
| Stats Grid | 自适应网格（min 140px），统计卡片 |
| Stat Card | 居中数字+标签，hover 上浮 2px |
| Story Block | 卡片式段落，hover 金色边框 |
| Details Panel | 折叠面板，disclosure-closed 标记 |
| Quote Block | 斜体引用块，::before/::after 金色引号装饰 |
| Section Title | 金色 3px 左边框 + 6px padding-left |
| File Links | 内联 flex 按钮，hover shadow-hover |

## Layout

| 规则 | 值 |
|---|---|
| 容器最大宽度 | 760px |
| Stats Grid | auto-fit, min 140px |
| 卡片内边距 | clamp(16px, 2.5vw, 24px) |

## Page Structure

```
Hero
├── 标题 "雾灯残页"
├── tagline
├── subtitle（AIGC 开发说明）
└── back link

Stats Grid
├── 生成文字量（万字）
├── AI Agent 调用次数
├── 原创 IP 资源数
├── 分支结局数

Section: 核心 AIGC 应用场景
├── Story Block: 世界观生成
├── Story Block: 角色创作
├── Story Block: 分支叙事设计
├── Story Block: 文本润色与风格统一
├── Story Block: Visual Novel 脚本导出
└── Story Block: 多语言翻译

Section: AI Agent 协作模式
├── Details: Agent 1 — 世界观构建
├── Details: Agent 2 — 角色设计
├── Details: Agent 3 — 对话生成
└── Details: Agent 4 — 品质审查

Section: 开发指标
├── 投入产出比分析
└── 人类vs AI 工作占比

Section: 生成文件
├── file-link: script.rpy
├── file-link: story_text.txt
├── file-link: story_overview.md
├── file-link: worldbuilding.md
└── file-link: character_profiles.md

Section: 技术架构
├── AI 模型选择理由
├── Prompt Engineering 示例
└── Quality Control 机制
```

## Themes

| Theme | CSS Selector | 特征 |
|---|---|---|
| Default | `body` | 深褐底 + 暖米文字 + 古铜金强调 |
| Dark | `body[data-theme="dark"]` | 更深底色，降低亮度 |
| Ink | `body[data-theme="ink"]` | 羊皮纸浅色 + 深棕文字 + 棕色强调 |

## Motion

| 动效 | 规格 |
|---|---|
| 卡片悬停 | 0.2s ease，shadow-hover + translateY(-2px) |
| 文件链接悬停 | shadow-hover + scale(0.98) |
| Details 展开 | 原生浏览器行为 |
