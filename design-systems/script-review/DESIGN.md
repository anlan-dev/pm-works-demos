---
version: "2.0"
name: "剧本·进度复盘"
description: "消费娱乐类剧本分析工具，剧场红（#e74c3c）+白卡片，Inter+JetBrains Mono 字体，热力图+词云+场景卡片。"
product-type: 消费娱乐类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#e74c3c"
  primary-soft: "rgba(231,76,60,0.08)"
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
  heatmap:
    cell-radius: 4px
    color-scale: "white → {colors.primary}"
  button-primary:
    backgroundColor: "{colors.primary}"
    height: 44px
responsive:
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# 剧本·进度复盘 Design System

## Overview

剧本复盘是一款面向**编剧/内容创作者**的剧本分析工具。核心功能：拖拽导入 → AI 场景拆分 → diff 对比改稿 → 热力图复盘。

### 设计原则

- **剧场感**：剧场红主色，营造创作氛围
- **数据可视化**：热力图+词云，直观呈现剧本结构
- **AI 辅助**：AI 拆分+改稿建议，减少手动工作

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片 |
| Primary | `#e74c3c` | 剧场红品牌色 |
| Primary Soft | `rgba(231,76,60,0.08)` | 选中态背景 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Heatmap Cell | 圆角 4px，颜色从白到剧场红 |
| Scene Card | 左侧色条+标题+摘要+AI标签 |
| Diff View | 绿色新增/红色删除，等宽字体 |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 单列，Tab 切换（导入/场景/改稿/热力图） |
| Tablet | 双面板 |
| Desktop | 三面板完整布局 |
