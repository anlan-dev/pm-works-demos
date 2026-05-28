# 《雾灯残页》系统策划案

版本：2026-05-12  
范围：属性、状态、检定、周目推进、叙事镜头、结局分支  
关联文档：主轴与结局命名对照见 `故事概览.md` · `story_text.txt`（分流附录）；世界观与事件池见 `世界观设定集.md`；人设与矩阵见 `角色设定集.md`；周目选项与同源连线图、`clue_*` 赋值点括号叙事名见 `branch_tree.html`。

## 文案与跨职能协同（与 `text_test/text-test-usage.md`《二次元游戏文案策划面试题深度解析》对齐·摘用）

面向剧本↔系统↔演出的对齐方式，与本作双端（`script.rpy` / `text_runner.py`）同构：

- **情感目标与技术手段分离**（Q10/Q11）：接口或演出受阻时，先写下本段要送达的「情感峰值」，再在现有检定点、镜头污染、门旁白、道具文案上找替代承载；**观众记住峰值，不必记住实现手段**。

- **删减时的三问**（Q14）：删一句前问——(1) 删后剧情是否断裂，(2) 人物弧是否断裂，(3) 信息是否可迁至物品 / 档案 / Loading。设定少塞对白，多塞进告示、残页、回声。

- **CG/镜头与文案张力**：若画面与初版旁白情绪不一致，优先改语境做**二次阅读**（劫后余生的静、温柔里的刀），不轻易推翻全章（Q11）。

- **梗与 UI**：主线禁用时效网络梗；UI 与检定词条不出现道德裁决式标签（参见「终局分支原则」）。世界观内生梗优于外来梗（Q12）。

- **场面与侧面**：角色出场与关键事件须在正面信息外配**环境／细节／神态**等侧面烘托（至少两类可感、可核对），禁止无因果链的修辞硬拼；与《角色设定集》「镜头与侧面烘托」、《世界观设定集》文案方法论互证。

以上不新增程序字段，仅约束文案与验收口径。

## 系统目标
- 低数值复杂度，高叙事分歧
- 选择结果可追踪
- 结局表达“收益与代价并存”
- 同一规则可在 `script.rpy` 与 `text_runner.py` 双端复现

## 设计边界
- 属性总量控制在 5 项，避免面板膨胀
- 隐藏变量用于分流，不用于“神秘扣分”
- 每轮至少提供一次“短期收益 vs 长期代价”选择
- 每个结局都能回溯到 2-3 个关键行为锚点

## 属性
- `awareness`：信息识别
- `tenacity`：承压与牺牲能力
- `sync`：关系协同能力
- `authority`：强制决断能力
- `meta_awareness`：元叙事感知

## 状态变量
- 关系：`mika_knows_me`、`mika_bond`、`cecil_bond`、`cassius_bond`、`lucien_bond`
- 线索：`clue_truth`、`clue_shrine`、`clue_elder`、`clue_cecil`（叙事文档称 **缄卷裂真** / **七灯残阶** / **蜡誓遗册** / **暗影徽记**）
- 进度：`loop_count`、`recruited_count`
- 行为：`confronted`
- 隐藏丝线值：`thread_mercy`、`thread_obsession`、`thread_erosion`、`thread_revelation`、`scripture_mark`
- 结局记录：`endings_found`（用于多周目继承与 New Game+）

**四角色羁绊对终局的联动规则**：
| 羁绊变量 | 角色 | 主要影响结局 | 次要影响 |
|---|---|---|---|
| mika_bond | 米迦 | ASCENSION（>=2）、DAWN（>=1）、PILGRIM（>=1） | CANDLELIGHT 提权 |
| cecil_bond | 塞西尔 | CANDLELIGHT（>=1覆盖火力）、COVENANT（>=1） | CYCLE 轻度软化 |
| cassius_bond | 卡修斯 | JUDGEMENT（>=2）、AUTHOR（>=1） | — |
| lucien_bond | 卢西恩 | COVENANT（>=2）、CANDLELIGHT（>=1存活辅助） | — |

羁绊界面显示规则：未识认角色（`know_*` 为 False）显示为「？？？羁绊」；识认后显示为「（角色名）羁绊」。识认触发点为各经折初见对话（米迦 Loop1、塞西尔 Loop1 黄昏、卢西恩 Loop2 北街、卡修斯 Loop3 镇口）。

每一条羁绊至少影响两个结局入口；若四羁绊均不足，CYCLE 权重上升。

## 周目结构（7轮）
- Loop1-3：建立关系底色与线索基础，主打“信息与立场”分岔
- Loop4-5：引入镜头污染分级，角色视角开始影响叙述质感
- Loop6-7：压缩容错，提前分流概率上升
- Final：主检定 + 暗骰 + 隐藏丝线值联合结算，进入九结局之一

## 推进状态机
1. 读取当前周目状态（新开局 / 继续进度 / New Game+）
2. 执行本轮事件与选项，写入属性、关系、隐藏值增量
3. 执行检定并记录结果类型（暴击/大失败/成功/失败）
4. 执行 `early_resolution_check(stage)`（满足门槛即提前分流）
5. 若未分流，推进到下一轮；到终局轮进入 `final_resolution`
6. 结局落地后写入 `endings_found`，并触发收尾逻辑（存档清理或继承）

## 检定机制
- 主接口：`roll_check(stat_name, stat_value, difficulty)`
- 结果类型：`critical_success`、`critical_failure`、`success`、`failure`
- 暗骰接口：`meta_roll()`
- 判定顺序：先主检定，后暗骰，再合并隐藏丝线值门槛
- 文案反馈：四类结果词条必须在三端同词条（`story_text` / `script.rpy` / `text_runner`）
- **玩家可见层**：`early_resolution` 与裂隙类通知对白不宣读暗骰面值，仅播成章索引对应氛围句或 UI 副标（与 `text_runner` / `script.rpy` 同源）；策划表与分支树仍可用数值描述门槛。

## 提前分流与终局结算
- 每轮末允许提前分流，触发条件由"显性属性 + 隐藏丝线值 + 四角色羁绊 + 暗骰窗口"组成
- `AUTHOR` 入口关注：`meta_awareness`、`thread_revelation`、暗骰命中窗口、`cassius_bond >= 1`
- `PILGRIM` 入口关注：早推门行为、`scripture_mark`、轮次窗口、`mika_bond >= 1`
- `JUDGEMENT` 入口关注：`scripture_mark`、`thread_revelation`、`clue_elder`、`cassius_bond >= 2`
- `COVENANT` 入口关注：`thread_mercy`、`lucien_bond >= 2`、`cecil_bond >= 1`
- `CANDLELIGHT` 入口关注：`thread_mercy`、`lucien_bond + cecil_bond >= 1`
- `ASCENSION` 入口关注：`mika_knows_me`、`mika_bond >= 2`
- `DAWN` 入口关注：`mika_bond >= 1`
- 其余终局由主检定结果、关系状态与隐藏值综合决策
- 具体阈值以 `game/script.rpy` 为单一真值源，`text_runner.py` 逐项对齐

## 存档与周目继承
- 存档文件：`text_runner_save.json`
- 入口模式：新游戏 / 继续上次进度 / New Game+
- New Game+ 继承项：`endings_found`
- 兼容目标：旧存档缺字段时自动补默认值，不阻断读取

## 性格驱动命运（系统落地）
- 分支设计优先依据“角色性格触发的决策倾向”，其次才是事件触发
- 每个关键选项应显式对应至少一个角色性格方向（控局/共情/求真）
- 结局判定需要满足“可回溯性”：玩家能从角色在多轮中的选择习惯，推断终局偏向

## 叙事镜头系统（污染分级）
- 伴随角色镜头：`pick_companion_lens(...)` 选出当前主导视角
- 强度层级：`calc_lens_level(stage, state)` 输出 `L0 / L1 / L2`
- 文本投射：`tinted_gate_narration(stage_key, lens, level, phase)`
- 执行点位：Loop4-Loop7 关键门前后 + Final 结算段
- 目标：同一事件在不同陪同角色下，气味/触感/词面重心发生变化

## 台词差分控制（系统约束）
- 五名核心角色使用独立“禁用词 + 句长范围 + 情绪触发词”表
- 冲突场景允许语气词、停顿、断句；平静场景压低修饰密度
- 台词不得直接讲背景设定，背景信息通过动作与细节侧写外显
- 旁白与台词共同承担人物差分，避免“只靠人名换壳”

## 分支审稿清单（9条）
- [ ] 该分支是否由“角色性格”驱动，并排除“剧情巧合直推”路径
- [ ] 该分支是否至少改变一个可追踪变量（属性/关系/隐线/标记）
- [ ] 该分支的即时收益是否清晰可感（信息、关系、战术或生存）
- [ ] 该分支是否包含可见代价（关系、身体、秩序、认知至少其一）
- [ ] 该分支是否对应三轴之一（命运轴 / 个体轴 / 未知轴）
- [ ] 该分支是否能在后续文本中出现余波回响（非一次性用完）
- [ ] 该分支是否避免“绝对正确答案”表达，保留取舍张力
- [ ] 该分支是否有角色专属动作或台词锚点，避免同质化
- [ ] 该分支若删除，主线是否会失去一段独特命运路径（若不会，应重写）

## 终局分支原则（苏丹式取舍）
- 不设置“最好/最坏”结局，只设置“哲学偏向不同”的结局
- 每条终局都回答同一个问题：你选择把代价压在命运、个体，还是未知
- 终局判定以“收益与代价并存”为前提，不允许纯奖励分支
- 文案层禁止道德裁决句式（如“正确结局/错误结局”），改用“倾向/后果/余波”

### 三条哲学轴
- 命运轴：接受既定结构、改写既定结构、或被结构反噬
- 个体轴：保全自我边界、交换自我边界、或让自我被叙事吞没
- 未知轴：拥抱未知、利用未知、或拒绝未知

### 分支呈现规则
- 每个终局必须明确一个“主要偏向轴”与一个“次要代价轴”
- 结局文本需要同时给出“当下收益”与“延迟后果”
- 玩家看到的是立场选择，文本呈现采用偏向与代价标签

## 当前终局映射（九结局）
- `DAWN`：偏向个体与关系修复；代价是对深层真相的让渡 · 入径要求 `mika_bond >= 1`、主检定成功/暴击 · 若无米迦羁绊则不可入
- `CANDLELIGHT`：偏向他者存续；代价是自我持续磨损 · 入径要求 `lucien_bond + cecil_bond >= 1`、thread_mercy 偏高
- `THRONE`：偏向命运控制权；代价是关系坍缩与孤立 · 入径要求 thread_obsession 偏高（不依赖羁绊）
- `ASCENSION`：偏向未知共鸣；代价是现实锚点稀释 · 入径要求 `mika_knows_me` 为真、`mika_bond >= 2`
- `CYCLE`：偏向生存延续；代价是问题永续化 · 四羁绊均偏低时权重自动升高
- `AUTHOR`：偏向元层突破；代价是个体边界与叙事边界同时溶解 · 入径要求 `cassius_bond >= 1`、meta_awareness 高、暗骰命中
- `PILGRIM`：偏向提前行动与单人承担；代价是群体连接断裂 · 入径要求 `mika_bond >= 1`、早推门、暗骰达标
- `JUDGEMENT`：偏向审判与自我承认；代价是旧秩序不可逆损失 · 入径要求 `cassius_bond >= 2`、clue_elder 为真
- `COVENANT`：偏向共同行动与克制；代价是变革速度下降、长期负担上移 · 入径要求 `lucien_bond >= 2`、`cecil_bond >= 1`

## 变量改动来源表（按 Loop）

### Loop1
- `点头搭话，让气氛先热起来` -> `sync +1`
- `盯着锈剑看，往旧事里探` -> `awareness +1`，`meta_awareness +1`
- `把黄昏刺杀直接摊开` -> `authority +1`
- `把水壶递过去，先给一口温度` -> `sync +1`，`mika_bond +1`
- `先问报酬与口粮，把日子的账簿摊开` -> `tenacity +1`
- `在路牌背面刻一道记号（木屑沾指，掌纹发冷）` -> `thread_revelation +1`，`thread_erosion +1`
- 剧情分支（非菜单）会写入 `clue_cecil = True`，且部分路径附加 `authority +1`
- 固定推进：`recruited_count +1`，`loop_count +1`

**`text_runner.py` 终端版（Loop1 附加流程，与引擎剧情同构）**：`loop_one` 在米迦村口主菜单 **`choose("LOOP ONE …")` 之前**会先跑 `run_week_dialogues(state, 1)`。村口主菜单前以体感、关系与争盐冲突为主；盐税告示全文与「北街／巷口／旧墨」三路指名长引导改在 **`loop_two` 章首**读出（与 `game/script.rpy` 一致），避免信息堆在首轮选项前；`run_week_dialogues` 内 `loop_no==1` 仍只补**一句短接引**扣回**口授七夜**。口授节律内每日三选项来自 **`VOICE_LIBRARY`**，条目前缀 **`角色名｜`**，经 **`constrained_voice_block()`** 过机。**主答句**由 **`WEEK_SAY_ROTATION`** 按日轮换（同 mood 连日选也不复述同一句）；**第一周** `team_reaction_line` 仅允许「照面日早于当前日」的队友具名目（前两日只有环境旁白）；塞西尔／卢西恩／卡修斯**首次担主声日**前先播 **`week1_first_contact_scene`**；**`daily_rpg_feedback`** 按 `week_day` 取桥接与尾评语，勿总读列表首条。**日内小事件旁白**：`run_week_dialogues` 在每向分支前依次为 **`第 N 天`**、**`DAILY_MICRO_EVENT_RULES`**（七章×七日，按 `know_mika/know_cecil/know_cassius/know_lucien` **子集**择句：**需求集合越大越优先**；未到识认门槛则**不具名同桌**，仅以路人碎语／谣传为照面预埋）、当日 **`WEEK_DIALOGUE_PACKS` focal**。改选项、Rotation 或日内规则表须与 `story_text.txt`**「口授七夜」**节（与终端横幅用词一致）互链。**世道长句后移**（检定后或下一轮章首）详见 `story_text.txt` 各 Loop「世道」拆条与本文 Loop2–Loop6 检定位置。

### Loop2
- `跟着我` -> `tenacity +1`
- `你身边有刺客` -> `awareness +1`，`clue_truth = True`，`clue_cecil = True`
- `拿锈剑开一句玩笑` -> `sync +1`，`tenacity +1`
- `去街角和塞西尔聊` -> `sync +2`，`cecil_bond +1`，`clue_cecil = True`
- `提黑水河的梦` -> `awareness +1`，`mika_bond +1`（且可写入 `mika_knows_me`）
- `让塞西尔在巷口试射一箭（黄铜门环先闷响一记，胸口那口气才松下半寸）` -> `thread_mercy +1`，`thread_obsession +1`
- 检定 `roll_check("坚韧", tenacity, 12)` 会按结果追加 `mika_bond`（暴击通常 `+2`，成功通常 `+1`）
- 固定推进：`recruited_count +1`，`loop_count +1`

### Loop3
- `对米迦说，跟我来` -> `sync +1`
- `带他去旧神殿` -> `awareness +1`，`clue_shrine = True`
- `聊他炉火砖缝里那点私藏和旧事` -> `tenacity +1`，`mika_bond +1`
- `去看卡修斯带来的法术书` -> `cassius_bond +1`，`clue_elder = True`
- `提河对面的梦` -> `awareness +1`，`mika_bond +1`（且可写入 `mika_knows_me`）
- `把轮回真相说到明面` -> `authority +1`，`tenacity +1`（且可写入 `mika_knows_me`）
- `让卡修斯读你掌心旧裂纹（呼吸短停，指骨发凉）` -> `thread_revelation +1`，`thread_erosion +1`
- 检定 `roll_check("同步", sync, 12)` 会按结果追加 `mika_bond`（暴击通常 `+2`，成功通常 `+1`）
- 固定推进：`loop_count +1`

### Loop4
- `问米迦，记得我吗` -> `tenacity +1`
- `去神殿看戒指` -> `awareness +1`，`clue_shrine = True`
- `谈公告牌上的字` -> `meta_awareness +1`，`authority +1`
- `找塞西尔和旧书` -> `cecil_bond +1`，`lucien_bond +1`，`clue_elder = True`
- `认下执印遗裔之名` -> `authority +1`，`mika_knows_me = True`（依脚本）
- `把救人这件事摊开讲` -> `sync +1`，`tenacity +1`，`mika_bond +1`
- `替米迦包扎旧伤（布条吸血，心口回暖）` -> `thread_mercy +1`，`sync +1`
- 检定 `roll_check("坚韧与并肩", tenacity + sync, 12)` 会按结果追加 `mika_bond`（暴击通常 `+2`，成功通常 `+1`）
- **逆写时刻**：若 `thread_erosion >= 2`，奈尔在检定后无意漏嘴说出不该知道的信息（裂谷坐标/前哨年份），米迦首次警觉「他比我们多活过」，奈尔咽回答案；`thread_revelation +1`
- 固定推进：`loop_count +1`

### Loop5
- `问米迦记不记得那些梦` -> `mika_bond +1`（且可写入 `mika_knows_me`）
- `去找最后一扇门` -> `awareness +1`，`clue_truth = True`，`clue_shrine = True`
- `和米迦谈条件` -> `tenacity +1`，`mika_bond +1`（且可写入 `mika_knows_me`）
- `先找卡修斯` -> `cassius_bond +1`，`authority +1`
- `带所有人进神殿` -> `sync +1`，`tenacity +1`，`recruited_count +1`
- `直接带线索去旧庭要塞` -> `authority +1`，`awareness +1`，`clue_truth = True`
- `把门槛上的灰抹在掌心（回声贴掌背呢，腕底脉门自己发沉）` -> `thread_obsession +1`，`thread_revelation +1`
- `今夜就推门，不再多等（经句压进喉间，决断提前）` -> `authority +1`，`thread_obsession +1`，`scripture_mark +1`
- `再观一轮风向，延后推门（先听风，再动手）` -> `tenacity +1`，`meta_awareness +1`，`thread_mercy +1`
- **冲突锚 C1（卢西恩退队危机）**：灰原兵变伤员潮→神殿阶前四重伤三双手；卢西恩放弃轻伤员转向前哨老兵，米迦质问「你放弃了那一个」，卢西恩不应——止血带折四层按进奈尔掌心。`lucien_bond +1`，`thread_mercy +1`，`thread_obsession +1`
- 固定推进：`loop_count +1`

### Loop6
- `让卢西恩再查一次伤口（药酒苦橙味，时间感反向）` -> `thread_mercy +1`，`tenacity +1`，`lucien_bond +1`
- `把七灯教义读给米迦听（教义一句句落地，你跟米迦的呼吸才慢慢对上）` -> `scripture_mark +1`，`sync +1`，`meta_awareness +1`
- `逼问卡修斯裂谷坐标（他应声时像在交付一把会烫伤手的钥匙）` -> `awareness +1`，`authority +1`，`thread_obsession +1`
- `于圣所列像座前的誓石边，折断旧钥匙（断裂声里，同时有退让与抬头）` -> `thread_erosion +1`，`thread_revelation +1`
- `再等最后一轮（把门边的余地留给还没说完的话）` -> `thread_mercy +1`，`mika_bond +1`
- `立刻开门（夜还深，门先回应你）` -> `authority +1`，`scripture_mark +1`
- 检定 `roll_check("坚韧与并肩", tenacity + sync, 12)` 参与后续分流判定
- **冲突锚 C2（塞西尔vs卡修斯）**：钟楼下针锋相对——塞西尔主张「坐标先拿」，卡修斯主张「读前须备」。选项②③对应站边，写入 `_loop6_sided`（字符串：cecil/cassius）
- **冲突锚 C3（米迦终止动议）**：若 `mika_bond >= 2`，米迦在选项后质问「我们这一次能赢吗」——不是问句是门；奈尔咽回答案。逆写时刻（S1）升级；`mika_knows_me = True`
- 固定推进：`loop_count +1`

### Loop7
- `为米迦系紧护腕（布条勒紧时，他把额头抵过来一瞬）` -> `thread_mercy +1`，`sync +1`，`mika_bond +1`
- `把自己的名字写进封蜡（蜡油先咬住指腹发烫，疼了半拍，才把名字按实）` -> `thread_revelation +1`，`scripture_mark +1`，`authority +1`
- `让卡修斯朗读禁章（字音刮过墙皮，灰线就扑簌掉点渣）` -> `meta_awareness +1`，`thread_erosion +1`，`scripture_mark +1`
- `沉默推门（门轴替你开口）` -> `tenacity +1`，`awareness +1`
- **冲突锚 C4（全员后退一步）**：若选「沉默推门」且 `_loop6_sided` 非空——被站边的角色后退一步，让出奈尔前方的路。站塞西尔→退箭离弦；站卡修斯→搁笔撕经注。无台词，后退即回答。
- 固定推进：`loop_count +1`

### Final（终局段）
- 主检定：`roll_check("坚韧与并肩", tenacity + sync, 12)` 与暗骰共同决定分流
- 关键入口：
  - `AUTHOR`：`meta_awareness` 与 `thread_revelation` 达标，且暗骰命中窗口
  - `PILGRIM`：早推门关联轮次 + `scripture_mark` 达标，且暗骰达标
  - 其余结局：由 `thread_mercy / thread_obsession / thread_erosion / thread_revelation`、显性属性与检定结果联合决定
- 结局落地时写入：`endings_found.append(<ENDING_ID>)`
- 收尾分支的 `最后抉择`（如并肩离开 / 留下断后 / 再入轮回）会决定落入的具体结局编号

## 内容同步与验收
- 同步基线文件：`game/script.rpy`、`text_runner.py`、`story_text.txt`、`branch_tree.html`
- 同步要求：结局正文、判词词条、分流说明三类文本保持同源
- **文案禁令（硬性）**：凡对上述基线文件**新增、改写或由模型生成的叙事/系统面向玩家的中文**，**在合入主干前都必须**运行 `python tools/copy_guard_check.py`；以 **exit code 0** 为放行条件。**禁止**仅以「语感看过」跳过；若工具误报除外，须在 PR/提交说明写明理由并同步调整规则。
- 文案回扫：与上条同一命令（含全件禁令、`game/script.rpy` 固定词条正/负向校验；详见 `tools/copy_guard_check.py` 头部说明）
- 运行验收：
  - `python -m py_compile text_runner.py`
  - `ReadLints` 检查改动文件
  - 抽查九结局在 `branch_tree` 的摘要版/全文版一致性

## 文案回扫固定清单
- 运行自动回扫：`python tools/copy_guard_check.py`（script.rpy 必含短语 + 口径禁用项见工具内常量）；**每一条**由人或模型写出的补丁，均以「本命令 exit 0」为收束，不靠记忆里的禁令复述。
- 若命中规则，先修正文案，再次回扫直到通过
- 同步四个口径文件：`game/script.rpy`、`text_runner.py`、`story_text.txt`、`branch_tree.html`
- 语感复核：台词有情绪起伏与动作承接，段落包含画面/声音/气味/触感信息
- 备份更新：将本轮核心文案文件复制到 `archive/recovery/`，文件名使用时间戳
- 更新日志：在 `DEVELOPMENT_LOG.md` 记录回扫结果与同步范围

## 同步基线
- `game/script.rpy`
- `text_runner.py`
- `story_text.txt`
- `branch_tree.html`
