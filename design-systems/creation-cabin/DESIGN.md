---
version: "1.0"
name: "星途·创作舱"
description: "沉浸式网文/剧本写作工作台，多主题系统，角色管理+大纲+多格式导出一体化创作桌面。"
colors:
  canvas: "#e6e6e6"
  surface: "#e6e6e6"
  text-primary: "#3f3f3f"
  text-secondary: "#4a4a4a"
  text-muted: "#6b6b6b"
  accent-blue: "#0071e3"
  tag-bg: "#d8d8d8"
  toast-bg: "rgba(63,63,63,0.9)"
  shadow-light: "rgba(255,255,255,0.66)"
  shadow-dark: "rgba(0,0,0,0.12)"
themes:
  light-gray:
    canvas: "#e6e6e6"
    surface: "#e6e6e6"
    text: "#3f3f3f"
    accent: "#0071e3"
  dark:
    canvas: "#000000"
    surface: "#1c1c1e"
    card: "#2c2c2e"
    text: "#ffffff"
    accent: "#0a84ff"
    text-muted: "#8e8e93"
  mint:
    canvas: "#e3f0ea"
    surface: "#f0f9f4"
    card: "rgba(255,255,255,0.86)"
    text: "#1e3a2f"
    accent: "#6e9b89"
  ink:
    canvas: "#f5f5f5"
    surface: "#ffffff"
    card: "#ffffff"
    text: "#1a1a1a"
    accent: "#333333"
typography:
  family: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', system-ui, sans-serif"
  weight-regular: 400
  weight-medium: 500
  weight-semibold: 600
  weight-bold: 700
  heading-size: "1.1rem"
  body-size: "0.875rem"
  caption-size: "0.75rem"
rounded:
  small: 8px
  medium: 12px
  large: 16px
spacing-unit: 8px
components:
  - workspace-layout
  - sidebar-tree
  - editor-canvas
  - character-card
  - outline-node
  - modal-dialog
  - toast-notification
  - theme-switcher
  - export-panel
---

# 星途·创作舱 Design System

## Overview

创作舱是一款面向**网文/剧本创作者**的沉浸式写作桌面，提供角色设定卡、大纲树、多格式导出（Markdown/PDF/DOCX）等完整功能。产品定位为"创作者的 Photoshop"——把所有创作工具集中在一个界面。

### 设计原则

- **沉浸**：编辑区占据最大面积，侧边栏可折叠
- **组织**：角色、大纲、场景分层管理，树形导航
- **多面**：4 套主题满足不同创作场景（日间/夜间/薄荷/墨水屏）
- **可导出**：所有内容均支持多格式输出

## Colors

### Default — Light Gray

| Token | Value | Usage |
|---|---|---|
| Canvas | `#e6e6e6` | 页面背景 |
| Text Primary | `#3f3f3f` | 标题、正文 |
| Accent Blue | `#0071e3` | 链接、选中态、边框高亮 |
| Tag BG | `#d8d8d8` | 标签背景 |
| Toast BG | `rgba(63,63,63,0.9)` | 消息提示 |

### Dark — 深色模式

| Token | Value | Usage |
|---|---|---|
| Canvas | `#000000` | 页面背景（纯黑） |
| Surface | `#1c1c1e` | 一级容器 |
| Card | `#2c2c2e` | 二级卡片 |
| Text Primary | `#ffffff` | 标题、正文 |
| Accent | `#0a84ff` | 链接、选中态 |
| Text Muted | `#8e8e93` | 辅助信息 |

深色模式遵循 Apple Human Interface Guidelines 的 true black 原则，surface 层级为 `#000 → #1c1c1e → #2c2c2e → #3a3a3c`。

### Mint — 薄荷绿

| Token | Value | Usage |
|---|---|---|
| Canvas | `#e3f0ea` | 页面背景 |
| Surface | `#f0f9f4` | 一级容器 |
| Card | `rgba(255,255,255,0.86)` | 半透明白卡 |
| Text | `#1e3a2f` | 深墨绿文字 |
| Accent | `#6e9b89` | 森林绿强调 |

### Ink — 墨水屏

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f5f5` | 浅灰纸张色 |
| Surface | `#ffffff` | 纯白编辑区 |
| Text | `#1a1a1a` | 近黑文字 |
| Accent | `#333333` | 深灰强调 |

墨水屏主题**无阴影、无渐变**，使用纯边框分割，适配电子墨水设备。

## Typography

- **字体栈**：`SF Pro Text` (macOS) → `PingFang SC` (中文) → `system-ui`
- **编辑区**：`0.875rem`，行高 1.7，适合长文阅读
- **导航**：`0.75rem`，medium weight
- **标题**：`1.1rem`，bold

## Layout

### 三栏工作台

```
┌─────────────────────────────────────────────┐
│ Header (Logo + 标题 + 工具栏)               │
├──────┬────────────────────────┬──────────────┤
│      │                        │              │
│ 侧边栏 │     编辑主区域 (Editor)    │   属性面板    │
│(树形) │                        │  (角色/场景)  │
│      │                        │              │
├──────┴────────────────────────┴──────────────┤
│ 状态栏 (字数/章节/保存状态)                    │
└─────────────────────────────────────────────┘
```

- **侧边栏宽度**：`240px`，可折叠至 `0`
- **属性面板**：`280px`，可隐藏
- **编辑区**：flex-grow 填充剩余空间
- **Header**：sticky 定位，`backdrop-filter: blur(12px)`

## Elevation

### Light/Mint 主题

```css
/* 凸起卡片 */
box-shadow: -8px -8px 16px rgba(255,255,255,0.66),
             8px 8px 16px rgba(0,0,0,0.12);
```

### Dark 主题

```css
/* Apple 风格深色阴影 */
box-shadow: 0 2px 8px rgba(0,0,0,0.4);
border: 1px solid rgba(255,255,255,0.1);
```

### Ink 主题

```css
/* 无阴影，纯边框 */
border: 1px solid #cccccc;
```

## Do's and Don'ts

### Do

- ✅ 编辑区始终占据 60%+ 宽度
- ✅ 侧边栏树支持拖拽排序
- ✅ 角色卡片支持头像+标签+关系线
- ✅ 导出面板提供 Markdown/PDF/DOCX 三选项
- ✅ 主题切换使用 CSS 变量热替换，无需重载

### Don't

- ❌ 不要在编辑区内弹浮层（打断沉浸感）
- ❌ 不要默认展开所有侧边栏
- ❌ 不要限制文件数量（创作者需要自由）
- ❌ 不要在深色模式使用纯白文字（用 `rgba(235,235,245,0.72)`）

## Agent Prompt Guide

> 当你为创作舱生成 UI 代码时：
>
> 1. 使用三栏布局：侧边栏 + 编辑区 + 属性面板
> 2. 支持 4 套主题切换，通过 `body.theme-*` class 和 CSS 变量实现
> 3. 深色模式遵循 Apple HIG true black 原则
> 4. 墨水屏主题禁用所有阴影和渐变
> 5. 编辑区使用 `contenteditable` 或 `textarea`，字体 0.875rem
> 6. 侧边栏使用树形结构，支持展开/折叠
> 7. Toast 通知从底部滑入，3 秒后自动消失
> 8. 所有交互状态（hover/active/focus）必须完整
