# Demo 上线前验证清单

每个 demo 上线前必须通过以下检查。未通过的项目必须修复。

---

## 1. 基础功能

- [ ] 核心功能可用（用户能完成主要任务）
- [ ] 所有按钮/链接可点击
- [ ] 表单提交正常
- [ ] 数据持久化正常（localStorage）
- [ ] 页面刷新后数据不丢失

---

## 2. 移动端适配

- [ ] 320px 宽度正常显示
- [ ] 375px 宽度正常显示（iPhone SE）
- [ ] 768px 宽度正常显示（iPad）
- [ ] 触摸目标 ≥ 44px
- [ ] 无横向滚动条
- [ ] 键盘弹出时页面不被遮挡

---

## 3. 性能

- [ ] 首屏加载 < 3 秒（3G 网络）
- [ ] 图片已压缩（如有）
- [ ] 无未使用的 CSS/JS
- [ ] 无阻塞渲染的资源

---

## 4. 视觉一致性

- [ ] 使用 neumorphic-shared.css（如适用）
- [ ] 颜色方案一致
- [ ] 字体大小层级清晰
- [ ] 间距规律（8px 网格）
- [ ] 圆角统一

---

## 5. 边界情况

- [ ] 空状态有提示（无数据时）
- [ ] 加载状态有反馈
- [ ] 错误状态有提示
- [ ] 长文本不破坏布局
- [ ] 特殊字符正常显示

---

## 6. 代码质量

- [ ] 无 console.log
- [ ] 无硬编码测试数据
- [ ] 无 TODO/FIXME 注释
- [ ] HTML 语义化（使用正确的标签）
- [ ] CSS 变量命名规范

---

## 7. 可访问性

- [ ] 图片有 alt 属性
- [ ] 表单有 label
- [ ] 颜色对比度 ≥ 4.5:1
- [ ] 键盘可导航
- [ ] 屏幕阅读器可读

---

## 8. 安全

- [ ] 无硬编码 API Key
- [ ] 无 XSS 漏洞（用户输入已转义）
- [ ] 无敏感信息泄露

---

## 检查方法

### 移动端测试
```bash
# Chrome DevTools
F12 → Toggle Device Toolbar → 选择设备
```

### 性能测试
```bash
# Chrome DevTools
F12 → Network → Disable Cache → Reload
```

### 代码检查
```bash
# 搜索 console.log
grep -r "console.log" *.html

# 搜索硬编码数据
grep -r "test\|demo\|example" *.html
```

---

## 快速检查脚本

在浏览器控制台运行：

```javascript
// 检查 console.log
const logs = performance.getEntriesByType('resource');
console.log('资源加载数量:', logs.length);

// 检查图片大小
document.querySelectorAll('img').forEach(img => {
  console.log(img.src, img.naturalWidth, img.naturalHeight);
});

// 检查触摸目标
document.querySelectorAll('button, a, input').forEach(el => {
  const rect = el.getBoundingClientRect();
  if (rect.width < 44 || rect.height < 44) {
    console.warn('触摸目标太小:', el);
  }
});
```

---

## 签名

| 检查项 | 检查人 | 日期 | 状态 |
|--------|--------|------|------|
| 基础功能 | | | |
| 移动端适配 | | | |
| 性能 | | | |
| 视觉一致性 | | | |
| 边界情况 | | | |
| 代码质量 | | | |
| 可访问性 | | | |
| 安全 | | | |
