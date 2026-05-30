# Awesome DESIGN.md · 王天娇作品集设计系统

> 基于 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 的理念，为每个项目创建 DESIGN.md 文件。
> 将 DESIGN.md 放入项目根目录，AI 编码工具即可生成一致的 UI。

---

## 什么是 DESIGN.md？

[DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) 是 Google Stitch 提出的概念——一份给 AI 看的纯文本设计系统说明书。

| 文件 | 谁读 | 定义什么 |
|------|------|---------|
| `AGENTS.md` | 编码 Agent | 如何构建项目 |
| `DESIGN.md` | 设计 Agent | 项目应该长什么样 |

**本仓库为 8 个项目提供即用的 DESIGN.md 文件。**

---

## 📁 项目设计系统

### 🏥 健康医疗类

| 项目 | DESIGN.md | 描述 |
|------|-----------|------|
| **宠伴·健康台账** | [pet-vaccine/DESIGN.md](./pet-vaccine/DESIGN.md) | 新拟物风格，Noto Sans SC，暖色调，宠物疫苗/驱虫/体检记录 |
| **会议·反刍舱** | [meeting-ruminant/DESIGN.md](./meeting-ruminant/DESIGN.md) | 暗色主题，深海军蓝画布，indigo-purple 强调色，录音转写+会议复盘 |

### 🏠 生活服务类

| 项目 | DESIGN.md | 描述 |
|------|-----------|------|
| **住值·租房决策** | [zhuzhi-rent/DESIGN.md](./zhuzhi-rent/DESIGN.md) | 新拟物风格，双轴图表（净收益+租收比），滑块输入，租房计算器 |
| **冷启动·行动引擎** | [cold-start/DESIGN.md](./cold-start/DESIGN.md) | 极简新拟物，大地色系（蓝灰/橄榄绿/暖灰红），倒计时启动器 |

### 🎨 创作工具类

| 项目 | DESIGN.md | 描述 |
|------|-----------|------|
| **星途·创作舱** | [creation-cabin/DESIGN.md](./creation-cabin/DESIGN.md) | 三栏工作台，4 套主题（浅灰/深色/薄荷/墨水屏），角色管理+大纲+多格式导出 |
| **剧本·进度复盘** | [script-review/DESIGN.md](./script-review/DESIGN.md) | 热力图看板+词云+场景卡片，Apple HIG 色板，AI 剧情辅助生成 |

### 🌐 跨境电商类

| 项目 | DESIGN.md | 描述 |
|------|-----------|------|
| **GlobalFUN·跨境拼团** | [cross-border-ai/DESIGN.md](./cross-border-ai/DESIGN.md) | 移动 APP 壳 (430px)，Tailwind 色板，中/英/日三语 i18n，双币价格 |

### 🛠 工具效率类

| 项目 | DESIGN.md | 描述 |
|------|-----------|------|
| **Prompt Library** | [prompt-library/DESIGN.md](./prompt-library/DESIGN.md) | 新拟物极简，JetBrains Mono 代码块，搜索+收藏+使用统计，localStorage 持久化 |

---

## 🎨 两大设计家族

### 家族 A：新拟物（Neumorphism）

**适用项目**：宠伴、住值、冷启动、Prompt Library

```css
/* 凸起卡片 — 双向阴影 */
.nr {
  box-shadow: -8px -8px 16px rgba(255,255,255,0.66),
               8px 8px 16px rgba(0,0,0,0.12);
}

/* 凹陷输入框 */
.ni {
  box-shadow: inset 4px 4px 8px rgba(0,0,0,0.06),
              inset -4px -4px 8px rgba(255,255,255,0.5);
}

/* 按钮交互 — hover 减弱, active 凹陷 */
.nb:hover { box-shadow: -3px -3px 8px var(--sl), 3px 3px 8px var(--sd); }
.nb:active { box-shadow: inset 4px 4px 8px rgba(0,0,0,0.08), inset -4px -4px 8px rgba(255,255,255,0.4); }
```

| 项目 | 画布色 | 强调色 | 特色 |
|------|--------|--------|------|
| 宠伴 | `#f0f0f3` | `#4a90d9` | 暖色调，Noto Sans SC |
| 住值 | `#e6e6e6` | `#5a6a7a` | 双轴图表，滑块输入 |
| 冷启动 | `#e6e6e6` | `#5a6a7a` | 大地色三色系，倒计时 |
| Prompt Lib | `#e6e6e6` | `#5a6a7a` | JetBrains Mono 代码块 |

### 家族 B：扁平/Apple HIG

**适用项目**：会议反刍、创作舱、剧本复盘、GlobalFUN

| 项目 | 风格 | 画布色 | 强调色 | 主题数 |
|------|------|--------|--------|--------|
| 会议反刍 | 深色专业 | `#0a1628` | `#818cf8` | 1 (暗) |
| 创作舱 | 多主题 | `#e6e6e6` | `#0071e3` | 4 (浅灰/暗/薄荷/墨水屏) |
| 剧本复盘 | Apple HIG | `#e8e8ed` | `#0071e3` | 2 (浅灰/暗) |
| GlobalFUN | 电商扁平 | `#f5f7fb` | `#2563eb` | 1 (浅) |

---

## 📦 每个 DESIGN.md 包含

| 章节 | 内容 |
|------|------|
| 1. Visual Theme | 氛围、密度、设计哲学 |
| 2. Color Palette | 语义色 + 功能角色 |
| 3. Typography | 字体、层级表 |
| 4. Components | 按钮、卡片、输入框、导航 |
| 5. Layout | 间距、网格、留白 |
| 6. Depth | 阴影、表面层级 |
| 7. Do's and Don'ts | 设计红线 |
| 8. Responsive | 断点、触控目标 |
| 9. Agent Prompt | 快速色彩参考、即用提示词 |

---

## 🚀 使用方法

1. 选择一个项目的 `DESIGN.md`
2. 复制到你的项目根目录
3. 告诉 AI Agent："按照 DESIGN.md 的规范构建 UI"

### 示例 Prompt

```
请按照 DESIGN.md 的设计规范，构建一个宠物健康记录页面。
要求：
- 使用新拟物风格（参考 DESIGN.md 中的阴影系统）
- 主色调使用 #4a90d9
- 卡片圆角 16px
- 移动端优先，响应式布局
```

---

## 🔗 相关资源

- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - 62.8k stars，55+ 大厂设计系统
- [Google Stitch](https://stitch.withgoogle.com/) - AI 驱动的 UI 生成工具
- [DESIGN.md 格式文档](https://stitch.withgoogle.com/docs/design-md/format/)

---

## 📝 贡献

欢迎提交 Issue 或 PR 来改进设计系统文件。

---

## 📄 License

MIT License

---

**作者**：王天娇 · PM Portfolio
**GitHub**：[anlan-dev/pm-works-demos](https://github.com/anlan-dev/pm-works-demos)
