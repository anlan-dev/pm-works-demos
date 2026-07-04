# UI 设计作品集 · 王天娇

> **每个像素都有它的道理** —— 产品经理视角的 UI 设计，每个设计决策都有商业逻辑支撑。

## 🎯 作品概览

| # | 作品 | 风格 | 核心亮点 |
|---|------|------|----------|
| 01 | **MoneyFlow 财务仪表盘** | 扁平 + 渐变 | Z型阅读流、Progressive Disclosure、数字跳动动画 |
| 02 | **HabitFlow 健康打卡** | 暖色调 | BJ Fogg 行为模型、损失厌恶心理学、进度环动画 |
| 03 | **CloudSync SaaS 定价页** | 扁平 + 渐变 | 锚定效应、Von Restorff 效应、年付默认选中 |
| 04 | **宠伴·健康台账** | 标准浅色 | 多主题切换、OCR 识别、数据看板、Excel 导出 |
| 05 | **GlobalCart 跨境电商** | 电商扁平 | 中/英/日三语 i18n、双币价格、AI 智能推荐 |
| 06 | **创作工作台** | 多主题 | 三栏布局、4 套主题、角色管理、多格式导出 |
| 07 | **Prompt Library** | 标准浅色 | 搜索收藏、使用统计、LocalStorage 持久化 |
| 08 | **Lofi 玻璃态音乐播放器** | Glassmorphism | 毛玻璃 backdrop-filter、韵律波动画、沉浸深色背景 |
| 09 | **NEON 赛博朋克数据看板** | Cyberpunk / Neon | 霓虹色板、网格背景、等宽字体数据、系统负载监控 |
| 10 | **粋·SUI 日式极简任务管理** | 侘寂极简 | 大量留白、衬线字体、米白画布、朱红单色强调 |
| 11 | **BRUTAL STUDIO 粗野主义品牌** | Brutalism | 纯黑白+红、零圆角、超大字重、粗边框 |

## 🧠 设计理念

### 四个核心原则

1. **用户优先** — 每个设计决策都从「用户需要什么」出发，而非「技术能做什么」
2. **数据驱动** — 用 A/B 测试和行为数据验证设计假设，不依赖主观审美判断
3. **心理学应用** — 锚定效应、损失厌恶、Fitts's Law——每个交互都有理论支撑
4. **效率优先** — 减少认知负荷和操作步骤，让用户用最少的思考完成任务

### 设计风格家族

| 家族 | 风格 | 适用场景 | 代表作品 |
|------|------|----------|----------|
| **A. 标准浅色** | 白卡片、浅灰画布、统一阴影 | 工具类、健康类、效率类 | 宠伴、Prompt Library |
| **B. 扁平/Apple HIG** | 渐变、阴影、简洁 | 数据密集型、电商、专业工具 | MoneyFlow、CloudSync |
| **C. Glassmorphism** | backdrop-filter 毛玻璃、半透明层次 | 音乐/娱乐/氛围类产品 | Lofi 音乐播放器 |
| **D. Cyberpunk / Neon** | 霓虹色、网格背景、荧光高亮 | 游戏/科技数据产品 | NEON 数据看板 |
| **E. 日式极简 / 侘寂** | 大量留白、衬线字体、自然色 | 效率/创意工具 | 粋·SUI 任务管理 |
| **F. Brutalism** | 零圆角、粗边框、纯对比色 | 先锋品牌/艺术机构 | BRUTAL STUDIO |

## 🛠 技术实现

- **CSS 变量系统** — 每个作品独立色板，统一命名规范
- **IntersectionObserver** — 滚动入场动画，分级延迟
- **requestAnimationFrame** — 数字跳动动画，easeOutCubic 缓动
- **SVG 动画** — 进度环、图标动效
- **LocalStorage** — 数据持久化（Prompt Library）
- **Chart.js** — 数据可视化（财务仪表盘、宠物台账）
- **backdrop-filter** — 毛玻璃效果（Glassmorphism 音乐播放器）
- **CSS Grid + 文字阴影** — 霓虹灯管效果（Cyberpunk 数据看板）
- **Noto Serif SC** — 衬线字体营造人文质感（侘寂任务管理）
- **墨刀标注系统** — 自研原型标注交互（modao-annotations.js / .css）
- **多端适配** — 响应式设计，支持 430px 移动端到 1440px 桌面端

## 📁 项目结构

```
UIwork/
├── index.html                ← 作品集首页（暗色风格、毛玻璃导航）
├── 01-finance-dashboard.html
├── 02-health-tracker.html
├── 03-saas-pricing.html
├── 04-pet-vaccine.html
├── 05-cross-border-ai.html
├── 06-creation-cabin.html
├── 07-prompt-library.html
├── 08-glassmorphism.html
├── 09-cyberpunk.html
├── 10-japanese-minimal.html
├── 11-brutalist.html
├── modao-annotations.css     ← 墨刀原型标注样式
└── modao-annotations.js      ← 墨刀原型标注逻辑
```

## 🚀 本地预览

```bash
# 克隆仓库
git clone https://github.com/anlan-dev/UI-work.git

# 进入目录
cd UI-work

# 用浏览器打开 index.html
# 或使用 Live Server（VS Code 插件）
```

## 📊 设计决策统计

- **作品数量**: 11 个
- **设计决策**: 45+ 个
- **心理学理论**: 16 个
- **设计风格**: 6 种（标准浅色、扁平、Glassmorphism、Cyberpunk、侘寂、Brutalism）
- **响应式断点**: 430px / 768px / 1024px / 1440px
- **墨刀标注系统**: 自研原型标注交互（modao-annotations.js）

## 🔗 相关链接

- **GitHub**: [anlan-dev/UI-work](https://github.com/anlan-dev/UI-work)
- **PM 作品集**: [anlan-dev/pm-works-demos](https://github.com/anlan-dev/pm-works-demos)
- **Email**: Wangtj0212@outlook.com

---

## 📚 设计规范文档

本作品集配套完整的设计规范文档，位于 `../work/设计参考/` 目录：

| 文档 | 内容 | 用途 |
|------|------|------|
| **设计规范_色彩与字体系统.md** | 色彩体系、字体层级、间距系统、圆角规范、阴影规范 | 视觉设计参考 |
| **设计规范_交互逻辑与动效.md** | 交互原则、动效系统、手势交互、状态反馈、无障碍设计 | 交互设计参考 |
| **设计规范_组件与布局系统.md** | 栅格系统、响应式断点、按钮/卡片/输入框等组件规范 | 组件开发参考 |
| **UI调整记录_2026-06-19.md** | 今日全项目UI/UX审计与优化记录 | 版本记录 |
| **APP界面截图清单.md** | 50+ 个优秀APP参考链接（站酷/Dribbble/Behance） | 设计灵感 |

### 设计系统概览

```
色彩系统：
  浅色主题：#f5f5f7 画布 + #ffffff 卡片 + #0071e3 主色
  暗色主题：#050507 画布 + #111115 卡片 + #a78bfa 强调
  日式极简：#faf8f5 米白画布 + #c4553a 朱红强调

字体系统：
  主字体：Inter + Noto Sans SC
  层级：Display(2.4-4rem) → H1(1.5-2rem) → Body(0.875-1rem) → Caption(0.75rem)

间距系统：
  基数：4px
  常用：8px / 12px / 16px / 24px / 32px / 48px

圆角规范：
  sm=8px / md=12px / lg=16px / xl=20px / full=999px

阴影规范：
  sm: 0 1px 3px rgba(0,0,0,0.04)
  md: 0 1px 3px rgba(0,0,0,0.04), 0 8px 24px rgba(0,0,0,0.04)
  lg: 0 4px 12px rgba(0,0,0,0.04), 0 16px 48px rgba(0,0,0,0.06)
```

---

**每个像素都有它的道理** ✨
