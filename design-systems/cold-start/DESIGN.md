---
version: "2.0"
name: "冷启动·行动引擎"
description: "工具效率类行动启动器，白卡片+浅灰画布，Inter 字体，AI 拆解拖延任务为最小行动。"
product-type: 工具效率类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#0071e3"
  success: "#34c759"
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
  pill: 9999px
spacing:
  unit: 4px
components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    boxShadow: "{colors.shadow}"
  button-primary:
    backgroundColor: "{colors.primary}"
    height: 44px
  input-field:
    height: 44px
responsive:
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# 冷启动·行动引擎 Design System

## Overview

冷启动是一款帮助**拖延症用户**启动任务的极简工具。输入拖延任务 → AI 拆解为 3 步最小行动 → 选择执行模式（规则/AI）→ 倒计时执行。

### 设计原则

- **极简**：最少输入，最少选择，最少干扰
- **即时反馈**：倒计时+进度条，实时状态可见
- **Hick 定律**：执行模式仅 2 个选项，减少决策疲劳

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片 |
| Primary | `#0071e3` | 主操作 |
| Success | `#34c759` | 任务完成 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Big CTA | 高度 56px，圆角 16px，字号 18px/600 |
| Timer | 等宽数字（JetBrains Mono），48px |

## Responsive

移动端优先，单列布局，大按钮居中。
