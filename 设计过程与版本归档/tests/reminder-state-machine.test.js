/**
 * 宠伴·健康台账 — 提醒状态机测试
 *
 * 测试场景：验证提醒状态流转逻辑
 * 运行方式：浏览器控制台直接执行，或引入测试框架
 */

const ReminderStateMachine = {
  STATUS: {
    PENDING: 'pending',
    SNOOZED: 'snoozed',
    DISMISSED: 'dismissed',
    DONE: 'done',
    OVERDUE: 'overdue'
  },

  /**
   * 计算提醒状态
   * @param {Object} reminder - 提醒对象
   * @param {Date} now - 当前时间
   * @returns {string} 状态
   */
  calculateStatus(reminder, now = new Date()) {
    const scheduledDate = new Date(reminder.scheduledDate);
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const scheduled = new Date(scheduledDate.getFullYear(), scheduledDate.getMonth(), scheduledDate.getDate());

    if (reminder.status === this.STATUS.DONE) {
      return this.STATUS.DONE;
    }

    if (reminder.status === this.STATUS.DISMISSED) {
      return this.STATUS.DISMISSED;
    }

    if (reminder.status === this.STATUS.SNOOZED && reminder.snoozeUntil) {
      const snoozeDate = new Date(reminder.snoozeUntil);
      if (snoozeDate > now) {
        return this.STATUS.SNOOZED;
      }
    }

    if (scheduled < today) {
      return this.STATUS.OVERDUE;
    }

    return this.STATUS.PENDING;
  }
};

// ===== 测试用例 =====

function runTests() {
  const results = [];

  function test(name, fn) {
    try {
      fn();
      results.push({ name, passed: true });
      console.log(`✅ ${name}`);
    } catch (error) {
      results.push({ name, passed: false, error: error.message });
      console.error(`❌ ${name}: ${error.message}`);
    }
  }

  function assert(condition, message) {
    if (!condition) {
      throw new Error(message || 'Assertion failed');
    }
  }

  // 测试 1：计划接种日是昨天，且状态是「未完成」→ 应标记为「超期」
  test('超期提醒：计划日为昨天且未完成', () => {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    const reminder = {
      id: 'rem_001',
      scheduledDate: yesterday.toISOString().split('T')[0],
      status: 'pending'
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.OVERDUE,
      `期望 OVERDUE，实际得到 ${result}`
    );
  });

  // 测试 2：计划接种日是今天 → 应为「待处理」
  test('待处理提醒：计划日为今天', () => {
    const today = new Date();

    const reminder = {
      id: 'rem_002',
      scheduledDate: today.toISOString().split('T')[0],
      status: 'pending'
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.PENDING,
      `期望 PENDING，实际得到 ${result}`
    );
  });

  // 测试 3：已标记完成 → 保持「完成」
  test('已完成提醒：状态为 done', () => {
    const reminder = {
      id: 'rem_003',
      scheduledDate: '2025-01-01',
      status: 'done'
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.DONE,
      `期望 DONE，实际得到 ${result}`
    );
  });

  // 测试 4：稍后提醒且未到期 → 保持「稍后」
  test('稍后提醒：snoozeUntil 未到期', () => {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);

    const reminder = {
      id: 'rem_004',
      scheduledDate: '2025-01-01',
      status: 'snoozed',
      snoozeUntil: tomorrow.toISOString()
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.SNOOZED,
      `期望 SNOOZED，实际得到 ${result}`
    );
  });

  // 测试 5：稍后提醒已过期 → 应标记为「超期」
  test('超期提醒：snoozeUntil 已过期', () => {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    const reminder = {
      id: 'rem_005',
      scheduledDate: '2025-01-01',
      status: 'snoozed',
      snoozeUntil: yesterday.toISOString()
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.OVERDUE,
      `期望 OVERDUE，实际得到 ${result}`
    );
  });

  // 测试 6：已忽略 → 保持「忽略」
  test('已忽略提醒：状态为 dismissed', () => {
    const reminder = {
      id: 'rem_006',
      scheduledDate: '2025-01-01',
      status: 'dismissed'
    };

    const result = ReminderStateMachine.calculateStatus(reminder);
    assert(
      result === ReminderStateMachine.STATUS.DISMISSED,
      `期望 DISMISSED，实际得到 ${result}`
    );
  });

  // 汇总
  const passed = results.filter(r => r.passed).length;
  const total = results.length;
  console.log(`\n📊 测试结果: ${passed}/${total} 通过`);

  return results;
}

// 导出供模块化使用
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ReminderStateMachine, runTests };
}
