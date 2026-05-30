---
version: "1.0"
name: "GlobalFUN · 全球好物跨境拼团"
description: "AI 智能推荐跨境拼团电商平台，多语言切换（中/英/日）、实时汇率、拼团下单全流程体验。"
colors:
  canvas: "#f5f7fb"
  surface: "#e6e6e6"
  text-primary: "#1f2937"
  text-muted: "#6b7280"
  border: "#e5e7eb"
  primary: "#2563eb"
  primary-soft: "#dbeafe"
  success: "#059669"
  warning: "#d97706"
typography:
  family: "'Inter', 'Noto Sans SC', system-ui, sans-serif"
  weight-regular: 400
  weight-medium: 500
  weight-semibold: 600
  weight-bold: 700
  heading-size: "1.25rem"
  body-size: "0.875rem"
  caption-size: "0.75rem"
  price-size: "1.5rem"
rounded:
  small: 8px
  medium: 12px
  card: "var(--neu-card-radius)"
  pill: 999px
spacing-unit: 8px
components:
  - app-shell
  - top-bar
  - lang-switcher
  - product-card
  - group-buy-banner
  - price-tag
  - category-tabs
  - bottom-nav
  - cart-sheet
  - checkout-flow
  - rating-stars
---

# GlobalFUN · 跨境拼团 Design System

## Overview

GlobalFUN 是一款面向**跨境消费者**的拼团电商平台。核心卖点是 AI 智能推荐 + 多语言（中/英/日）+ 实时汇率换算 + 拼团优惠。产品以 430px 宽的移动端视图为中心，模拟真实 APP 体验。

### 设计原则

- **国际感**：蓝色主色调，传达信任与全球化
- **移动优先**：430px 固定宽度，模拟手机屏幕
- **多语言**：中/英/日三语无缝切换，UI 文案实时翻译
- **电商标准**：遵循主流电商 APP 的布局和交互模式

## Colors

| Token | Value | Usage |
|---|---|---|
| Canvas | `#f5f7fb` | 页面背景（浅蓝灰） |
| Surface | `#e6e6e6` | 卡片背景 |
| Text Primary | `#1f2937` | 标题、价格 |
| Text Muted | `#6b7280` | 辅助文字 |
| Border | `#e5e7eb` | 分割线、卡片边框 |
| Primary | `#2563eb` | 按钮、链接、品牌色 |
| Primary Soft | `#dbeafe` | 选中态背景、标签 |
| Success | `#059669` | 拼团成功、折扣标签 |
| Warning | `#d97706` | 库存紧张、倒计时 |

配色采用 **Tailwind CSS 色板**体系（gray-50 ~ gray-900, blue-600, emerald-600），与新拟物产品线形成差异化。

## Typography

- **字体栈**：`Inter` (英文/数字) → `Noto Sans SC` (中文) → `system-ui`
- **品牌名**：700 weight, 18px
- **价格**：700 weight, 1.5rem, 主色蓝
- **商品名**：600 weight, 0.875rem
- **辅助文字**：400 weight, 0.75rem, muted 色

## Layout

### 移动端 APP 壳

```
┌─────────────────────────┐ 430px
│ Top Bar (品牌 + 搜索 + 语言) │
├─────────────────────────┤
│ Category Tabs (横向滑动)    │
├─────────────────────────┤
│ Banner (拼团活动/倒计时)    │
├─────────────────────────┤
│ Product Grid (2列)         │
│ ┌────────┐ ┌────────┐    │
│ │ 图片    │ │ 图片    │    │
│ │ 标题    │ │ 标题    │    │
│ │ ¥→$    │ │ ¥→$    │    │
│ │ 拼团价  │ │ 拼团价  │    │
│ └────────┘ └────────┘    │
├─────────────────────────┤
│ Bottom Nav (首页/发现/购物车/我的) │
└─────────────────────────┘
```

- **App Shell**：`max-width: 430px`，居中，模拟手机
- **Product Grid**：2 列等分，gap 12px
- **Category Tabs**：`overflow-x: auto`，横向滚动
- **Bottom Nav**：固定底部，4 个图标+文字

## Elevation

本产品使用**标准扁平阴影**，非新拟物：

```css
/* 品牌图标 */
box-shadow: 0 4px 12px rgba(37,99,235,0.2);

/* 卡片 */
box-shadow: var(--neu-shadow); /* 继承 shared CSS */
```

## 特殊组件

### 价格标签

```
原价: ¥299 / $42.5
拼团价: ¥199 / $28.3
```

- 支持双币显示（人民币 + 美元）
- 原价使用删除线
- 汇率实时更新，显示更新时间

### 语言切换器

- 顶部导航栏右侧，显示当前语言 flag + 缩写
- 点击弹出选择器：🇨🇳 中文 / 🇺🇸 English / 🇯🇵 日本語
- 切换后所有 UI 文案即时翻译，无需刷新
- 语言偏好存储在 `localStorage`

### 拼团倒计时

- 使用 `setuptools` 倒计时组件
- 橙色背景 + 白色数字
- 显示"还差 X 人成团"

## Do's and Don'ts

### Do

- ✅ 所有价格同时显示人民币和美元
- ✅ 语言切换后整个页面文案即时更新
- ✅ 商品卡片图片使用 `object-fit: cover`
- ✅ 拼团进度使用进度条 + 文字双重提示

### Don't

- ❌ 不要使用新拟物阴影（本产品是扁平电商风格）
- ❌ 不要硬编码货币符号（根据语言动态切换）
- ❌ 不要忽略日语的竖排排版适配
- ❌ 不要在商品列表使用无限滚动（用分页）

## Agent Prompt Guide

> 当你为 GlobalFUN 生成 UI 代码时：
>
> 1. 使用 `max-width: 430px` 的移动 APP 壳布局
> 2. 色板使用 Tailwind CSS 体系（blue-600 = `#2563eb`）
> 3. 价格组件必须支持双币显示（¥ / $）
> 4. 语言切换使用 i18n 对象 + `_i18n` 函数，存储到 localStorage
> 5. 拼团倒计时使用 `setuptools` 组件
> 6. Category Tabs 使用横向滚动，不换行
> 7. Bottom Nav 固定底部，图标+文字垂直排列
> 8. 阴影风格：扁平阴影，非新拟物
