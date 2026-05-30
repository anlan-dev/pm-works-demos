---
version: "1.0"
name: "Prompt Library · Vibe Coding 工作台"
description: "产品经理视角的 Vibe Coding Prompt 库，从 PRD 生成到 UI 批判，搜索+收藏+使用统计，新拟物极简风格。"
colors:
  canvas: "#e6e6e6"
  surface: "#dedede"
  text-primary: "#3f3f3f"
  text-secondary: "#6b6b6b"
  text-muted: "#999999"
  accent: "#5a6a7a"
  accent-green: "#7a8a6a"
  accent-red: "#8a6a6a"
  code-bg: "#f0f0f0"
  code-border: "#d8d8d8"
  shadow-light: "rgba(255,255,255,0.66)"
  shadow-dark: "rgba(0,0,0,0.12)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  mono-family: "'JetBrains Mono', 'Courier New', monospace"
  weight-light: 300
  weight-regular: 400
  weight-medium: 500
  weight-semibold: 600
  weight-bold: 700
  heading-size: "clamp(1.3rem, 3.5vw, 1.8rem)"
  body-size: "0.875rem"
  code-size: "0.82rem"
  caption-size: "0.78rem"
rounded:
  small: 16px
  medium: 28px
  large: 32px
  pill: 40px
spacing-unit: 8px
components:
  - header
  - stats-bar
  - category-nav
  - search-bar
  - prompt-card
  - code-block
  - copy-button
  - favorite-toggle
  - back-link
---

# Prompt Library · Vibe Coding 工作台 Design System

## Overview

Prompt Library 是一个面向**产品经理**的 Vibe Coding Prompt 工具库。收录了从 PRD 生成、用户故事拆解、UI 批判到竞品分析的完整 prompt 链。支持搜索、分类筛选、一键复制、收藏和使用统计。

### 设计原则

- **工具感**：像一个精心整理的工具箱，而非博客
- **可复制**：每个 prompt 一键复制，代码块格式清晰
- **可发现**：搜索 + 分类 + 标签三重过滤
- **新拟物极简**：与 Cold Start 同系列视觉语言

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#e6e6e6` | 页面背景 |
| Surface | `#dedede` | 卡片/输入框 |
| Text Primary | `#3f3f3f` | 标题、正文 |
| Text Secondary | `#6b6b6b` | 说明文字 |
| Text Muted | `#999999` | 辅助信息 |
| Accent Blue-Gray | `#5a6a7a` | 主按钮、链接 |
| Accent Green | `#7a8a6a` | 成功状态 |
| Accent Red | `#8a6a6a` | 收藏高亮 |
| Code BG | `#f0f0f0` | 代码块背景 |
| Code Border | `#d8d8d8` | 代码块边框 |

与 Cold Start 共享同一色板，但增加了代码块专用的 `code-bg` 和 `code-border` 色值。

## Typography

- **主字体**：`Inter` (英文) → `Noto Sans SC` (中文) → `system-ui`
- **代码字体**：`JetBrains Mono` → `Courier New` → `monospace`
- **标题**：`clamp(1.3rem, 3.5vw, 1.8rem)`，700 weight，响应式
- **代码块**：0.82rem，行高 1.7，`white-space: pre-wrap`
- **标签**：0.68rem，凹陷新拟物样式

## Layout

### 单列布局

```
┌─────────────────────────────────────┐
│ 返回链接 ←                           │
│ Header (标题 + 副标题)                │
├─────────────────────────────────────┤
│ Stats Bar (总 Prompt 数 + 分类统计)   │
├─────────────────────────────────────┤
│ Search Bar (新拟物凹陷输入框)         │
├─────────────────────────────────────┤
│ Category Nav (分类标签, 新拟物凸起)   │
├─────────────────────────────────────┤
│ Prompt Card                          │
│ ┌─────────────────────────────────┐ │
│ │ Title + Tags + ❤️ 收藏          │ │
│ │ 使用场景说明                     │ │
│ │ ┌─────────────────────────────┐ │ │
│ │ │ Code Block (可复制)          │ │ │
│ │ │ JetBrains Mono              │ │ │
│ │ │                   [Copy 📋] │ │ │
│ │ └─────────────────────────────┘ │ │
│ └─────────────────────────────────┘ │
│ ...更多卡片...                       │
└─────────────────────────────────────┘
```

- **单列居中**：`max-width: 760px`
- **卡片间距**：16px
- **代码块**：`max-height: 320px`，超出滚动
- **返回链接**：顶部左对齐，accent 色

## Elevation

### 卡片 — 凸起

```css
.nr {
  background: var(--bg);
  border-radius: 28px;
  box-shadow: -8px -8px 16px rgba(255,255,255,0.66),
               8px 8px 16px rgba(0,0,0,0.12);
  padding: 20px;
}
```

### 标签 — 凹陷

```css
.prompt-tag {
  background: var(--bg);
  border-radius: 40px;
  padding: 3px 10px;
  font-size: 0.68rem;
  box-shadow: inset 2px 2px 4px rgba(0,0,0,0.04),
              inset -2px -2px 4px rgba(255,255,255,0.4);
}
```

### 代码块 — 凹陷

```css
.prompt-text {
  background: #f0f0f0;
  border: 1px solid #d8d8d8;
  border-radius: 16px;
  padding: 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.82rem;
  line-height: 1.7;
}
```

## 特殊组件

### 搜索栏

- 新拟物凹陷输入框（`inset shadow`）
- `placeholder: "搜索 Prompt..."`
- 实时过滤，输入即搜索

### 分类导航

- 新拟物凸起胶囊按钮
- 激活态切换为凹陷样式
- 显示每个分类的 Prompt 数量

### 收藏系统

- 红心图标，点击切换收藏状态
- 收藏数据存储在 `localStorage`
- 支持"仅看收藏"筛选

### 使用统计

- 每次复制 prompt 自动计数+1
- 数据持久化到 `localStorage`
- Stats Bar 显示总使用次数

## Do's and Don'ts

### Do

- ✅ 代码块使用等宽字体（JetBrains Mono）
- ✅ 复制按钮使用新拟物凸起样式
- ✅ 搜索支持中英文模糊匹配
- ✅ 收藏状态用心形图标颜色区分（灰色 ↔ 红色）

### Don't

- ❌ 不要在代码块内使用语法高亮（保持纯文本）
- ❌ 不要让搜索结果为空时无提示（显示友好空状态）
- ❌ 不要限制 prompt 长度（支持完整长文本）
- ❌ 不要自动展开所有 prompt（默认折叠，点击展开）

## Agent Prompt Guide

> 当你为 Prompt Library 生成 UI 代码时：
>
> 1. 使用新拟物双向阴影系统（与 Cold Start 相同）
> 2. 代码块使用 `JetBrains Mono` 字体 + `#f0f0f0` 背景
> 3. 标签使用凹陷样式（`inset shadow`），圆角 `40px`
> 4. 搜索输入框使用凹陷样式，实时过滤
> 5. 分类标签栏水平排列，可换行
> 6. 收藏和使用统计通过 `localStorage` 持久化
> 7. 复制功能使用 `navigator.clipboard.writeText()`
> 8. 标题使用 `clamp()` 实现响应式字号
