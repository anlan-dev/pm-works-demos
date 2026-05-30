---
version: "1.0"
name: "剧本·进度复盘"
description: "长剧本创作进度管理工具，高频词分析、热力图看板、场景复盘、AI 剧情生成，多主题适配。"
colors:
  canvas: "#e6e6e6"
  surface: "#e6e6e6"
  text-primary: "#1d1d1f"
  text-secondary: "#424245"
  text-muted: "#86868b"
  accent-blue: "#0071e3"
  tag-bg: "#dedede"
  toast-bg: "rgba(29,29,31,0.9)"
  filter-active-bg: "#0071e3"
  filter-active-text: "#ffffff"
themes:
  light-gray:
    canvas: "#e8e8ed"
    surface: "#e6e6e6"
    text: "#1d1d1f"
    accent: "#0071e3"
    header-bg: "rgba(255,255,255,0.78)"
  dark:
    canvas: "#000000"
    surface: "#1c1c1e"
    card: "#2c2c2e"
    text: "#ffffff"
    accent: "#0a84ff"
typography:
  family: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', system-ui, sans-serif"
  weight-regular: 400
  weight-medium: 500
  weight-semibold: 600
  weight-bold: 700
  heading-size: "1.2rem"
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
  - heatmap-board
  - word-cloud
  - scene-card
  - progress-bar
  - filter-tabs
  - modal-dialog
  - toast-notification
  - ai-panel
---

# 剧本·进度复盘 Design System

## Overview

剧本进度复盘是一款面向**长剧本/网文创作者**的进度管理工具。核心功能包括：高频词分析（词云+柱状图）、热力图看板（每日字数可视化）、场景复盘（按章节/场景查看进度）、AI 剧情辅助生成。

### 设计原则

- **数据驱动**：用热力图和词云让创作进度一目了然
- **场景化**：按场景/章节组织，而非线性文档
- **多主题**：默认浅灰、深色模式，适配长时间写作
- **AI 增强**：AI 面板作为辅助，不干扰主流程

## Colors

### Default — Light Gray

| Token | Value | Usage |
|---|---|---|
| Canvas | `#e8e8ed` | 页面背景 |
| Surface | `#e6e6e6` | 卡片/侧边栏 |
| Text Primary | `#1d1d1f` | 标题、正文 |
| Text Secondary | `#424245` | 说明文字 |
| Text Muted | `#86868b` | 辅助信息（Apple 灰） |
| Accent Blue | `#0071e3` | 链接、选中态 |
| Tag BG | `#dedede` | 标签背景 |
| Filter Active | `#0071e3` | 筛选按钮激活态 |

色板比 Cold Start 更接近 Apple 官方色值（`#1d1d1f` 替代 `#3f3f3f`），因为剧本复盘是数据密集型工具，需要更高对比度。

### Dark — 深色模式

同创作舱的 Apple HIG true black 系统。

## Typography

- **字体栈**：`SF Pro Text` → `PingFang SC` → `system-ui`
- **标题**：bold, 1.2rem
- **数据标签**：medium, 0.75rem
- **正文**：regular, 0.875rem

## Layout

### 工作台布局

```
┌─────────────────────────────────────────────┐
│ Header (标题 + 日期范围 + 导出按钮)          │
├──────┬──────────────────────────────────────┤
│      │ ┌──────────────────────────────────┐ │
│ 侧边栏 │ │ 热力图看板 (GitHub-style)       │ │
│(章节树) │ ├──────────────────────────────────┤ │
│      │ │ 词云 + 高频词柱状图               │ │
│      │ ├──────────────────────────────────┤ │
│      │ │ 场景卡片列表                      │ │
│      │ └──────────────────────────────────┘ │
├──────┴──────────────────────────────────────┤
│ AI 面板 (可折叠)                             │
└─────────────────────────────────────────────┘
```

- **侧边栏**：`220px`，章节/场景树形导航
- **热力图**：GitHub 贡献图风格，按天显示写作字数
- **词云**：字号按词频缩放，颜色按情感分类
- **AI 面板**：底部抽屉，默认折叠

## Elevation

同创作舱设计系统，Light 主题使用新拟物双向阴影，Dark 主题使用 Apple 风格单向阴影 + 半透明边框。

## Do's and Don'ts

### Do

- ✅ 热力图支持月/季/年三种时间跨度
- ✅ 词云支持点击高亮对应场景
- ✅ 场景卡片显示字数、完成度、最后编辑时间
- ✅ 筛选按钮使用新拟物凹陷态标记激活

### Don't

- ❌ 不要在热力图上加过多颜色（保持 4-5 级灰度）
- ❌ 不要让 AI 面板遮挡主内容区
- ❌ 不要在词云中显示停用词（的、了、是）
- ❌ 不要自动保存时打断用户（静默保存 + 状态栏提示）

## Agent Prompt Guide

> 当你为剧本进度复盘生成 UI 代码时：
>
> 1. 使用工作台三栏布局：侧边栏 + 主内容区 + 可折叠 AI 面板
> 2. 热力图使用 CSS Grid，每个格子 12×12px，4-5 级灰度
> 3. 词云使用绝对定位 + 随机旋转（±15°）
> 4. 场景卡片使用新拟物凸起样式，hover 时阴影减弱
> 5. 筛选标签栏支持多选，激活态使用凹陷样式
> 6. 支持 Light Gray / Dark 两套主题切换
> 7. 字体使用 SF Pro Text + PingFang SC
> 8. 数据加载时使用骨架屏（skeleton），不用 spinner
