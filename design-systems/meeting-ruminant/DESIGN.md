---
version: "2.0"
name: "会议·反刍舱"
description: "工具效率类会议复盘 PWA，白卡片+浅灰画布，Inter 字体，录音转写+待办提取+周报复盘。"
product-type: 工具效率类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#0071e3"
  primary-hover: "#0077ed"
  primary-soft: "rgba(0,113,227,0.08)"
  success: "#34c759"
  warning: "#ff9500"
  danger: "#ff3b30"
  text-primary: "#1d1d1f"
  text-muted: "#6e6e73"
  hairline: "rgba(0,0,0,0.04)"
  shadow: "0 2px 8px rgba(0,0,0,.06)"
  shadow-hover: "0 4px 12px rgba(0,0,0,.1)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  mono-family: "'JetBrains Mono', monospace"
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
    padding: 16-24px
    boxShadow: "{colors.shadow}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    height: 44px
  input-field:
    height: 44px
    rounded: "{rounded.sm}"
  tab-bar:
    height: 40px
    activeColor: "{colors.primary}"
  compliance-disclaimer:
    position: "fixed; bottom: 0"
    backgroundColor: "rgba(255,255,255,0.96)"
    backdropFilter: "blur(12px)"
responsive:
  breakpoints:
    mobile: 360px
    tablet: 768px
    desktop: 1024px
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# 会议·反刍舱 Design System

## Overview

会议反刍舱是一款面向**职场白领**的会议复盘工具。核心功能：录音转写 → 待办提取 → 周报复盘。支持 Web Speech API 本地转写，数据存储在 IndexedDB/localStorage。

### 设计原则

- **工具效率**：一键录音，自动转写，减少手动操作
- **信息密度**：待办按优先级分组，周报按日期聚合（Miller 7±2）
- **隐私优先**：录音本地处理，合规声明模块

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片/面板 |
| Primary | `#0071e3` | 录音按钮/强调 |
| Success | `#34c759` | 待办完成 |
| Warning | `#ff9500` | 待办优先级高 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Record Button | 64px 圆形，居中置底（Fitts 定律） |
| Todo Item | 左侧色点标记优先级，支持拖拽排序 |
| Tab Bar | 底部胶囊式，高度 40px |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 单列，录音按钮居中 |
| Tablet | 双面板（录音+待办） |
| Desktop | 三面板（录音+待办+周报） |
