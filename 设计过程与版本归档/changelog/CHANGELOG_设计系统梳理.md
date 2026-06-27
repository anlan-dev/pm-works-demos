# 设计系统梳理 — 迭代日志

> 记录 2026-06-28 全项目设计系统梳理的背景、过程与成果。

---

## 背景

截至 2026-06-27，作品集已积累 **13 个可交互 Demo**，涵盖工具效率、消费娱乐、企业服务、数据可视化等多种产品类型。但设计规范分散在：
- `设计参考/` 下的三件套（色彩/组件/交互）
- 各 Demo 内联 CSS
- `neumorphic-shared.css` 和 `dev-flow.css` 共享样式
- 8 个现有 `design-systems/*/DESIGN.md`

**问题**：
1. 新增项目（PixelPick、Mistlamp、vn-game、branch-tree、demo-hub）缺少 DESIGN.md
2. UIwork 11 个风格 Demo 缺少统一设计规范文档
3. 跨项目访问设计规范需要跳转多个文件
4. 面试场景下无法快速展示「设计系统建设能力」

---

## 2026-06-28 · 全项目设计系统梳理

### 核心改动

#### 新增 6 个 DESIGN.md

| 项目 | 路径 | 风格类型 |
|------|------|----------|
| PixelPick | `design-systems/pixelpick/DESIGN.md` | 暗房接触印相 / Apple HIG 暗色 |
| Mistlamp | `design-systems/mistlamp/DESIGN.md` | 哥特暗色文字冒险 |
| vn-game | `design-systems/vn-game/DESIGN.md` | AIGC 展示页 / 三主题切换 |
| branch-tree | `design-systems/branch-tree/DESIGN.md` | 羊皮纸手稿可视化 |
| demo-hub | `design-systems/demo-hub/DESIGN.md` | 面试官导航门户 |
| UIwork | `design-systems/UIwork/DESIGN.md` | 暗色画廊 + 11 风格规范 |

#### 更新 design-systems/README.md

- DESIGN.md 从 8 篇扩展至 14 篇（覆盖 13 个项目的 14 个 DESIGN.md，UIwork 算 1 篇）
- 新增 4 个产品分类
- 新增 2 个设计风格（暗色沉浸类、导航/门户类）
- 更新日期至 2026-06-28

### 每个 DESIGN.md 的标准结构

```
YAML frontmatter（色彩 Token / 字体层级 / 圆角 / 间距）
1. Overview（产品定位 + 设计隐喻 + 设计原则）
2. Colors（语义色 Token 表 + 使用说明）
3. Typography（字体栈 + 层级表）
4. Components（按钮/卡片/输入框/导航规范）
5. Layout（容器宽度 + 响应式断点策略）
6. Page Structure（信息架构树状图）
7. Motion（动效时长/缓动/prefers-reduced-motion）
```

### 验收标准

- [x] 14 个 DESIGN.md 全覆盖（原有 8 个 + 新增 6 个）
- [x] README.md 索引更新
- [x] YAML frontmatter 与实际 CSS 变量对齐
- [x] 每个 DESIGN.md 含完整的 Page Structure 信息架构
- [x] 与 der/模板/DESIGN_TEMPLATE.md 格式一致

---

## 全项目设计系统全景

### 六种设计风格

| 风格 | 画布 | 主色 | 代表项目 |
|------|------|------|----------|
| 工具效率类（白卡片） | `#f5f5f7` | `#0071e3` | 宠伴/会议/冷启动/Prompt |
| 消费娱乐类（品牌定制） | `#f5f5f7` | 按品牌 | 创作舱/剧本复盘 |
| 企业服务类（深蓝专业） | `#f8fafc` | `#1e4a6b` | 跨境电商 |
| 暗色沉浸类（暗房/哥特） | `#000000~#0f0e0c` | 琥珀蓝/古铜金 | PixelPick/Mistlamp/分支树 |
| 导航/门户类（蓝紫渐变） | `#fafbfd` | `#4f46e5` | Demo Hub |
| 创新实验类（11风格） | 按风格 | 按风格 | UIwork 08-11 |

---

## 经验总结

### 做得好的

1. **YAML frontmatter 先行**：机器可读，AI Agent 可直接消费
2. **与源码 CSS 对齐**：每个 Token 值都来自实际 HTML 文件
3. **设计隐喻贯穿**：暗房、手稿、展板等隐喻让设计有「故事」

### 待改进

1. UIwork 子风格（08-11）的细节规范可在独立 DESIGN.md 中展开
2. 新增项目的 dev-flow 流程条尚未创建 SVG
3. 设计系统的 Figma Token 导出待同步
