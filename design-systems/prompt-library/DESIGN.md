---
version: "2.0"
name: "Prompt Library"
description: "工具效率类 PM Prompt 模板库，白卡片+浅灰画布，Inter+JetBrains Mono 字体，搜索+收藏+使用统计。"
product-type: 工具效率类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#0071e3"
  accent-purple: "#8b5cf6"
  accent-green: "#10b981"
  text-primary: "#1d1d1f"
  text-muted: "#6e6e73"
  hairline: "rgba(0,0,0,0.04)"
  shadow: "0 2px 8px rgba(0,0,0,.06)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  mono-family: "'JetBrains Mono', monospace"
rounded:
  sm: 8px
  md: 12px
  lg: 16px
spacing:
  unit: 4px
components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    boxShadow: "{colors.shadow}"
  code-block:
    backgroundColor: "{colors.canvas}"
    fontFamily: "JetBrains Mono"
    rounded: "{rounded.sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    height: 44px
  search-bar:
    height: 44px
    rounded: "{rounded.sm}"
responsive:
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# Prompt Library Design System

## Overview

Prompt Library 是一款面向**产品经理/AI 从业者**的标准化 Prompt 模板库。搜索+分类筛选→卡片列表→一键复制。localStorage 持久化收藏和使用统计。

### 设计原则

- **工具效率**：搜索置顶，分类横标签，一键复制（Jakob 定律）
- **代码感**：JetBrains Mono 代码块，紫色/绿色语法高亮
- **数据驱动**：使用统计+收藏数，排序热门 Prompt

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片 |
| Primary | `#0071e3` | 主操作 |
| Accent Purple | `#8b5cf6` | Prompt 标签 |
| Accent Green | `#10b981` | 代码高亮 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Code Block | JetBrains Mono，背景 #f5f5f7，圆角 8px |
| Search Bar | 高度 44px，圆角 8px |
| Category Tag | 胶囊形，紫色/绿色/蓝色 |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 单列卡片列表 |
| Tablet | 双列网格 |
| Desktop | 三列网格 |
