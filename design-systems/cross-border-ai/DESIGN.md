---
version: "2.0"
name: "GlobalFUN·跨境AI拼团"
description: "企业服务类跨境电商，深蓝专业（#1e4a6b）+白卡片，Inter 字体，4 Agent 并行+翻转展示+拼团流程。"
product-type: 企业服务类
last-updated: 2026-06-19
colors:
  canvas: "#f8fafc"
  surface: "#ffffff"
  primary: "#1e4a6b"
  accent: "#0071e3"
  success: "#10b981"
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
  agent-card:
    backgroundColor: "{colors.surface}"
    thinking-state: "三点跳动 + 品牌色脉冲"
  button-primary:
    backgroundColor: "{colors.primary}"
    height: 44px
responsive:
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  stagger: "+100ms"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# GlobalFUN·跨境AI拼团 Design System

## Overview

GlobalFUN 是一款面向**跨境购物消费者**的 AI 拼团平台。4 个 AI Agent 并行处理（比价/关税/物流/推荐），翻转卡片展示结果，支持中/英/日三语。

### 设计原则

- **专业信任**：深蓝主色传递企业级可靠性
- **信息密度**：双币价格、关税计算、物流追踪一屏呈现
- **Agent 交互**：思考态用品牌色脉冲，结果用卡片依次滑入（stagger 100ms）

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f8fafc` | 冷白背景 |
| Surface | `#ffffff` | 卡片 |
| Primary | `#1e4a6b` | 深蓝品牌色 |
| Accent | `#0071e3` | 强调/CTA |
| Success | `#10b981` | 价格优势/完成 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Agent Card | 白色卡片+思考态三点跳动+品牌色脉冲 |
| Price Tag | 等宽数字（JetBrains Mono），双币显示 |
| Search Bar | 高度 48px，圆角 12px |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 单列，Agent 纵向排列 |
| Tablet | 双列 Agent 网格 |
| Desktop | 4 列 Agent 并行 |
