---
version: "2.0"
name: "住值·租房决策"
description: "工具效率类租房计算器，白卡片+浅灰画布，Inter 字体，财务绿（#10b981）+双轴图表+滑块输入。"
product-type: 工具效率类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#10b981"
  primary-soft: "rgba(16,185,129,0.08)"
  danger: "#ff3b30"
  warning: "#ff9500"
  text-primary: "#1d1d1f"
  text-muted: "#6e6e73"
  hairline: "rgba(0,0,0,0.04)"
  shadow: "0 2px 8px rgba(0,0,0,.06)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
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
  slider:
    track-height: 4px
    thumb-size: 24px
    accent-color: "{colors.primary}"
  data-card:
    large-number: "24px/700"
    label: "12px/500"
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

# 住值·租房决策 Design System

## Overview

住值是一款面向**租房决策者**的计算器。输入收入/支出/偏好 → 实时计算生命成本 → 多方案对比 → AI 租房顾问建议。

### 设计原则

- **数据驱动**：双轴图表（净收益+租收比），大数字统计卡
- **即时反馈**：滑块输入实时更新结果（<100ms）
- **财务绿**：#10b981 主色，传递财务健康/正向收益

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片 |
| Primary | `#10b981` | 财务绿/正向数据 |
| Danger | `#ff3b30` | 负向数据 |
| Warning | `#ff9500` | 注意 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Slider | 轨道 4px，滑块 24px，品牌色 |
| Data Card | 大数字 24px/700 + 标签 12px/500 |
| Chart | 双轴（净收益+租收比），品牌色渐变 |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 单列，滑块全宽 |
| Tablet | 双列（输入+结果） |
| Desktop | 三列（输入+结果+AI建议） |
