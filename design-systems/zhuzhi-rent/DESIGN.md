---
version: alpha
name: 住值·租房决策
description: A neumorphic rental decision calculator with dual-axis chart visualization, algorithm-driven cost breakdown, and AI-powered recommendations. The system balances warm cream surfaces with data-rich panels for complex financial comparisons.
colors:
  primary: "#5a6a7a"
  primary-hover: "#4a5a6a"
  success: "#2b7a4b"
  warning: "#c09040"
  danger: "#c04040"
  ink: "#2d3436"
  body: "#4a4a4a"
  muted: "#7f8c8d"
  canvas: "#f0f0f3"
  surface: "#ffffff"
  shadow-dark: "rgba(0, 0, 0, 0.1)"
  shadow-light: "rgba(255, 255, 255, 0.7)"
typography:
  display-lg:
    fontFamily: "'Noto Sans SC', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
  title:
    fontFamily: "'Noto Sans SC', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "'Noto Sans SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
  mono:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: 8px
  md: 12px
  lg: 16px
  pill: 9999px
components:
  card-neumorphic:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: 20px
    boxShadow: "8px 8px 16px {colors.shadow-dark}, -8px -8px 16px {colors.shadow-light}"
  input-slider:
    backgroundColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    height: 8px
  chart-dual-axis:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 16px
  result-card-positive:
    backgroundColor: "#e8f5e9"
    textColor: "{colors.success}"
    rounded: "{rounded.md}"
    padding: 16px
  result-card-negative:
    backgroundColor: "#ffebee"
    textColor: "{colors.danger}"
    rounded: "{rounded.md}"
    padding: 16px
---
## Overview
住值·租房决策 is a neumorphic rental cost calculator. The design emphasizes **data clarity** and **algorithm transparency** — users input parameters and immediately see how rent affects their net income through dual-axis charts.

**Key Characteristics:**
- Neumorphic card system (matching pet-vaccine)
- Dual-axis chart (net income + rent ratio)
- Slider-based input for intuitive parameter adjustment
- Color-coded results (green = positive, red = negative)
- AI recommendation panel with personalized advice
- Responsive layout for mobile-first usage
## Colors
- Primary: #5a6a7a (muted blue-gray)
- Success: #2b7a4b (positive net income)
- Danger: #c04040 (negative net income)
- Warning: #c09040 (approaching threshold)
## Layout
- Single column mobile layout
- Parameter inputs at top
- Chart visualization in middle
- Results and AI recommendations at bottom
## Agent Prompt Guide
```
请按照 DESIGN.md 的新拟物风格构建租房计算器：
- 使用新拟物卡片（双向阴影）
- 滑块输入，实时更新图表
- 双轴图表：净收益（左轴）+ 租收比（右轴）
- 结果用绿色（正）/红色（负）标注
```
