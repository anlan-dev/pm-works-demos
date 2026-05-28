# Cross-border E-commerce · 跨境电商 — 架构概览

> 本文档用最简语言回答三个问题：由哪些大块组成、大块之间怎么通信、核心数据长什么样。

---

## 1. 模块组成

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Cross-border E-commerce · 跨境电商                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                           UI 层 (Neumorphic 设计)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   聊天面板    │  │  Orchestrator │  │  Progress    │  │  Agent       │   │
│  │   (Chat)     │  │  路由面板     │  │  Compiler    │  │  Matrix      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
├─────────────────────────────────────────────────────────────────────────────┤
│                           Agent 层 (多 Agent 协同)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  选品 Agent   │  │  翻译 Agent   │  │  物流 Agent   │  │  Orchestrator │   │
│  │  (Product)   │  │  (Translate) │  │  (Logistics) │  │  (路由调度)   │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
├─────────────────────────────────────────────────────────────────────────────┤
│                           MCP 层 (服务总线)                                 │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  MCP Protocol · 消息格式 · 路由规则 · 服务注册 · 负载均衡           │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────────┤
│                           数据层                                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                     │
│  │ localStorage │  │  AI API      │  │  离线规则引擎 │                     │
│  └──────────────┘  └──────────────┘  └──────────────┘                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 模块 | 职责 | 关键交互 |
|------|------|----------|
| **聊天面板** | 用户输入与 AI 响应展示 | 为 Orchestrator 提供意图输入 |
| **Orchestrator 路由面板** | 意图识别与 Agent 调度可视化 | 调度选品/翻译/物流 Agent |
| **ProgressCompiler** | 上下文压缩与状态维护 | 长对话上下文管理 |
| **Agent Matrix** | 多 Agent 并行状态展示 | 实时显示各 Agent 运行状态 |
| **选品 Agent** | 趋势分析、竞品研究、利润计算 | 为用户提供选品决策支持 |
| **翻译 Agent** | 多语言翻译、本地化建议 | 为产品描述提供翻译 |
| **物流 Agent** | 运费计算、时效预估 | 为物流方案提供决策支持 |
| **MCP 协议** | Agent 间标准化通信 | 消息格式、路由规则、服务注册 |

---

## 2. 数据流

```
用户操作                 数据流向                     存储/处理
──────────────────────────────────────────────────────────────────
输入需求 ──────────────→ Orchestrator 意图识别 ────→ Agent 路由
                                                      ↓
Agent 调度 ─────────────→ MCP 服务总线 ──────────→ 专家 Agent
                                                      ↓
工具调用 ──────────────→ MCP 可见性控制 ──────────→ 工具执行
                                                      ↓
上下文压缩 ─────────────→ ProgressCompiler ──────────→ 状态维护
                                                      ↓
结果聚合 ──────────────→ Orchestrator 汇总 ────────→ 用户响应
                                                      ↓
状态更新 ──────────────→ Agent Matrix ────────────→ 实时展示
```

**核心规则**：
- 所有数据默认写 `localStorage`
- MCP 协议实现 Agent 间标准化通信
- Orchestrator 智能路由到专业 Agent
- ProgressCompiler 压缩长对话上下文

---

## 3. 核心数据结构

### MCPMessage（MCP 消息）

```javascript
{
  id: "msg_1694000000",
  type: "request",           // request | response | notification
  method: "product.search",  // 服务.方法
  params: {
    query: "蓝牙耳机",
    market: "US",
    category: "electronics"
  },
  timestamp: "2025-12-20T08:00:00Z"
}
```

### AgentState（Agent 状态）

```javascript
{
  agentId: "product_agent",
  name: "选品专家",
  status: "running",         // idle | running | completed | error
  currentTask: "分析蓝牙耳机市场趋势",
  progress: 0.75,
  tools: ["search", "analyze", "calculate"],
  visibility: {
    search: true,
    analyze: true,
    calculate: false
  }
}
```

### ProgressCompiler（上下文压缩）

```javascript
{
  sessionId: "session_001",
  context: [
    { role: "user", content: "帮我找蓝牙耳机" },
    { role: "agent", content: "正在分析市场趋势..." }
  ],
  summary: "用户需要蓝牙耳机选品建议，已分析美国市场",
  nextAction: "生成利润报告"
}
```

### OrchestratorRoute（路由记录）

```javascript
{
  routeId: "route_001",
  intent: "product_selection",
  confidence: 0.92,
  selectedAgent: "product_agent",
  reason: "用户明确提到选品需求",
  timestamp: "2025-12-20T08:00:00Z"
}
```

---

## 4. 关键设计决策

| 决策 | 选择 | 原因 |
|------|------|------|
| 存储方案 | localStorage | 零服务器成本，隐私优先 |
| AI 方案 | 多平台支持 + 离线兜底 | 确保基本功能可用 |
| Agent 架构 | 多 Agent 协同 | 跨境电商涉及多环节专业化 |
| 通信协议 | MCP 服务总线 | 标准化、可扩展、易维护 |
| 可视化 | Neumorphic 设计 | 作品集统一风格 |
| 响应式 | 移动端优先 | 用户优先手机端访问 |

---

## 5. Agent 协同矩阵

| Agent | 职责 | 触发条件 | 输出 |
|-------|------|----------|------|
| **Orchestrator** | 意图识别、路由调度 | 用户输入 | 路由决策 |
| **选品 Agent** | 趋势分析、利润计算 | 选品相关意图 | 产品推荐 |
| **翻译 Agent** | 多语言翻译、本地化 | 翻译相关意图 | 翻译结果 |
| **物流 Agent** | 运费计算、时效预估 | 物流相关意图 | 物流方案 |

---

## 6. MCP 可见性控制

```
┌─────────────────────────────────────────────────────────┐
│                    MCP 服务总线                          │
├─────────────────────────────────────────────────────────┤
│  工具名称      │  Agent      │  状态      │  可见性     │
├─────────────────────────────────────────────────────────┤
│  search()     │  选品 Agent  │  激活      │  ✓ 可见    │
│  analyze()    │  选品 Agent  │  激活      │  ✓ 可见    │
│  calculate()  │  物流 Agent  │  屏蔽      │  ✗ 隐藏    │
│  translate()  │  翻译 Agent  │  激活      │  ✓ 可见    │
└─────────────────────────────────────────────────────────┘
```

---

## 7. 关键实现细节

### Orchestrator 路由算法

```javascript
const routeToAgent = (intent) => {
  const intentMap = {
    'product': 'product_agent',
    'translate': 'translate_agent',
    'logistics': 'logistics_agent'
  };
  
  const detectedIntent = detectIntent(intent);
  const agentId = intentMap[detectedIntent] || 'product_agent';
  
  return {
    agentId,
    confidence: detectedIntent.confidence,
    reason: detectedIntent.reason
  };
};
```

### Agent Matrix 状态更新

```javascript
const updateAgentMatrix = (activeAgentIndex = -1) => {
  const agents = els.agentMatrix.querySelectorAll('.agent-card');
  agents.forEach((card, index) => {
    const statusEl = card.querySelector('.agent-status');
    if (index === activeAgentIndex) {
      card.style.border = '1px solid rgba(124, 58, 237, 0.5)';
      statusEl.textContent = 'RUNNING';
      statusEl.style.color = '#a78bfa';
    } else {
      card.style.border = '1px solid transparent';
      statusEl.textContent = 'IDLE';
      statusEl.style.color = '#4ade80';
    }
  });
};
```
