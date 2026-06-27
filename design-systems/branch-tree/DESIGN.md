---
version: "2.0"
name: "Branch Tree · 《雾灯残页》游戏结构示意图"
description: "数据可视化类游戏叙事分支图，羊皮纸手稿风格（#120f0c 底+ #ead9bc 卡片），Georgia 衬线字体 + 仿古做旧质感，展示游戏世界观/角色/分支/结局全貌。"
product-type: 数据可视化类
last-updated: 2026-06-27
colors:
  canvas: "#120f0c"
  frame: "#2b2016"
  paper: "#ead9bc"
  paper-edge: "#c3a87d"
  ink: "#2f2418"
  ink-soft: "#5f4b34"
  axis-fate: "#7d5b2a"
  axis-self: "#5e3e68"
  axis-unknown: "#2f5b70"
  chip: "#f2e5cd"
typography:
  family: "'Georgia', 'Times New Roman', 'Microsoft YaHei', serif"
  title:
    fontSize: "clamp(28px, 3.2vw, 40px)"
    fontWeight: 700
    letterSpacing: 1px
  card-title:
    fontSize: "clamp(15px, 1.8vw, 17px)"
    color: ink-soft
    borderBottom: "1px solid rgba(111,80,44,0.28)"
  card-body:
    fontSize: "clamp(13px, 1.1vw, 14px)"
    lineHeight: 1.68
  chip-label:
    fontSize: 12px
    lineHeight: 1.3
rounded:
  card: 12px
  chip: 999px
  board: 14px
spacing:
  container-max: "min(1320px, 96vw)"
  card-padding: "clamp(14px, 1.6vw, 18px)"
  board-padding: "clamp(14px, 2vw, 22px)"
  gap: "clamp(14px, 2vw, 24px)"
components:
  board:
    border: "1px solid rgba(195,168,125,0.42)"
    rounded: 14px
    background: "rgba(43,32,22,0.84)"
    boxShadow: "0 12px 28px rgba(0,0,0,0.34)"
  card:
    background: "radial-gradient(ellipse at 50% 0%, rgba(255,240,210,0.6) 0%, transparent 60%), linear-gradient(180deg, #f5e9d4, paper)"
    backgroundColor: paper
    color: ink
    border: "1px solid paper-edge"
    rounded: 12px
    boxShadow: "inset 0 1px 0 rgba(255,255,255,0.55), 0 4px 10px rgba(0,0,0,0.2)"
    padding: card-padding
  legend:
    border: "1px solid rgba(195,168,125,0.45)"
    rounded: 12px
    background: "rgba(43,32,22,0.76)"
    display: grid
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))"
  chip:
    backgroundColor: chip
    color: ink
    border: "1px solid rgba(110,83,49,0.3)"
    rounded: 999px
    fontSize: 12px
    padding: "4px 10px"
  timeline:
    display: grid
    gap: 10px
  lens-preview:
    display: grid
    gap: 8px
  ending-card:
    display: grid
    gap: 10px
responsive:
  touch-target-min: 44px
  layout: "mobile-first 单列, desktop 多列 grid"
  breakpoints:
    mobile: "< 640px — 全单列，Timeline JS accordion"
    tablet: "640-1024px — 双列"
    desktop: "> 1024px — Timeline 4列，Row 2列"
motion:
  reduced-motion: "prefers-reduced-motion: reduce"
---

# Branch Tree · 游戏结构示意图 Design System

## Overview

Branch Tree（branch_tree.html）是《雾灯残页》文字冒险游戏的**结构可视化页面**，用羊皮纸手稿风格展示游戏的完整叙事架构：世界观、角色关系、分支轴线、章节 Timeline 和结局谱系。

### 设计隐喻：考古学家的手稿板

- **深色底**（`#120f0c`）模拟黑绒布展示台
- **羊皮纸卡片**（`#ead9bc` + 做旧渐变）复刻古文献质感
- **药丸标签**（chip）如同分类标签贴在展板上
- **三条轴线**：命运轴（#7d5b2a）、自我轴（#5e3e68）、未知轴（#2f5b70）

### 设计原则

- **信息考古**：用"展板+卡片+标签"的三层结构呈现复杂游戏系统
- **可扫描性**：Legend 图例先行，Chip 快速标记，Card 深入细节
- **移动友好**：mobile-first 单列，Timeline 用 JS accordion 折叠
- **古文献质感**：渐变+内阴影+边框模拟羊皮纸叠放效果

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#120f0c` | 深褐展示台底色 + 径向渐变光晕 |
| Frame | `#2b2016` | Legend 面板背景 |
| Paper | `#ead9bc` | 卡片羊皮纸底色 |
| Paper Edge | `#c3a87d` | 卡片边框色 |
| Ink | `#2f2418` | 卡片内文字色 |
| Ink Soft | `#5f4b34` | 卡片标题色 |
| Axis Fate | `#7d5b2a` | 命运轴 - 棕色 |
| Axis Self | `#5e3e68` | 自我轴 - 紫色 |
| Axis Unknown | `#2f5b70` | 未知轴 - 蓝色 |
| Chip | `#f2e5cd` | 标签底色 |

## Typography

| 层级 | 字体 | 规格 | 用途 |
|---|---|---|---|
| Title | Georgia / Times New Roman | 28-40px / 700 | 页面主标题 |
| Card Title | Georgia | 15-17px | 卡片三级标题（底部边框） |
| Card Body | Georgia / Microsoft YaHei | 13-14px / 1.68 | 卡片内容 |
| Chip Label | Georgia | 12px / 1.3 | 图例标签 |
| Code | monospace | 0.92em | 代码片段 |

## Components

| 组件 | 规格 |
|---|---|
| Board | 深色展板容器，border + rounded + shadow |
| Card | 羊皮纸卡片：径向渐变+线性渐变双层背景，inset 白边+drop shadow |
| Legend | 图例面板：auto-fit grid，min 200px |
| Chip | 药丸标签（999px 圆角），chip-bg + ink 文字 |
| Timeline | 移动端 accordion，桌面端 4 列 grid |
| Lens Preview | 预览网格，视点卡片 |
| Ending Card | 结局卡片（接入条件+描述+达成率） |
| Axis Chart | 三条轴线可视化（命运/自我/未知） |

## Layout

| 规则 | 值 |
|---|---|
| 容器最大宽度 | min(1320px, 96vw) |
| 卡片内边距 | clamp(14px, 1.6vw, 18px) |
| 间距 | clamp(14px, 2vw, 24px) |

### 响应式策略

```
Mobile (< 640px):
  Layout: 1fr（全单列）
  Row: 1fr
  Lens Preview: 1fr
  Ending Grid: 1fr
  Timeline: JS accordion（点击展开）

Tablet (640-1024px):
  Row: 2fr
  Lens Preview: 2fr
  
Desktop (> 1024px):
  Row: 2fr
  Row-2: 2fr
  Timeline: 4 列 grid
  Lens Preview: 3fr
  Ending Grid: 2fr
```

## Page Structure

```
Title
├── h1: 《雾灯残页》游戏结构
└── p: 副标题

Legend（图例）
├── Chip: 核心概念标签
├── Chip: 三条轴线说明
└── Chip: 结局类型

Board（主展板）
├── 世界观（Worldview）
│   ├── Card: 世界背景
│   ├── Card: 核心设定
│   └── Card: 规则系统
├── 角色关系（Characters）
│   ├── Card: 主角
│   ├── Card: 关键NPC
│   └── Card: 关系图
├── 三条轴线
│   ├── 命运轴（Fate）
│   ├── 自我轴（Self）
│   └── 未知轴（Unknown）
├── Timeline
│   ├── Card: 章节 1
│   ├── Card: 章节 2
│   └── ...
├── 视点系统（Lens Preview）
│   ├── Card: 视角 1
│   └── Card: 视角 2
└── 结局谱系（Endings）
    ├── Card: 结局 A
    ├── Card: 结局 B
    └── ...
```

## Motion

| 动效 | 规格 |
|---|---|
| 无主动画 | 静态展示页，不使用动效 |
| Accordion | 原生 details/summary 行为 |
| 响应式切换 | CSS Grid 断点切换 |
