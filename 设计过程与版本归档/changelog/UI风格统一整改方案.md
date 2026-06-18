# UI 风格统一整改方案

> 版本：v1.0 | 日期：2026-06-19
> 范围：demo/work/ 全部 12 个 HTML Demo
> 基线：commit `586c7ba`（design-systems v2.0 更新后）

---

## 一、排查结果总览

### 1.1 分类统计

| 状态 | 文件数 | 文件列表 |
|------|--------|---------|
| **已完成改造** | 8 | pet-vaccine / meeting-ruminant / index / creation-cabin / script-review / cross-border-ai / zhuzhi-rent / cold-start / prompt-library / demo-hub |
| **有残留代码需清理** | 6 | creation-cabin / script-review / zhuzhi-rent / prompt-library / vn-game |
| **从未改造（Neumorphic 完整）** | 1 | vn-game.html |
| **特殊风格（非 Neumorphic）** | 1 | branch_tree.html |

### 1.2 详细排查

#### A. 已完成改造 + 有残留代码（需清理）

| 文件 | 残留类型 | 残留位置 | 严重度 |
|------|---------|---------|--------|
| creation-cabin.html | `#e6e6e6` 色值 | CSS 变量 `--soft-bg` + 注释 | 低（深色主题变量） |
| script-review.html | `#e6e6e6` 色值 | 深色主题 `--form-bg` / `--record-bg` / `--toast-text` | 低（深色主题变量） |
| zhuzhi-rent.html | `#e6e6e6` 色值 | 主题切换点 `.theme-dot.t-light` | 低（主题指示器） |
| prompt-library.html | `#e6e6e6` 色值 | Prompt 内容文本中 | 无（内容文本） |
| cross-border-ai.html | `#e6e6e6` 色值 | DESIGN 注释中 | 无（注释） |
| cold-start.html | `#e6e6e6` 色值 | DESIGN 注释中 | 无（注释） |

#### B. 从未改造（Neumorphic 完整）

| 文件 | 当前风格 | 问题 |
|------|---------|------|
| **vn-game.html** | Neumorphic 完整 | `--bg: #e6e6e6`、双向阴影 `8px 8px 16px`、圆角 28px、无 Inter 字体 |

#### C. 特殊风格（需单独评估）

| 文件 | 当前风格 | 评估 |
|------|---------|------|
| **branch_tree.html** | 深色哥特风（#120f0c 画布、#ead9bc 纸张色） | 非 Neumorphic，风格独特且与产品主题强绑定（《雾灯残页》游戏结构图），建议保留现有风格但微调细节 |

---

## 二、vn-game.html 专属 UI 改造计划

### 2.1 产品定位分析

| 维度 | 描述 |
|------|------|
| **产品名称** | 雾灯残页 · AIGC 游戏开发 |
| **核心功能** | 哥特文字冒险游戏，全程 AIGC 辅助开发 |
| **目标用户** | 游戏/互动内容爱好者、AIGC 技术关注者 |
| **产品属性** | 消费娱乐类 |
| **品牌原型** | Playful Approachable（有趣+沉浸） |
| **Tech-Comfort** | 6-8（熟悉游戏交互） |

### 2.2 UI 风格选型

**当前风格**：Neumorphic（灰色凸起卡片、双向阴影）
**问题**：Neumorphic 的"柔和凸起"与哥特冒险游戏的"悬疑暗沉"氛围严重不符

**目标风格**：**沉浸式暗色叙事风**

参考设计趋势：
- 视觉小说/文字冒险游戏的暗色沉浸式 UI
- 哥特美学：深色底+暖光点缀+衬线字体
- 与 branch_tree.html 的深色哥特风保持一致（同产品线）

### 2.3 色彩体系重构

```css
/* 旧 Neumorphic 色彩 */
--bg: #e6e6e6;           /* 浅灰画布 */
--text: #3f3f3f;         /* 深灰文字 */
--accent: #5a6a7a;       /* 蓝灰强调 */
--shadow: -8px -8px 16px rgba(255,255,255,0.66), 8px 8px 16px rgba(0,0,0,0.12);

/* 新沉浸式暗色叙事色彩 */
--bg: #0f0e0c;           /* 深色哥特画布 */
--bg-card: #1a1816;      /* 深色卡片 */
--text: #e8ddd0;         /* 暖白文字（旧纸感） */
--muted: #8a7e72;        /* 暖灰辅助 */
--accent: #c49a6c;       /* 暖金强调（灯光/火焰） */
--accent-soft: rgba(196,154,108,0.12);
--danger: #a04040;       /* 暗红（危险/悬疑） */
--shadow: 0 4px 16px rgba(0,0,0,.4);
--border: rgba(196,154,108,0.1);
--card-radius: 12px;
```

**色彩 rationale**：
- 深色画布 `#0f0e0c`：营造夜晚/悬疑氛围
- 暖白文字 `#e8ddd0`：旧纸/羊皮纸质感，避免纯白刺眼
- 暖金强调 `#c49a6c`：灯光/烛光/火焰意象
- 暗红 `#a04040`：危险/紧张情绪

### 2.4 排版系统

```css
/* 旧 Neumorphic 字体 */
font-family: system-ui, sans-serif;

/* 新叙事字体 */
--font-body: 'Noto Serif SC', Georgia, serif;      /* 衬线体增强叙事感 */
--font-ui: 'Inter', 'Noto Sans SC', system-ui;     /* UI 元素用无衬线 */
--font-mono: 'JetBrains Mono', monospace;           /* 代码/特殊文本 */

/* 字号层级 */
--text-xl: 24px/700;    /* 章节标题 */
--text-lg: 18px/600;    /* 场景标题 */
--text-md: 15px/400;    /* 叙事正文（稍大，增强阅读感） */
--text-sm: 13px/500;    /* UI 辅助 */
```

### 2.5 交互体验优化

| 交互场景 | 当前实现 | 改造方案 |
|----------|---------|---------|
| **对话推进** | 点击推进 | 添加打字机效果（逐字出现，50ms/字） |
| **选项选择** | 普通按钮 | 暗色卡片+暖金边框+hover 发光效果 |
| **场景切换** | 无过渡 | 添加淡入淡出（400ms ease-in-out） |
| **存档/读档** | 无 | 新增存档槽位卡片（暖金色激活态） |
| **文字动画** | 静态 | 关键句添加轻微震动（CSS shake） |

### 2.6 响应式适配

| 断点 | 布局 | 特殊处理 |
|------|------|---------|
| Mobile (360-412px) | 全屏对话+底部选项 | 对话区占 70vh，选项区占 30vh |
| Tablet (768px) | 居中卡片（max-width 600px） | 两侧留暗色边距增强沉浸感 |
| Desktop (1024px+) | 居中卡片（max-width 720px） | 背景添加雾气/粒子效果 |

### 2.7 视觉层级

```
Layer 1: 对话文本（最大视觉权重）
  → 衬线体 15px，暖白色，行高 1.8

Layer 2: 选项按钮（次级权重）
  → 暗色卡片+暖金边框，hover 发光

Layer 3: UI 控制（最低权重）
  → 存档/设置/返回，13px，暖灰色
```

### 2.8 实施排期

| 阶段 | 任务 | 优先级 |
|------|------|--------|
| Phase 1 | CSS 变量替换（色彩+字体+阴影+圆角） | P0 |
| Phase 2 | 打字机效果+选项交互优化 | P1 |
| Phase 3 | 场景切换动效+存档系统 UI | P2 |
| Phase 4 | 响应式适配+深色主题 polish | P2 |

---

## 三、branch_tree.html 评估与微调方案

### 3.1 当前状态评估

| 维度 | 评估 |
|------|------|
| **风格** | 深色哥特风（#120f0c 画布、#ead9bc 纸张色） |
| **是否 Neumorphic** | 否 |
| **与产品主题匹配度** | 高（《雾灯残页》游戏结构图，哥特美学） |
| **需要改造** | 不需要大改，仅需微调细节 |

### 3.2 微调方案

| 调整项 | 当前值 | 建议值 | 理由 |
|--------|--------|--------|------|
| 字体 | system-ui | `Inter + Noto Serif SC` | 与 vn-game 统一叙事字体 |
| 触控目标 | 未检查 | 确保 ≥ 44px | 移动端可访问性 |
| 动效 | 无 | 节点 hover 轻微放大 | 增强交互反馈 |
| 响应式 | 未检查 | 移动端画布支持双指缩放 | 小屏查看复杂树形结构 |

---

## 四、残留代码清理方案

### 4.1 creation-cabin.html

**残留位置**：CSS 变量 `--soft-bg: #e6e6e6`（深色主题中）

**清理方案**：
```css
/* 旧值 */
--soft-bg: #e6e6e6;

/* 新值 */
--soft-bg: #2a2a2a;  /* 深色主题下应使用深色值 */
```

### 4.2 script-review.html

**残留位置**：深色主题中 `--form-bg` / `--record-bg` / `--toast-text`

**清理方案**：
```css
/* 旧值 */
--form-bg: #e6e6e6;
--record-bg: #e6e6e6;
--toast-text: #e6e6e6;

/* 新值 */
--form-bg: #2a2a2a;
--record-bg: #2a2a2a;
--toast-text: #f5f5f7;
```

### 4.3 zhuzhi-rent.html

**残留位置**：主题切换点 `.theme-dot.t-light { background: #e6e6e6; }`

**清理方案**：
```css
/* 旧值 */
.theme-dot.t-light { background: #e6e6e6; }

/* 新值 */
.theme-dot.t-light { background: #f5f5f7; }
```

### 4.4 DESIGN 注释更新

**cross-border-ai.html / cold-start.html / creation-cabin.html / prompt-library.html**

更新 DESIGN 注释块中的色值描述，与实际 CSS 变量一致。

---

## 五、整改验收标准

| 验收项 | 标准 | 检查方法 |
|--------|------|---------|
| Neumorphic 残留 | `#e6e6e6` 出现次数 = 0（注释和内容文本除外） | Grep 扫描 |
| 双向阴影 | `8px 8px 16px` / `-8px -8px 16px` 出现次数 = 0 | Grep 扫描 |
| 字体统一 | 全部文件使用 Inter + Noto Sans SC | Grep 扫描 |
| 色彩一致 | 画布 #f5f5f7 / 卡片 #ffffff / 阴影 0 2px 8px | 逐文件检查 |
| 触控目标 | 主要按钮/控件 ≥ 44px | 逐文件检查 |
| vn-game 改造 | 暗色叙事风完整落地 | 视觉审查 |
| 响应式 | 360px/768px/1024px 三断点正常 | 逐文件检查 |

---

## 六、实施排期总览

| 阶段 | 任务 | 文件数 | 优先级 |
|------|------|--------|--------|
| **Phase 1** | vn-game.html 完整改造（Neumorphic→暗色叙事风） | 1 | P0 |
| **Phase 2** | 残留代码清理（creation-cabin / script-review / zhuzhi-rent） | 3 | P1 |
| **Phase 3** | DESIGN 注释更新（4 个文件） | 4 | P2 |
| **Phase 4** | branch_tree.html 微调（字体+触控+响应式） | 1 | P2 |
| **Phase 5** | 全量验收+提交+推送 | 全部 | P0 |
