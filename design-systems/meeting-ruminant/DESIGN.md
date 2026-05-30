---
version: alpha
name: 会议·反刍舱
description: A dark-themed meeting productivity interface with deep navy canvas, gradient accents, and data-dense dashboard panels. The system emphasizes audio waveform visualization, timeline-based content navigation, and structured todo extraction from meeting transcripts.
colors:
  primary: "#6366f1"
  primary-hover: "#818cf8"
  primary-active: "#4f46e5"
  success: "#10b981"
  warning: "#f59e0b"
  danger: "#ef4444"
  ink: "#f1f5f9"
  body: "#cbd5e1"
  muted: "#94a3b8"
  muted-soft: "#64748b"
  canvas: "#0f172a"
  surface-1: "#1e293b"
  surface-2: "#334155"
  surface-3: "#475569"
  hairline: "#334155"
  accent-gradient-start: "#6366f1"
  accent-gradient-end: "#8b5cf6"
typography:
  display-lg:
    fontFamily: "'Inter', 'SF Pro Display', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'SF Pro Display', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title:
    fontFamily: "'Inter', 'SF Pro Text', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body:
    fontFamily: "'Inter', 'SF Pro Text', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'SF Pro Text', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  mono:
    fontFamily: "'JetBrains Mono', 'SF Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
rounded:
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px
spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
components:
  card-dark:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 20px
    border: "1px solid {colors.hairline}"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 20px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: 10px 20px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  input-field:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    border: "1px solid {colors.hairline}"
  badge-status:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  audio-waveform:
    backgroundColor: "{colors.surface-1}"
    accentColor: "{colors.primary}"
    height: 48px
  timeline-item:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    borderLeft: "2px solid {colors.hairline}"
    padding: "12px 0 12px 16px"
---
## Overview
会议·反刍舱 is a dark-themed meeting productivity tool. The atmosphere is **deep navy canvas** (`{colors.canvas}` — #0f172a) with a three-step surface ladder for content hierarchy. The design philosophy is **focused, data-dense, and professional** — users should feel productive and in control.

The single chromatic accent is **indigo-purple** (`{colors.primary}` — #6366f1) with a gradient variant for emphasis. The dark theme reduces eye strain during long meeting review sessions.

**Key Characteristics:**
- Deep navy canvas (#0f172a) with surface ladder
- Indigo-purple accent (#6366f1) for primary actions
- Audio waveform visualization with gradient fill
- Timeline-based content navigation
- Structured todo extraction with status badges
- Monospace font for transcript text
- Chart.js data visualizations (line charts, bar charts)
## Colors
### Brand & Accent
- **Indigo** ({colors.primary} — #6366f1): Primary CTA, active states
- **Gradient** (indigo → purple): Audio waveform, emphasis elements
### Surface
- **Canvas** (#0f172a): Page background
- **Surface 1** (#1e293b): Default cards
- **Surface 2** (#334155): Elevated cards, hover states
- **Surface 3** (#475569): Active/selected states
### Text
- **Ink** (#f1f5f9): Headlines on dark
- **Body** (#cbd5e1): Running text
- **Muted** (#94a3b8): Secondary labels
## Layout
- Mobile-first, single column
- Sidebar navigation on desktop
- Bottom controls for audio playback
## Do's and Don'ts
### Do
- Use dark surfaces consistently
- Maintain high contrast for readability
- Use gradient accents sparingly for emphasis
### Don't
- Use light backgrounds — stay in dark theme
- Overuse gradients — reserve for key elements
## Agent Prompt Guide
```
请按照 DESIGN.md 的暗色主题规范构建会议记录页面：
- 背景色 #0f172a，卡片使用 #1e293b
- 主色调 #6366f1，渐变用于音频波形
- 文字颜色 #f1f5f9（标题）/ #cbd5e1（正文）
- 使用等宽字体显示转写文本
```
