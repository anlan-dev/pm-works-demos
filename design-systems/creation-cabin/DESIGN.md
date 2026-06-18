---
version: "2.0"
name: "星途·创作舱"
description: "消费娱乐类创作管理平台，品牌渐变（#667eea→#764ba2）+白卡片，Inter+Display 字体，4 套主题。"
product-type: 消费娱乐类
last-updated: 2026-06-19
colors:
  canvas: "#f5f5f7"
  surface: "#ffffff"
  primary: "#667eea"
  primary-gradient: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
  text-primary: "#1d1d1f"
  text-muted: "#6e6e73"
  hairline: "rgba(0,0,0,0.04)"
  shadow: "0 2px 8px rgba(0,0,0,.06)"
  shadow-hover: "0 4px 12px rgba(0,0,0,.1)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  display-family: "'Noto Serif SC', serif"
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
  sidebar:
    backgroundColor: "{colors.surface}"
    width: 240px
  button-primary:
    backgroundColor: "{colors.primary}"
    height: 44px
responsive:
  breakpoints:
    mobile: 360px
    tablet: 768px
    desktop: 1024px
  touch-target-min: 44px
  viewport: "width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover"
motion:
  micro: "200ms ease-out"
  elastic: "cubic-bezier(.34,1.56,.64,1)"
  reduced-motion: "prefers-reduced-motion: reduce → disable all animations"
---

# 星途·创作舱 Design System

## Overview

创作舱是一款面向**连载/兼职作者**的创作管理平台。三栏工作台布局（侧边栏+章节列表+写作区），支持 4 套主题切换，AI 灵感辅助。

### 设计原则

- **沉浸式**：写作区最大化，工具栏边缘化（Fitts 定律）
- **品牌感**：渐变主色体现创作的想象力与活力
- **多主题**：浅灰/深色/薄荷/墨水屏，适配不同创作场景

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f7` | 页面背景 |
| Surface | `#ffffff` | 卡片/侧边栏 |
| Primary | `#667eea` | 品牌色 |
| Primary Gradient | `#667eea→#764ba2` | Hero/CTA |

## Components

| 组件 | 规格 |
|------|------|
| Sidebar | 宽度 240px，白色背景，圆角 0 |
| Card | 圆角 12px，阴影 0 2px 8px rgba(0,0,0,.06) |
| Editor | 全屏写作区，字号 16px，行高 1.8 |
| AI Panel | 右侧面板，渐变边框 |

## Responsive

| 断点 | 布局 |
|------|------|
| Mobile | 底部 Tab 切换（章节/写作/AI） |
| Tablet | 双栏（侧边栏隐藏，汉堡菜单） |
| Desktop | 三栏完整布局 |
