# 布局适配规范

> 适用范围：作品集全部页面（index.html 及各 Demo）
> 版本：v1.1 | 更新日期：2026-06-26

---

## 一、核心布局约束

### 1.1 三层溢出防护

```css
/* 第一层：文档级 */
html, body { overflow-x: hidden }

/* 第二层：容器级 */
.container { max-width: 780px; width: 100%; margin: 0 auto; overflow-x: hidden }

/* 宽屏收紧（≥1400px） */
@media (min-width: 1400px) {
  .container { max-width: 760px }
}

/* 第三层：卡片级 */
.card { max-width: 100%; overflow: hidden }
```

### 1.2 容器规范

| 容器 | max-width | 用途 |
|------|-----------|------|
| `.container` | 780px（≥1400px 时 760px） | 主内容区 |
| `.top-nav-inner` | 780px | 顶部导航 |
| 卡片内表格 | 100%（需包裹 `overflow-x:auto`） | 宽表格 |

### 1.3 间距规范（PC 端舒适阅读）

| 元素 | 间距值（clamp） | 说明 |
|------|----------------|------|
| `.container` padding | `clamp(32px, 4vw, 52px)` 上下 / `clamp(16px, 4vw, 32px)` 左右 | 容器外围留白 |
| `.section-title` top margin | `clamp(40px, 5.5vw, 56px)` | 大段落间距，明确分隔 |
| `.section-title` bottom margin | `clamp(16px, 2.5vw, 24px)` | 标题与内容间距 |
| `.section-title` bottom border | `1px solid rgba(0,0,0,.06)` + padding | 视觉分隔线 |
| `.card` padding | `clamp(22px, 3.2vw, 32px)` | 卡片内留白 |
| `.card` margin-bottom | `clamp(18px, 2.5vw, 24px)` | 卡片间距 |
| `.card` border | `1px solid rgba(0,0,0,.08)` | 淡淡的边框 |
| `.card` box-shadow | `0 2px 12px rgba(0,0,0,.06)` | 轻阴影 |
| `.step` margin-bottom | `clamp(12px, 1.8vw, 16px)` | 步骤间距 |
| `.step` gap | `clamp(10px, 1.4vw, 14px)` | 序号与内容间距 |
| `.card-sub` margin-bottom | `clamp(14px, 2vw, 22px)` | 副标题与内容间距 |
| `.divider` margin | `clamp(32px, 4.5vw, 44px)` | 分隔线上下间距 |
| `.footer` margin-top | `clamp(32px, 5vw, 48px)` | 页脚上方间距 |
| `.step-text` line-height | `1.7` | 正文行高，提升可读性 |
| `body` line-height | `1.47059` | 全局行高 |

### 1.4 Flex 子元素防溢出

```css
/* flex 子元素必须设 min-width:0 以允许收缩 */
.step { display: flex; min-width: 0 }
.step-body { flex: 1; min-width: 0 }
.harness .hstep > span:last-child { flex: 1; min-width: 0 }
```

---

## 二、响应式断点

| 断点 | 宽度 | 设备 | 关键适配 |
|------|------|------|----------|
| **mobile** | ≤ 640px | 手机 | 单列布局、字号缩小、flow-badge 换行 |
| **tablet** | 641–820px | 平板 | 隐藏右侧 TOC、显示抽屉菜单 |
| **desktop-sm** | 821–1120px | 小桌面 | TOC 右侧固定、容器加大右 padding |
| **desktop** | > 1120px | 大桌面 | 默认布局 |
| **ultrawide** | ≥ 1400px | 2K/4K 宽屏 | 容器收窄至 760px，确保阅读舒适度 |

---

## 三、文字防溢出规则

### 3.1 允许的操作（仅针对文本元素）

```css
.step-text, .card-sub, .card-title, .arch-box, .quote, .ft-list li,
.harness .hstep > span:last-child, .comp-value, .result, .gate-table td,
details summary, details summary > div {
  overflow-wrap: break-word;
  word-break: break-word;
}
```

### 3.2 禁止的操作

| 禁止写法 | 原因 |
|----------|------|
| `* { overflow-wrap: break-word }` | 通配符应用会破坏 flex/grid 布局的最小宽度计算 |
| `* { word-wrap: break-word }` | 同上，且 word-wrap 是废弃属性 |
| `* { hyphens: auto }` | 通配符连字符会影响所有元素的文本渲染 |
| `.step-body { overflow: hidden }` | 会干扰 flex 子元素的尺寸计算，导致布局异常 |
| `word-break: break-all` | 过于激进，会在任意字符处断行（URL/数字场景除外） |

---

## 四、表格与代码块

### 4.1 宽表格

```css
/* 包裹层 */
.table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch }

/* 表格本身 */
table { width: 100%; border-collapse: collapse }

/* 移动端表格可设 white-space:nowrap 整体滚动 */
@media (max-width: 640px) {
  .gate-table { display: block; overflow-x: auto }
}
```

### 4.2 代码块

```css
pre, code {
  overflow-x: auto;
  white-space: pre-wrap;  /* 允许换行 */
  word-break: break-word;
  max-width: 100%;
}
```

---

## 五、Flow Badge（流程指示器）

```css
/* 桌面端：单行显示 */
.flow-badge { display: inline-flex; white-space: nowrap }

/* 移动端：允许换行 */
@media (max-width: 640px) {
  .flow-badge { white-space: normal; flex-wrap: wrap }
}
```

---

## 六、新增模块检查清单

新增卡片或模块时，逐项检查：

- [ ] 卡片是否在 `.container` 内
- [ ] 卡片是否有 `max-width: 100%`
- [ ] flex 子元素是否设 `min-width: 0`
- [ ] 长文本元素是否加 `overflow-wrap: break-word`
- [ ] 表格是否包裹在 `overflow-x: auto` 容器中
- [ ] 是否有 `white-space: nowrap` 的元素在窄屏下可能溢出
- [ ] 是否有内联 `width` 超出容器宽度
- [ ] 移动端（≤640px）是否验证过无横向滚动条

---

## 七、踩坑记录

### 2026-06-25：全模块宽度溢出

**现象**：独立项目及之后所有卡片占满整个屏幕宽度
**根因**：`* { overflow-wrap: break-word }` 通配符规则破坏了 flex 布局的最小宽度计算
**修复**：
1. 移除 `* { overflow-wrap: break-word }` 通配符
2. 仅对文本元素应用 `overflow-wrap: break-word`
3. 移除 `.step-body { overflow: hidden }`（保留 `min-width: 0`）
4. 添加 `html { overflow-x: hidden }` 作为文档级安全网

**教训**：永远不要用通配符 `*` 应用 `overflow-wrap`、`word-break`、`hyphens` 等影响文本换行的属性。这些属性会改变元素的最小内在宽度（min intrinsic width），导致 flex/grid 布局计算错误。

### 2026-06-26：PC 端视觉密度过高

**现象**：PC 宽屏下卡片内容填满容器，各版块缺乏留白，视觉拥挤
**根因**：880px 容器在 1920+ 宽屏上占比过大（约 46%），卡片 padding/margin 不足
**修复**：
1. 容器 max-width 从 880px → 780px，≥1400px 时进一步收紧至 760px
2. 卡片 padding 从 `clamp(18px,2.8vw,28px)` → `clamp(22px,3.2vw,32px)`
3. 卡片 margin-bottom 从 `clamp(14px,2vw,20px)` → `clamp(18px,2.5vw,24px)`
4. section-title 增加底部边框分隔线 + 加大上下 margin
5. step-text line-height 从 1.6 → 1.7
6. 所有间距 clamp 值整体上调约 20-30%

**教训**：内容宽度不只是"不溢出"就够了——在宽屏设备上，窄容器 + 大留白才能创造舒适的阅读体验。780px 是经过验证的"黄金阅读宽度"（约 65-75 个中文字符/行）。
