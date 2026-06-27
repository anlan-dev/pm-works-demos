# Demo Hub · 作品集导航页 — 架构概览

> 产品定位：面向面试官/招聘方的作品集统一导航门户，展示 13 个可交互产品 Demo。

---

## 1. 模块组成

```
┌────────────────────────────────────────────────────┐
│              Demo Hub · 作品集导航                    │
├──────────┬──────────┬──────────┬──────────────────┤
│  Hero    │  Metrics │  Filters │  Demo Grid        │
│  第一印象  │  核心指标  │  筛选标签  │  Demo 双栏卡片     │
├──────────┴──────────┴──────────┴──────────────────┤
│                   Footer（联系信息）                  │
└────────────────────────────────────────────────────┘
```

| 模块 | 职责 | 关键交互 |
|------|------|----------|
| **Hero** | 面试官第一印象：标题 + 副标题 + 渐变装饰条 | 顶部 4px 蓝紫渐变条 + 渐变文字标题 |
| **Metrics** | 4 个核心指标卡片（项目数/AI功能覆盖率/用户满意度/开发周期） | hover 上浮 4px + 阴影增强 |
| **Filters** | 按产品类型筛选 Demo（全部/工具效率/消费娱乐/企业服务/创作工具） | 圆角 20px 药丸标签，点击高亮 |
| **Demo Grid** | 双栏 Demo 卡片：左侧 200px 缩略图 + 右侧元信息 | hover 上浮 + shadow-xl |
| **CTA** | 快速入口按钮（作品集/UI设计/github） | 44px 高度，蓝紫背景 |

---

## 2. 数据流

```
页面加载 → Index 数据渲染 → 筛选交互 → 卡片更新
                ↓
           metrics[]   ← 预计算静态数据
           demos[]     ← 静态 Demo 列表（含产品类型标签）
                ↓
           筛选标签点击 → filterByType() → 过滤 demos[]
                ↓
           renderGrid() → 更新 Demo Grid DOM
```

**核心规则**：
- 纯静态数据（demos[] 在 JS 中硬编码），无后端 API
- 筛选为前端数组过滤，即时响应
- 指标数据为预计算静态值（非实时）

---

## 3. 核心数据结构

```javascript
const demos = [
  {
    id: 'pet-vaccine',
    name: '宠伴·健康台账',
    type: '工具效率类',
    stage: 'MVP验证',
    description: '宠物疫苗/驱虫/体检记录 PWA',
    tech: ['PWA', 'localStorage', 'OCR'],
    url: '../pet-vaccine.html',
    thumbnail: '...'
  },
  {
    id: 'pixelpick',
    name: 'PixelPick · AI 影像精选',
    type: '创作工具类',
    stage: 'MVP',
    description: '暗房接触印相风格 AI 优选工作台',
    tech: ['FileReader', 'Canvas API', '前端评分'],
    url: '../pixelpick.html',
    thumbnail: '...'
  }
  // ... 13 个 Demo
];

const metrics = {
  totalProjects: 13,
  activeUsers: '50+',
  aiCoverage: '85%',
  avgRating: 4.6
};
```

---

## 4. 设计决策

| 决策 | 理由 | 约束 |
|------|------|------|
| 面试官视角设计 | 核心用户是招聘方/面试官，需快速建立信任 | 需预设「面试官会问什么」，Hero 区回答了核心问题 |
| 蓝紫渐变品牌色 | 与主作品集（index.html）苹果蓝区分，建立独立的导航品牌 | 渐变在低端屏幕上可能色带，需降级方案 |
| 双栏 Demo 卡片 | 缩略图 + 文字描述 = 快速扫描 + 深入了解 | 移动端双栏缩为单列，缩略图变小 |
| 静态数据硬编码 | 导航页不需要动态数据，降低维护成本 | 新增 Demo 需手动更新 demos[] 数组 |
| 不依赖任何 CSS 框架 | 纯内联样式，确保 GitHub Pages 零依赖部署 | 样式复用性低，但导航页只需一套 |

---

## 5. 文件结构

```
demo-hub.html（单文件）
├── <style>  专业蓝紫设计系统
├── <html>   结构
│   ├── Hero（面试官第一印象）
│   ├── Metrics（4 个核心指标）
│   ├── Filters（产品类型标签）
│   ├── Demo Grid（双栏卡片列表）
│   ├── CTA 按钮组
│   └── Footer
└── <script> 筛选逻辑 + Demo 数据
```

---

## 6. 与其他项目的关系

- **上游依赖**：无。Demo Hub 是作品集的入口层，指向其他 13 个 Demo
- **设计系统**：独立蓝紫渐变体系，但与主作品集（index.html）苹果蓝保持「深→浅」的品牌关系
- **维护策略**：每新增一个 Demo，需在 `demo-hub.html` 的 `demos[]` 中新增一条记录
