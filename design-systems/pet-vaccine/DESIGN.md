---
version: "2.0"
name: "宠伴·健康台账"
description: "工具效率类宠物健康管理 PWA，白卡片+浅灰画布，Inter 字体，本地 OCR 识别，隐私优先架构。"
product-type: 工具效率类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#0071e3"
  primary-hover: "#0077ed"
  primary-soft: "rgba(0,113,227,0.08)"
  success: "#34c759"
  success-soft: "rgba(52,199,89,0.08)"
  warning: "#ff9500"
  warning-soft: "rgba(255,149,0,0.08)"
  danger: "#ff3b30"
  danger-soft: "rgba(255,59,48,0.08)"
  text-primary: "#1d1d1f"
  text-secondary: "#424245"
  text-muted: "#6e6e73"
  hairline: "rgba(0,0,0,0.04)"
  shadow: "0 2px 8px rgba(0,0,0,.06)"
  shadow-hover: "0 4px 12px rgba(0,0,0,.1)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  mono-family: "'JetBrains Mono', monospace"
  display-lg:
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  display-md:
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  title:
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
  body-lg:
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
  button:
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
rounded:
  sm: 8px
  md: 12px
  lg: 16px
  pill: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  xxxl: 48px
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: 16-24px
    boxShadow: "{colors.shadow}"
  card-hover:
    boxShadow: "{colors.shadow-hover}"
    transform: "translateY(-1px)"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    height: 44px
    padding: 10px 24px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  tab-bar:
    backgroundColor: "rgba(255,255,255,0.9)"
    activeColor: "{colors.primary}"
    activeBackground: "{colors.primary-soft}"
    height: 40px
  pill-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.pill}"
    height: 28px
    padding: 4px 12px
  compliance-disclaimer:
    position: "fixed; bottom: 0"
    backgroundColor: "rgba(255,255,255,0.96)"
    backdropFilter: "blur(12px)"
    maxHeight: "60vh"
    triggerHeight: "44px"
responsive:
  breakpoints:
    mobile: 360px
    mobile-lg: 412px
    tablet: 768px
    desktop: 1024px
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  page-transition: "300ms ease-out"
  stagger: "+50ms"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
accessibility:
  contrast-min: "4.5:1 (body text)"
  contrast-large: "3:1 (large text, 18px+)"
  focus-visible: "2px solid {colors.primary}"
  keyboard-nav: "Tab traversal, Enter submit, Esc close modal"
---

# 宠伴·健康台账 Design System

## Overview

宠伴是一款面向**多宠家庭**的健康管理 PWA。核心理念是"隐私优先、本地存储、零服务器依赖"。使用 Tesseract.js 在浏览器端完成 OCR 识别，所有数据存储在 localStorage。

### 设计原则

- **工具效率**：信息密度适中，操作路径最短，视觉不抢功能
- **隐私优先**：隐私 Consent 拦截 + 本地存储声明 + 合规声明模块
- **数据驱动**：疫苗完成率、花费趋势、AI 健康摘要卡片
- **渐进披露**：可折叠介绍区，默认展示主应用，减少认知负荷

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片/面板背景 |
| Primary | `#0071e3` | 主操作/强调 |
| Success | `#34c759` | 疫苗完成/正向数据 |
| Warning | `#ff9500` | 驱虫提醒/注意 |
| Danger | `#ff3b30` | 过期/删除操作 |
| Text Primary | `#1d1d1f` | 标题、正文 |
| Text Muted | `#6e6e73` | 辅助说明 |

## Components

| 组件 | 规格 |
|------|------|
| Card | 圆角 12px，padding 16-24px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Button | 高度 44px，圆角 8px，padding 10px 24px |
| Input | 高度 44px，圆角 8px，padding 12px 16px |
| Tab Bar | 底部胶囊式，高度 40px，当前项蓝色+底部指示条 |
| Pill Badge | 圆角 9999px，高度 28px |
| Compliance Disclaimer | 固定底部，毛玻璃背景，可展开收起 |

## Responsive

| 断点 | 宽度 | 布局 |
|------|------|------|
| Mobile | 360-412px | 单列，底部 Tab 导航 |
| Tablet | 768-1024px | 双列卡片网格 |
| Desktop | 1024px+ | 三列卡片网格 |

## Motion

| 场景 | 时长 | 缓动 |
|------|------|------|
| 微交互 | 200ms | ease-out |
| 页面切换 | 300ms | ease-out |
| 列表错开 | +50ms | stagger |
| Reduced Motion | 禁用所有非必要动画 | - |
