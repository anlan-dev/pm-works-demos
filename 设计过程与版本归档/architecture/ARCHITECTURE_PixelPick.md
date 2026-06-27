# PixelPick · AI 影像精选 — 架构概览

> 产品定位：面向专业设计师/摄影师的 AI 影像优选工作台，批量上传 → Best 评分 → 放大镜对比 → 一键导出。

---

## 1. 模块组成

```
┌──────────────────────────────────────────────────────┐
│              PixelPick · AI 影像精选                    │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ 上传模块  │ 分析引擎 │ Best 精选 │ 对比预览  │ 导出模块 │
│ (Upload) │ (AI      │ (Best    │ (Loupe   │ (Export) │
│          │  Scoring)│ Select)  │ Compare) │          │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│                  状态管理 (App State)                  │
├──────────────────────────────────────────────────────┤
│  Contact Sheet 网格渲染  │  胶片齿孔进度条 (Film Strip) │
└──────────────────────────────────────────────────────┘
```

| 模块 | 职责 | 关键交互 |
|------|------|----------|
| **上传模块** | 支持拖拽/点击上传多张图片，文件格式校验（JPEG/PNG/WebP） | 预览缩略图生成，进入分析队列 |
| **分析引擎** | 对每张图片计算 4 维度评分（构图/曝光/对焦/色彩），综合 Best Score | 纯前端计算，不依赖后端 API |
| **Best 精选** | 自动标出最高分图片，展示评分 + 入选理由 + 维度细分 | ★ 标记 + 蓝色边框 + 精选横幅 |
| **对比预览** | 支持放大镜悬停、图片切换对比 | Hover 波纹动效 + 全屏放大 |
| **导出模块** | 一键导出精选集（支持按评分筛选） | 单张/批量下载 |
| **Contact Sheet** | 自适应网格渲染缩略图，模拟暗房接触印相排版 | CSS Grid auto-fill |
| **Film Strip** | 5 步进度条（上传→分析→精选→对比→导出），当前步高亮 | 蓝色发光 notch + 绿色完成态 |

---

## 2. 数据流

```
用户操作                    数据流向                      状态
──────────────────────────────────────────────────────────
拖拽/选择图片 ──────→ FileReader → 缩略图生成 ──→ appState.images[]
                                                    ↓
AI 评分 ────────────→ 4 维度分析 → Best Score ──→ image.score
                                                    ↓
Best 精选 ──────────→ 按 score 排序 → 标记 best ──→ image.isBest
                                                    ↓
对比预览 ────────────→ 切换 activeImage ──────────→ appState.activeId
                                                    ↓
导出 ────────────────→ 筛选 bestIds → 下载/复制 ──→ 完成
```

**核心规则**：
- 所有处理纯前端（FileReader + Canvas API），图片不离开浏览器
- Best Score = 构图×0.3 + 曝光×0.25 + 对焦×0.25 + 色彩×0.2（前端模拟算法）
- 进度条状态嵌入 appState，驱动 UI 自动切换

---

## 3. 核心数据结构

### Image（单张图片）

```javascript
{
  id: 'uuid',
  fileName: 'DSC_0001.JPG',
  fileSize: 2457600,       // bytes
  dimensions: { w: 4000, h: 3000 },
  thumbnail: 'data:image/jpeg;base64,...',
  score: {
    total: 87,              // 0-100
    composition: 90,        // 构图
    exposure: 85,           // 曝光
    focus: 82,              // 对焦
    color: 91               // 色彩
  },
  isBest: false,
  reasons: ['黄金分割构图', '色彩饱和度优秀'],
  analyzedAt: 'ISO日期'
}
```

### AppState（全局状态）

```javascript
{
  step: 1,                  // 1-5: 上传/分析/精选/对比/导出
  images: [],
  bestId: null,
  activeId: null,           // 对比预览当前
  filter: 'all',            // all | best | unrated
  gridMode: 'grid'          // grid | list
}
```

---

## 4. 设计决策

| 决策 | 理由 | 约束 |
|------|------|------|
| 纯前端评分算法 | 演示 Demo 不依赖 AI API，离线可用，零成本 | 评分非真实 AI 推理，需在产品说明中标明 |
| 暗房接触印相隐喻 | 摄影行业熟悉 contact sheet，降低学习成本 | 需在 UI 中保持一致术语（Print/Contact Sheet/Darkroom） |
| Apple HIG 暗色规范 | 专业工具类产品主流，减少长时间使用眼疲劳 | 需在亮色环境下测试可读性 |
| 进度条 5 步线性 | 摄影工作流线性特征（选→评→筛→比→出），不可逆 | 支持返回上一步但不跳过 |
| 4:3 缩略图比例 | 与 DSLR/微单原生比例一致，减少裁切信息丢失 | 手机竖拍（3:4）可能裁切，需 fallback |

---

## 5. 文件结构

```
pixelpick.html（单文件）
├── <style>  内联样式 · 暗房设计系统
├── <html>   结构
│   ├── Header（暗房门牌）
│   ├── Film Strip（5步进度）
│   ├── Upload Zone（拖拽上传）
│   ├── Best Banner（精选横幅）
│   ├── Contact Sheet（缩略图网格）
│   ├── Loupe Modal（放大镜对比）
│   └── Toolbar（筛选/视图切换）
└── <script> 逻辑
    ├── FileReader 缩略图生成
    ├── Scoring 模拟评分引擎
    ├── Best 算法排序
    ├── Grid 渲染 + 懒加载
    └── Export 下载
```

---

## 6. 与其他项目的关系

- **设计系统**：独立暗色体系（#000000 + #0071e3），不与 neumorphic-shared.css 耦合
- **AIGC 能力**：评分引擎为前端模拟算法，未来可接入真实视觉 AI API（如 Google Vision / Replicate）
- **作品集定位**：展示「从用户场景出发设计工具」的 PM 能力，而非 AI 技术深度
