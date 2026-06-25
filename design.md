# 布局适配规范

> 适用范围：作品集全部页面（index.html 及各 Demo）
> 版本：v1.0 | 更新日期：2026-06-25

---

## 一、核心布局约束

### 1.1 三层溢出防护

```css
/* 第一层：文档级 */
html, body { overflow-x: hidden }

/* 第二层：容器级 */
.container { max-width: 880px; width: 100%; margin: 0 auto; overflow-x: hidden }

/* 第三层：卡片级 */
.card { max-width: 100%; overflow: hidden }
```

### 1.2 容器规范

| 容器 | max-width | 用途 |
|------|-----------|------|
| `.container` | 880px | 主内容区 |
| `.top-nav-inner` | 880px | 顶部导航 |
| 卡片内表格 | 100%（需包裹 `overflow-x:auto`） | 宽表格 |

### 1.3 Flex 子元素防溢出

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
