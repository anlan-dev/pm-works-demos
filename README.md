# Demo 开发日志（复盘用）

每个可交互 Demo 有独立 Markdown 日志：**时间在顶部、新记录置顶**。改 UI / 交互 / 文案 / 口径时，顺手追加一行，便于面试前复盘与版本对齐。

**约定**

1. 编辑某个 `*.html` 后，打开对应的 `dev-logs/<同名>.md`，在「## 记录」下**最上方**新增一条，格式见各文件头部说明。
2. **作品集迭代记录**：各 Demo 日志中的 **「## 作品集迭代记录（与 index.html 同步）」** 与主站 `index.html` 设计文档卡里「📜 查看完整迭代历史」一致；**改主站时请同步改对应 md 本节**（也可用 `dev-logs/_extract_index_iterations.py` 从主站抽取对照）。
3. 新拟物样式集中在 `neumorphic-shared.css`；`dev-flow` 条在 **`html data-ui="neumorphic"`** 时与之一致，见 `dev-flow.css` 文末。
4. 作品集主站 `index.html` 仍使用页内 Neu 段；逻辑上与本目录 token 一致，日志见 `index-portfolio.md`。

**文件索引**

| 日志文件 | 对应页面 |
|----------|----------|
| `pet-vaccine.md` | `pet-vaccine.html` |
| `meeting-ruminant.md` | `meeting-ruminant.html` |
| `creation-cabin.md` | `creation-cabin.html` |
| `script-review.md` | `script-review.html` |
| `cold-start.md` | `cold-start.html` |
| `prompt-library.md` | `prompt-library.html` |
| `zhuzhi-rent.md` | `zhuzhi-rent.html` |
| `demo-hub.md` | `demo-hub.html` |
| `index-portfolio.md` | `index.html` |
