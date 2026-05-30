---
version: "1.0"
name: "Cold Start · 冷启动行动引擎"
description: "极简拖延行动工具，新拟物风格，大地色系，引导用户把拖延拆解为可执行的第一步。"
colors:
  canvas: "#e6e6e6"
  surface: "#dedede"
  text-primary: "#3f3f3f"
  text-secondary: "#6b6b6b"
  text-muted: "#999999"
  accent: "#5a6a7a"
  accent-green: "#7a8a6a"
  accent-red: "#8a6a6a"
  shadow-light: "rgba(255,255,255,0.66)"
  shadow-dark: "rgba(0,0,0,0.12)"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  weight-light: 300
  weight-regular: 400
  weight-medium: 500
  weight-semibold: 600
  weight-bold: 700
  heading-size: "1.15rem"
  body-size: "0.95rem"
  caption-size: "0.78rem"
rounded:
  small: 16px
  medium: 28px
  large: 32px
  pill: 40px
spacing-unit: 8px
components:
  - neumorphic-card
  - neumorphic-button
  - neumorphic-input
  - tab-bar
  - modal-sheet
  - progress-indicator
---

# Cold Start · 冷启动行动引擎 Design System

## Overview

Cold Start 是一款**极简行动启动器**，核心理念是"别想了，开始"。产品帮助拖延症用户把模糊的焦虑拆解为具体的第一步行动。

### 设计原则

- **克制**：只展示当前最需要的一个动作，其余全部隐藏
- **温柔但坚定**：视觉柔软（新拟物），文案直接（"3-2-1 开始"）
- **零焦虑**：无进度条、无打卡日历、无社交比较

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#e6e6e6` | 页面背景 |
| Surface | `#dedede` | 卡片/输入框背景 |
| Text Primary | `#3f3f3f` | 标题、正文 |
| Text Secondary | `#6b6b6b` | 说明文字 |
| Text Muted | `#999999` | 辅助信息 |
| Accent Blue-Gray | `#5a6a7a` | 主按钮、链接 |
| Accent Green | `#7a8a6a` | 成功状态、完成标记 |
| Accent Red | `#8a6a6a` | 危险操作、倒计时 |

配色为**低饱和大地色系**，三种强调色（蓝灰、橄榄绿、暖灰红）分别对应"思考→行动→反思"三个阶段。

## Typography

- **字体栈**：`Inter` (英文) → `Noto Sans SC` (中文) → `system-ui`
- **标题**：700 weight, 1.15rem, letter-spacing: 2px
- **正文**：600 weight, 0.95rem
- **辅助文字**：500 weight, 0.78rem, 颜色 `#999`
- **无衬线极简风**，不使用装饰性字体

## Layout

- **单列布局**，`max-width: 720px`，居中
- **底部 Tab Bar**：固定定位，4 个标签页（首页/任务/统计/设置）
- **卡片间距**：16px
- **安全区域**：通过 `env(safe-area-inset-bottom)` 适配刘海屏
- **滚动**：`smooth` 平滑滚动

## Elevation（新拟物系统）

双向阴影是本产品的核心视觉语言：

```css
/* 凸起卡片 */
.nr {
  background: var(--bg);
  border-radius: 28px;
  box-shadow: -8px -8px 16px rgba(255,255,255,0.66),
               8px 8px 16px rgba(0,0,0,0.12);
}

/* 凹陷输入框 */
.ni {
  background: var(--bg);
  border-radius: 28px;
  box-shadow: inset 4px 4px 8px rgba(0,0,0,0.06),
              inset -4px -4px 8px rgba(255,255,255,0.5);
}

/* 按钮交互状态 */
.nb { /* 默认凸起 */ }
.nb:hover { /* 阴影减弱 */ }
.nb:active { /* 按下凹陷 */ }
```

## Do's and Don'ts

### Do

- ✅ 每个页面只展示一个核心 CTA
- ✅ 倒计时使用 3-2-1 跳转动画，制造紧迫感
- ✅ Tab 图标使用凹陷态标记当前页
- ✅ 操作反馈用 toast，不弹全屏 modal

### Don't

- ❌ 不要添加打卡日历或连续天数（会增加焦虑）
- ❌ 不要使用红色以外的高饱和颜色
- ❌ 不要在首页展示历史记录
- ❌ 不要加社交分享功能

## Agent Prompt Guide

> 当你为 Cold Start 生成 UI 代码时：
>
> 1. 使用新拟物双向阴影系统（`-8px -8px 16px` 亮 + `8px 8px 16px` 暗）
> 2. 背景色固定为 `#e6e6e6`，不允许白色
> 3. 圆角使用 `28px`（卡片）或 `40px`（按钮/标签）
> 4. 底部 Tab Bar 固定定位，带 `safe-area-inset-bottom`
> 5. 按钮必须有 hover（阴影减弱）和 active（凹陷）状态
> 6. 文案风格：直接、简短、有行动力（"开始"而非"点击此处开始任务"）
> 7. 使用 Inter + Noto Sans SC 字体栈
