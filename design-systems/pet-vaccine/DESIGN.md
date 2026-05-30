---
version: alpha
name: 宠伴·健康台账
description: A neumorphic pet health tracking interface with warm cream canvas, soft inner/outer shadows, and a calming blue primary accent. The system prioritizes touch-friendly cards, gentle transitions, and data-driven health visualizations. Designed for pet owners who need quick-glance health status and frictionless vaccine logging.
colors:
  primary: "#4a90d9"
  primary-hover: "#3a7bc8"
  primary-active: "#2a6ab7"
  primary-disabled: "#a8c5e8"
  success: "#2b7a4b"
  success-light: "#e8f5e9"
  warning: "#c09040"
  warning-light: "#fff3e0"
  danger: "#c04040"
  danger-light: "#ffebee"
  ink: "#2d3436"
  body: "#4a4a4a"
  muted: "#7f8c8d"
  muted-soft: "#b2bec3"
  hairline: "#d1d9e6"
  canvas: "#f0f0f3"
  surface: "#ffffff"
  surface-raised: "#f8f9fa"
  shadow-dark: "rgba(0, 0, 0, 0.1)"
  shadow-light: "rgba(255, 255, 255, 0.7)"
typography:
  display-lg:
    fontFamily: "'Noto Sans SC', 'SF Pro Display', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans SC', 'SF Pro Display', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title:
    fontFamily: "'Noto Sans SC', 'SF Pro Display', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Noto Sans SC', 'SF Pro Text', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body:
    fontFamily: "'Noto Sans SC', 'SF Pro Text', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans SC', 'SF Pro Text', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  button:
    fontFamily: "'Noto Sans SC', 'SF Pro Text', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
rounded:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  pill: 9999px
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
components:
  card-neumorphic:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 20px
    boxShadow: "8px 8px 16px {colors.shadow-dark}, -8px -8px 16px {colors.shadow-light}"
  card-neumorphic-pressed:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 20px
    boxShadow: "inset 4px 4px 8px {colors.shadow-dark}, inset -4px -4px 8px {colors.shadow-light}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "#ffffff"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "#ffffff"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  input-field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    boxShadow: "inset 2px 2px 5px {colors.shadow-dark}, inset -2px -2px 5px {colors.shadow-light}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 60px
  tab-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  status-badge-healthy:
    backgroundColor: "{colors.success-light}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  status-badge-warning:
    backgroundColor: "{colors.warning-light}"
    textColor: "{colors.warning}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  status-badge-danger:
    backgroundColor: "{colors.danger-light}"
    textColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  pet-avatar:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    size: 64px
  chart-container:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px
---
## Overview
宠伴·健康台账 is a neumorphic pet health tracking PWA. The base atmosphere is a **warm light-gray canvas** (`{colors.canvas}` — #f0f0f3) with soft inner and outer shadows creating the signature neumorphic depth. The design philosophy is **gentle, approachable, and data-driven** — pet owners should feel calm while tracking health data.

Brand identity comes from the **blue + cream pairing** — calming blue (`{colors.primary}` — #4a90d9) for primary actions, warm cream canvas for the background. The neumorphic shadow system uses two shadows: a dark shadow (`rgba(0,0,0,0.1)`) and a light shadow (`rgba(255,255,255,0.7)`) to create the raised/pressed effect.

**Key Characteristics:**
- Neumorphic card system with dual shadows (dark + light)
- Warm light-gray canvas (#f0f0f3) as the base
- Calming blue primary (#4a90d9) for actions
- Green/amber/red semantic status badges
- Touch-friendly 44px minimum touch targets
- Gentle transitions (0.3s ease)
- Data visualization with Chart.js (doughnut charts, line trends)
- PWA-ready with offline support
## Colors
### Brand & Accent
- **Primary Blue** ({colors.primary} — #4a90d9): Main CTA, active tabs, links
- **Primary Hover** ({colors.primary-hover} — #3a7bc8): Hover state
- **Primary Active** ({colors.primary-active} — #2a6ab7): Pressed state
- **Primary Disabled** ({colors.primary-disabled} — #a8c5e8): Disabled buttons
### Semantic
- **Success Green** ({colors.success} — #2b7a4b): Healthy status, completed actions
- **Warning Amber** ({colors.warning} — #c09040): Upcoming vaccines, alerts
- **Danger Red** ({colors.danger} — #c04040): Overdue, errors
### Surface
- **Canvas** ({colors.canvas} — #f0f0f3): Page background, neumorphic base
- **Surface** ({colors.surface} — #ffffff): Cards, modals, elevated content
- **Surface Raised** ({colors.surface-raised} — #f8f9fa): Subtle elevation
### Text
- **Ink** ({colors.ink} — #2d3436): Headlines
- **Body** ({colors.body} — #4a4a4a): Running text
- **Muted** ({colors.muted} — #7f8c8d): Secondary labels
- **Muted Soft** ({colors.muted-soft} — #b2bec3): Captions, timestamps
## Typography
### Font Family
- **Noto Sans SC** — Chinese + Latin display and body
- **SF Pro Display** — macOS/iOS fallback
- **SF Pro Text** — Body text fallback
### Hierarchy
| Token | Size | Weight | Use |
|---|---|---|---|
| display-lg | 28px | 700 | Page titles |
| display-md | 22px | 600 | Section headers |
| title | 18px | 600 | Card titles |
| body-lg | 16px | 400 | Lead text, form labels |
| body | 14px | 400 | Default body |
| caption | 12px | 500 | Badges, timestamps |
| button | 14px | 600 | Button labels |
## Layout
### Spacing System
- Base unit: 4px
- Card padding: 20px
- Section gap: 24px
- Page padding: 16px (mobile), 24px (tablet)
### Grid
- Mobile-first single column
- Tablet: 2-column card grid
- Max width: 480px (mobile PWA)
## Elevation & Depth
| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow | Background text |
| 1 (raised) | Outer shadow (8px 8px 16px dark/light) | Default cards |
| 2 (pressed) | Inner shadow (inset 4px 4px 8px) | Active buttons, input fields |
| 3 (floating) | Larger outer shadow + border | Modals, dropdowns |
## Do's and Don'ts
### Do
- Use neumorphic shadows consistently on all cards
- Keep touch targets ≥ 44px
- Use semantic colors for status (green/amber/red)
- Show data visualizations for health trends
- Use gentle transitions (0.3s ease)
### Don't
- Use flat design — always apply neumorphic shadows
- Use harsh borders — shadows replace borders
- Overcrowd cards — maintain generous padding
- Use bright/saturated colors — keep palette muted
## Responsive
- Mobile: 320px - 480px, single column
- Tablet: 481px - 768px, 2-column grid
- Touch targets: 44px minimum
- Bottom tab bar: 60px height, 5 tabs max
## Agent Prompt Guide
```
请按照 DESIGN.md 的新拟物风格规范构建宠物健康记录页面：
- 背景色 #f0f0f3，卡片使用双向阴影（8px 8px 16px rgba(0,0,0,0.1) + -8px -8px 16px rgba(255,255,255,0.7)）
- 主色调 #4a90d9，圆角 16px
- 输入框使用内阴影效果
- 状态标签使用胶囊形状（绿色=健康，橙色=待接种，红色=逾期）
- 移动端优先，底部 Tab 栏导航
```
