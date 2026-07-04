# ============================================
# Mistlamp Fragments - Rebuilt Script
# ============================================

init python:
    def roll_check(stat_name, stat_value, difficulty):
        dice = renpy.random.randint(1, 20)
        total = dice + stat_value
        if dice == 20:
            return (dice, stat_value, total, True, "critical_success")
        elif dice == 1:
            return (dice, stat_value, total, False, "critical_failure")
        success = total >= difficulty
        result_type = "success" if success else "failure"
        return (dice, stat_value, total, success, result_type)

    def meta_roll():
        return renpy.random.randint(1, 20)

    EARLY_RESOLUTION_RESONANCE_LINES = [
        "门缝里漏进一线的亮，像有人在低声校对还没落款的句子。",
        "你后脑像被薄纸划过，回声忽然贴骨——却数不清那是第几声。",
        "夜里有人把窗纸按平，你连自己的心跳都显得太响。",
        "风在某个转角改口，像把下一章提前塞给你半页。",
        "铁与木轻轻碰了一下，像提醒你别装听不见。",
        "冷光先落在你的指腹上，像有人在等你摁下去才肯承认。",
        "你忽然闻见旧墨发潮的气味，像在说你早该翻开那一折。",
        "雾里一声极细的裂响，像是纸边上有人折了一下指甲又停住。",
    ]

    def early_resolution_whisper(loop_count_val):
        idx = max(0, min(loop_count_val - 1, len(EARLY_RESOLUTION_RESONANCE_LINES) - 1))
        return EARLY_RESOLUTION_RESONANCE_LINES[idx]

    SHOW_STATS_BRIDGES = [
        "又一折落在命册纸脊上——你先把这一序的分量在舌底掂匀。",
        "钟槌未举，风里已有人替你数过下一息的利息。",
        "脚尖仍踏着旧石板，骨节却像在另一格里落印——你心里该把这一轮昼夜排位了。",
    ]

    def fate_message(result):
        if result == "critical_success":
            return "命运的丝线一下拉紧，像有人在耳边轻轻弹拨琴弦。"
        if result == "critical_failure":
            return "命运的丝线当场崩断，碎响贴着后颈划过。"
        if result == "success":
            return "命运的丝线缓缓收束，耳侧像掠过一根低钝的弦响。"
        return "命运的丝线松开半寸，风从偏斜的缝里灌进来。"

    def fate_message_lines(result):
        return "【丝线回响】" + fate_message(result)

    TR_ROLL_REVEAL = {
        "critical_success": "门内先传来一声亮响，像有人替你把锁舌拨开。",
        "critical_failure": "掌心一空，门内回声忽然退远，像潮水离岸。",
        "success": "石缝轻轻松了一口气，冷风肯进来半寸。",
        "failure": "门石仍紧，回声在缝里打了个转，又退回黑处。",
    }

    def terminal_roll_intro(stat_name, result):
        return "【命运检定·%s】%s" % (stat_name, TR_ROLL_REVEAL[result])

    def pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority):
        scores = {
            "mika": mika_trust,
            "cecil": cecil_bond,
            "cassius": (1 if clue_elder else 0) + authority // 2,
            "lucien": thread_mercy // 2,
            "neutral": 0,
        }
        lens = max(scores, key=scores.get)
        if scores[lens] <= 0:
            return "neutral"
        return lens

    def calc_lens_level(stage, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority):
        level = 0
        if stage >= 5:
            level = 1
        if stage >= 7:
            level = 2

        pressure = meta_awareness + thread_revelation + scripture_mark + thread_erosion + authority // 2
        if pressure >= 8:
            level = min(2, level + 1)
        elif pressure <= 2:
            level = max(0, level - 1)
        return f"L{level}"

    def tinted_gate_narration(stage_key, lens, level, phase="entry"):
        table = {
            "loop4_gate": {
                "neutral": "旧殿门前风带湿灰和旧蜡；袖口一蹭，霉冷就贴上来。",
                "mika": "旧殿门前，米迦先把你往后拨了半步，像在拦一口看不见的刃；掌心那点热意短短一蹭，却足够把整块冷石烫出一声很轻的回音。",
                "cecil": "旧殿门前，塞西尔先量角度再量人——弓弦只颤一下，杂音像被一刀切齐，你连自己的呼吸都显得太阔。",
                "cassius": "旧殿门前，卡修斯眼皮几乎不眨，指尖沿门缝刻纹划过——他在记哪道缝能侧身，哪道会绊住踝骨。",
                "lucien": "旧殿门前，卢西恩把一卷药布拍得极平铺在臂弯，草药、酒精与苦橙混在一起，硬是把石灰的死冷拖回人间一寸。",
            },
            "loop5_gate": {
                "neutral": "最后一扇门缝里吐出来的风含着铁盐和旧血干涸后的腥甜，像在低声练一句你尚未学会发音的誓词。",
                "mika": "你看那扇门。米迦喉间轻轻一滚像是笑，却只笑出半截；鞋底在石板上悄悄前移半寸，像给自己多垫一层底。",
                "cecil": "你看那扇门。塞西尔把肩线收成一条冷静的切线，吐字很轻，像在雪上刻路线——哪一步可先走，哪一步得把脚后跟钉住。",
                "cassius": "你看那扇门。卡修斯把术式手稿扣在掌心，焦墨与冷汗混成一痕；他念的每个字都带着刀背凉意，却仍把『怎么活』写在你看得见的行距里。",
                "lucien": "你看那扇门。卢西恩数完四个人呼吸才敢抬灯，火苗往门槛一侧偏——像把『还能退半步』这回事，交到你们发烫的瞳孔里。",
            },
            "loop6_gate": {
                "neutral": "雾把台阶打湿，你话没说完就被湿气冲淡，后半截堵在胸口。",
                "mika": "雾厚得能咬住舌根，米迦仍硬挤出两声干笑：声儿不大，像在哄雾里那只从未露面的兽别醒。",
                "cecil": "雾压得檐角滴水如钟，塞西尔自己站到最风口，衣袖纹丝不动——像把整座镇的怯都挡在他肩线这一侧之外。",
                "cassius": "雾里，钟楼方向传来一声空洞的回音残片，卡修斯报数像报丧，却又报得四平八稳——仿佛愈冷愈准的路线才配叫生路。",
                "lucien": "苦橙药酒味从袖口浮上来，像在提醒血液仍是热的。卢西恩把止血带的松紧卡在『疼但还能走路』的那一格里，不多说一个字。",
            },
            "loop7_gate": {
                "neutral": "第七轮的门前静得可耻——不叫不泣，只有把冷一点一点楔进掌心骨缝的那种安静。",
                "mika": "门轴不响，米迦却把护腕勒到发白，呼吸先乱了一拍又被他生生咬回去——像怕自己一出声就会把夜撕破。",
                "cecil": "门不响，塞西尔先为你们排稳步距——手势冷得像尺，却比任何高喊都更像一句『我在』。",
                "cassius": "封蜡裂开细纹，蜡泪像迟缓的血。卡修斯盯着那点裂，仿佛在等一行脚注自己站起来反咬执笔的人。",
                "lucien": "所有人的脉他终于肯点头：可以前进——那不是庆祝，是一句把恐惧拆成可操作步骤的手术口令。",
            },
            "final_gate": {
                "neutral": "你把掌心贴上门石——冷先钉进骨头，轰鸣迟一步才从远处追上来。",
                "mika": "你掌心贴上门石的一刻，身后米迦吐了口又长又涩的气，把那堆没骂出口的慌与狠一并咽回肚里烧成热度。",
                "cecil": "你贴上门石时，耳边掠过塞西尔最后一次方位词，轻得像羽，落在地上却是一圈可守的弧线。",
                "cassius": "你贴上门石时，听见卡修斯把代价从头到尾又念了一遍，每个音节像在逼你数数：这趟账，你还有几个铜子舍得押。",
                "lucien": "卢西恩的指腹最后停在你腕侧那一下很轻，却比门更先告诉你——心还在跳，就还配谈『下一步』。",
            },
        }
        intensity_entry = {
            "L0": "门前景物还清楚，指腹却沾上一层细墨粉。",
            "L1": "你抬眼时呼吸先乱了半拍——气味比人影先到。",
            "L2": "门前景物随着他的习惯改摆，连风声都像踩他的拍子。",
        }
        intensity_post = {
            "L0": "冷意照旧铺开，像一张还没人签名的判词。",
            "L1": "你再度抬眼，重心不觉偏了半寸，像被谁从旁轻推了一下。",
            "L2": "再看周遭，灰里浮尘都像带着同一句话。",
        }
        event = table.get(stage_key, {})
        base_line = event.get(lens, event.get("neutral", ""))
        tail_map = intensity_post if phase == "post" else intensity_entry
        return f"{base_line}{tail_map.get(level, '')}"


define narrator_voice = Character(None, what_italic=True)
define mika = Character("米迦")
define cecil = Character("塞西尔")
define cassius = Character("卡修斯")
define lucien = Character("卢西恩")
define you = Character("你")


# ----- ATTRIBUTES -----
default awareness = 0
default tenacity = 0
default sync = 0
default authority = 0
default meta_awareness = 0

# ----- FLAGS -----
default loop_count = 0
default clue_cecil = False
default clue_truth = False
default clue_shrine = False
default clue_elder = False
default recruited_count = 0
default mika_knows_me = False
default confronted = False
default mika_trust = 0
default cecil_bond = 0
# ----- HIDDEN THREAD VALUES (player invisible) -----
default thread_mercy = 0
default thread_obsession = 0
default thread_erosion = 0
default thread_revelation = 0
default scripture_mark = 0
default companion_lens = "neutral"
default lens_level = "L0"

# 与 text_runner 「口授」门闸对齐：奈尔已记入脸孔与声线的同伴。
default know_mika = False
default know_cecil = False
default know_cassius = False
default know_lucien = False


label start:
    scene black
    with dissolve
    # 叙事备忘：开场——灯影、门响轮次、信息战三嘴，勿改节奏堆成说明文

    narrator_voice "灯影先落在指节上，墨迹未干；你还来不及把这一夜读顺，它已逼迫你改口。"
    narrator_voice "第七次门响之前，名字会被重写，誓言会换押，代价沉在胃里，像石块。"
    narrator_voice "轮回把愿望折成账页；页角潮了，指腹一蹭就是凉。"
    narrator_voice "告示、口传和经卷常常各说各话——信息的真与假从来不对账。谁先把它钉成『事实』，谁的灯就先亮一格；擦掉的那一行，夜里会换措辞回来找你。"
    narrator_voice "肉身穿洞未必到头；等记忆被抽走、名字在簿子上淡成墨迹，下一轮村口的风刮在脸上，你未必认得出自己的脚步。"
    narrator_voice "推门念禁句，替人挡刀——账上不记白欠。换回权柄或多喘一晚，失去的却常是平静与信任。"
    narrator_voice "世上的悲剧也常后到——巨响落下来之前，多半是鞋带磨脚、半句话堵在心口。"
    narrator_voice "两套说辞若咬死同一桩旧事，先别急着替世界重写真相；你为听信哪一种声音，就得认哪一种疼。"
    narrator_voice "若想笑出声，只管借职务里的老话，或边境酒鬼的歪谚——别让短命的俏皮掺进路基，经不起几夜潮气。"
    narrator_voice "……这些是你踏进风口前还记得的活法。余下的，风里一件件验。"
    "（按任意键开始）"
    pause

    jump loop_one


label show_stats:
    $ _stats_bridge = renpy.random.choice(SHOW_STATS_BRIDGES)
    narrator_voice "[_stats_bridge]"
    narrator_voice "经折第[loop_count + 1]序 — 命册五蕴：觉察[awareness] 坚韧[tenacity] 同步[sync] 权能[authority] 元认知[meta_awareness]"
    return


label early_resolution_check(stage):
    $ m = meta_roll()
    $ core_score = awareness + tenacity + sync + authority + meta_awareness
    $ hidden_score = thread_mercy + thread_obsession + thread_erosion + thread_revelation + scripture_mark
    $ gate = 20 - stage

    if m < gate:
        return

    $ _early_resonance = early_resolution_whisper(loop_count)
    narrator_voice "[_early_resonance]"

    if thread_revelation >= max(1, stage - 2) and meta_awareness >= 1 and m >= 18:
        narrator_voice "你在第[stage]轮失手坠入裂隙的更深处——墨色书页自顾自哗然翻开，仿佛在挑选下一任读者。"
        jump ending_author

    if stage >= 6 and scripture_mark >= 3 and thread_revelation >= 4 and m >= 15:
        narrator_voice "第[stage]轮，百灯齐昂，百千喉咙同诵一节经文——世界突然变得太吵又太亮。"
        jump ending_judgement

    if stage >= 6 and thread_mercy >= 4 and sync >= 2 and m >= 14:
        narrator_voice "第[stage]轮，门框未攫走任何一息——你先刀背对内，戾气倏然退潮。"
        jump ending_covenant

    if thread_obsession >= (stage // 2 + 1) and (authority + meta_awareness) >= 2:
        narrator_voice "第[stage]轮你已握住王冕的冷牙，它含笑先咬住你脚底的影子不放。"
        jump ending_throne

    if thread_mercy >= (stage // 2 + 1) and (sync + mika_trust) >= 2 and core_score >= stage + 2:
        narrator_voice "第[stage]轮耳畔炸开彼此心跳如雷——那轰鸣替你宣读了不必出口的神殿裁断。"
        jump ending_sacrifice

    if thread_erosion >= (stage // 2 + 1) and core_score <= stage + 6:
        narrator_voice "第[stage]轮夜色将你的足迹抹去如拭墨，指针悄然归回最初一格。"
        jump ending_eternal

    if core_score + hidden_score >= (8 + stage * 2):
        if mika_knows_me:
            narrator_voice "你在第[stage]轮便把姓名与命运叠成一枚蜡印——门后有光，路旁亦布荆棘。"
            jump ending_ascension
        narrator_voice "第[stage]轮提前谢幕，石灰纷扬如终审落屑，晨光却蛮横抢先泻入。"
        jump ending_true

    return


# ============================================
# LOOP ONE
# ============================================
label loop_one:
    call show_stats

    narrator_voice "你站在村口。"
    narrator_voice "所以你先让指腹在袖口内侧那道旧裂上蹭一记：皮肉先认了疼在前，紧接着舌根才泛起一口冷铁似的涩——身体又比记忆里早半步说，付账快到了。"
    narrator_voice "疼落下来，你便不敢松那根束发黑绳：绳结死死咬住发尾，松一手就像承认这条托养线也能被名册涂销。"
    narrator_voice "于是下摆系带你便多打一个半扣，褶子卡住；说不上真能挡什么，只像替「名字还属于自己」又多挂了一颗小秤砣。"
    narrator_voice "风里告示纸脚翻起一寸，你习惯先咬最远署名与年月；边角读清了，视线才敢让给路牌下边那人——米迦冲你笑，笑里有烟火气，也有一点困意压着眼尾。"
    narrator_voice "漆面老得一吹就掉粉，落屑沾在他肩线上；你听远处鸡笼木门梆的一声短——短促利落，你便知道村里还有人忙着喂畜，日子过得不像要塌。"
    narrator_voice "你便叫奈尔。银发和红眼是先声；比这更锋利的一条记性，是你记得自己在这条路上死过很多次——所以这一轮你站在这儿，从来不是散步。"
    narrator_voice "路牌底下的闹剧先炸开来：有人正为半袋药盐掰腕，税吏哨子还没来得及咬紧，两只手便把麻袋扯裂，白线在撕扯里发亮——被点名的那一个却还活着：米迦，棕发，绿眼，腰上锈剑更像发冷的旧铁；他本人却比铁热，命与钱都要紧，还有一副能把恐惧说成希望的嗓子。"
    narrator_voice "米迦横插一步，锈剑往木栏上一靠，护手磨圆的绳结先于刃口顶住你眼帘：他握紧时指腹先碰的是家事捻出来的那一圈温，才敢把笑话当盾牌。"
    narrator_voice "护腕上暗褐旧布毛糙发褐，闻起来像熬过无数炉边裸麦糊的余温仍未散尽，缠着一口不肯谢幕的热。"
    narrator_voice "笑骂着把两只手腕各拍开半寸：松手再吵，谁先见血谁替全镇付账。"
    narrator_voice "那一声笑骂把火药味卸了半截。他回头挑眉像在邀功；笑意没落稳，眼珠又飞快掠过你侧脸一记，像在问这轮打趣有没有剐到人。"
    $ oral_register("mika")
    mika "诶——旅人？头回见吧。荷包里要是还有余钱，我能帮你少跑三趟冤枉路。"
    $ oral_entry_day = oral_run_week(1)
    $ _oral_wb = oral_week_bridge(1, oral_entry_day)
    narrator_voice "[_oral_wb]"

    menu:
        "点头搭话，让气氛先热起来":
            you "唔，算是。"
            mika "那我就不客气了。手头有点空，你这口水递得比神谕实在。"
            narrator_voice "他笑得很亮，眼尾却藏着一层没睡好的青影。"
            $ sync += 1

        "盯着锈剑看，往旧事里探":
            you "你这把剑，啧，像是从棺材边上捞出来的。"
            mika "说得好听一点，它叫历战老伙计。说得直白一点，啧，它还真有点掉渣。"
            narrator_voice "他把剑抽出半寸，锈末先钻进鼻腔；柄缠死死顶住虎口不动，指腹得沿绳股往里捋一寸家事捻熟的旧温，刃口才肯再吐出冷铁的一线腥。"
            $ awareness += 1
            $ meta_awareness += 1

        "把黄昏刺杀直接摊开":
            you "黄昏会有刺客来找你。信我。"
            mika "你这开场够硬。像铃还没响，先把刀摆上桌。"
            narrator_voice "他笑意淡了，手指压上剑柄，指节在暮光里绷出浅白。"
            $ authority += 1
            $ confronted = True

        "把水壶递过去，先给一口温度":
            you "先喝口水。"
            mika "你这人怪好。平时这口水递过来，后面总跟着一张账单呢。"
            narrator_voice "他接过水壶时指尖擦过你的手背，那点热意短短一瞬，像烛火蹭过冷玻璃。"
            $ sync += 1
            $ mika_trust += 1

        "先问报酬与口粮，把日子的账簿摊开":
            you "你哪位神明给过你行旅银？"
            mika "给了个称号响亮得很，可就是没给一枚铜子——哎。"
            narrator_voice "他说这话时坦坦荡荡，连穷都显出一点理直气壮。"
            $ tenacity += 1

        "在路牌背面刻一道记号（木屑沾指，掌纹发冷）":
            narrator_voice "你用指甲在路牌背面刻下一道细痕。木屑沾在指腹，像一层冷灰。"
            narrator_voice "那道痕咬得浅，指腹却仍蹭得到木纹吸进去的一点糙；凉意贴着，很久不肯散。"
            $ thread_revelation += 1
            $ thread_erosion += 1

    narrator_voice "黄昏一落，你便往暮色里寻人：影子先被拉长；旧殿方向巡铃应声敲了两遍，你听惯了那两道铃之间的距离，脚步声便压着它落下来。"
    narrator_voice "铃声落地，你便看见他背弓走近，脚步压得轻极了，像在替全队把呼吸按进土里；笑意先落下来，肩颈却不肯松。"
    narrator_voice "抬眼看人前，他先把你与落日之间的空地量成一道可停的缝：弓仍含臂弯里，指腹沿鞘槽拂过，像在擦净一声多余的回响。"
    narrator_voice "袍角下摆沾夜露；内侧针脚细得几乎看不见，逆光里才浮出一线旧徽轮廓，像把身份缝进褶里又不想真藏住。"
    narrator_voice "他在你与落日之间落定脚跟：浅沟沿线，不偏不倚；弓弦离掌心恰好两指，够一声弦响就能把所有人都拽停。"
    narrator_voice "腰侧极小磨石袋随步伐轻轻撞上大腿外侧，系带勒得死板；袋里石粉的淡腥让人记起箭一旦离弦就收不回第二张脸。"

    $ oral_register("cecil")

    if confronted:
        cecil "嗯……他说得对。"
        narrator_voice "他应声时眉眼仍温润，肩颈却先于笑容冷硬——像在刀背上铺了一层薄冰。"
        mika "诶，你哪位？"
        narrator_voice "米迦侧身半步挡在你前襟与来人弓弦之间，锈剑虽未出鞘，虎口已咬住柄缠，绿眼睛眯成两道不肯退让的刃。"
        cecil "……原本来杀你的。字面意思。"
        narrator_voice "紫瞳里波澜不惊，指腹却沿弓梢轻轻下滑半寸——不是安抚你，是把距离量成可反应的格。"
        you "你这次会停手。"
        narrator_voice "你开口时声带发紧；他听见那点紧，眼尾极轻地一抽——你喉间憋着的那半口气竟跟着肩头同松一毫，像两人误触到同一条回声。"
        cecil "奈尔，你知道得不少。别绷太紧——唔，弓我先放低。"
        narrator_voice "他的紫眼睛停在你脸上，冷得像贴骨的金属。"
        $ clue_cecil = True
        $ authority += 1
    else:
        mika "这位看着像会射箭的。跟我一把，先活过今夜再说。"
        cecil "那就同行。唔——步距让给我半步，前段警戒我来。"
        you "唔，他跟着。"
        narrator_voice "塞西尔看了你一眼，没有反驳。他指尖拨了拨弓弦，腰侧极小磨石袋随之轻撞；袋里石粉细震沾上指腹一抹凉腥，那股淡腥就把教官旧课上「落土好过落喉」一句推回舌根——不必数数，也够让人咽一口。"
        $ clue_cecil = True

    $ recruited_count += 1
    $ loop_count += 1
    call early_resolution_check(loop_count)
    jump loop_two


# ============================================
# LOOP TWO
# ============================================
label loop_two:
    call show_stats

    narrator_voice "你又醒了。"
    narrator_voice "昨宵村口的风里告示早翻过面：《盐道重税令》把药盐车逼去绕道；《北境冬补给失踪案》的流言却比马蹄先到——酒馆外护路兵对词，名册与账本仍留着刺眼空白。空白既刺眼，清早的风便替你指路：北街缝线的是卢西恩，药酒味常驻袖口；巷口迟早遇得到背弓量距的守夜人，袍边往往缝着褪色的看守团徽。旧墨甜味若先飘过镇口，多半便是学团旅法：卷册先响，名字等人自报。"
    narrator_voice "湿气既上来，鞋底便先黏在石缝里；你还在找立足点，路牌下边米迦已发呆良久，指尖绕着剑柄慢慢转圈。"
    narrator_voice "你往井那边偏头——井水还凉着，塞西尔却更早半步蹲在沿上擦弓弦。他眼底那点亮稳得像尺子，像在等谁先沉不住气、先抬头应声。"
    narrator_voice "往北街再借半步，帘里苦橙药酒与皂角先缠在一处；你循味找声，才看见担架旁的医师收针。指尖稳得像装订册页；黄铜与木柄轻轻一碰——谣传里的人声，从此有了可对上的骨相。"
    $ oral_register("lucien")
    narrator_voice "他侧身让出半步廊荫，潮雾里先亮的是铜盘与肩线；靴筒软垫把踝托起半分，站姿仍习惯性地朝伤病那一侧前倾。"
    narrator_voice "抬眼之前，他不动声色把你与米迦的呼吸各默数了一遍，才把「还能不能喘匀」这句话留进自己喉间。"
    lucien "借过。脉案还没落款呢——有话先到荫里说。唔……别把热气喷到旁人那一息上。"
    $ oral_entry_day = oral_run_week(2)
    $ _oral_wb = oral_week_bridge(2, oral_entry_day)
    narrator_voice "[_oral_wb]"

    menu:
        "跟着我":
            you "脚跟稳一点，跟着我走；别问路先问鞋底。"
            mika "行，钟敲你手里了。我让拍子，你让风向。"
            narrator_voice "他吐出一口气，像在把骨子里的懒与怕各推出一寸。"
            $ tenacity += 1

        "你身边有刺客":
            you "别回头太勤；你那影子里至今还掖着匕尖。"
            mika "一句话把我脊背晾在风口上了……行，我今日信你一回邪。"
            cecil "旅人没有夸大。只是我今日把刀刃朝内折了，嗯。"
            narrator_voice "塞西尔仍踞在井沿没挪步；擦弦声早停了。他接话时没有回头，声音却贴着凉井沿升起来，落进你们二人中间。"
            $ awareness += 1
            $ clue_truth = True
            $ clue_cecil = True

        "拿锈剑开一句玩笑":
            you "坊间传说你这剑单次只削得下半片魂；我猜是鞘太寒碜，刃口都不好意思探出头。"
            mika "听好了：不是剑穷，是人生穷。就这半片魂的豁口，也够替你我挡一枪冷箭。"
            narrator_voice "他笑得发抖，肩胛却悄悄松了一点点。"
            $ sync += 1
            $ tenacity += 1

        "去街角和塞西尔聊":
            cecil "咦，又是你——先靠墙，三下呼吸，想清楚哪一句是真正要紧的。"
            narrator_voice "他用弓梢轻点身后的石面，像在替你划出三步内唯一安全的三角；胸口起伏贴着你视线边缘，却仍把脸转向灯影更薄的一侧。"
            you "我不要讨吉利话，要你许我改写这一页死因。"
            narrator_voice "话音落地，他指尖在弦槽停了一息——不是犹豫，像在把弦上的颤压到你的句子下面。"
            cecil "钱袋不必打开。凶险讲全——唔，我就把『可能』俩字听进去。"
            narrator_voice "他抬眼的那一瞬紫光极浅，却比任何誓词更像承诺；唇角的薄笑没有加深，只是把刀背朝内转了半分。"
            $ sync += 2
            $ cecil_bond += 1
            $ clue_cecil = True

        "提黑水河的梦":
            you "黑水河上有人反复喊你。"
            mika "你……你连我木碗里最后那点挂壁的咸湿都闻着？"
            you "河岸对面立着的一直是我。"
            narrator_voice "他喉结剧烈一滚，像把一口冰咽得太急，眼角却腾地热了。"
            $ awareness += 1
            $ mika_trust += 1
            $ mika_knows_me = True

        "让塞西尔在巷口试射一箭（黄铜门环先闷响一记，胸口那口气才松下半寸）":
            cecil "退半步——数到三也别回头。"
            narrator_voice "箭啸短得像一句被腰斩的诗，砰地楔进远门环，黄铜抖出一圈残响。"
            narrator_voice "箭啸戛然而止，黄铜门环犹在颤鸣；你先觉肩窝里麻意退去一针宽，胸膛那圈无名绷紧才跟着泄下半格，像终于被允许换一口气。"
            $ thread_mercy += 1
            $ thread_obsession += 1

    narrator_voice "天色沉得像浸了水的墨，再浓一点就要淌下来。"
    narrator_voice "夜里神殿门前的风总爱迟半拍到；撩起衣袂，把火光揉成碎红点。"
    narrator_voice "旧殿檐下设着旅舍庖间赊来的条凳与外租木桶，麦酵气裹着醋渍河鲜的卤水；摊主依榷簿把肉刃上的最后一粒粗盐刮回瓮里，才把缺口陶碗推到石沿边。"
    lucien "汤里漂过雾海港的鱼干，我只尝一勺。余下的热浆归你们续火——谁也别指着伤兵名录，多偷舀一勺蛋白，嗯？"
    mika "那股腌渍味儿在心底顶着喉咙，苦。榷吏影子还横在石阶上呢。爹妈沿河省下来的晶屑，全塞在炉火砖缝里那一盅——我总不能站在石阶上，叭叭泼进半桶麦酒里糟蹋掉。"
    cecil "守夜干粮袋我多勒了半扣。盐在你们嘴里要起争——唔，我这弦会先抖给你看，它比嘴诚实。"
    you "掰下的黑面包屑里夹着两三颗粗晶，我搁在掌心数清了才敢咽。舌根先浮铁腥，咽下去喉咙发紧。"
    $ dice, bonus, total, success, result = roll_check("坚韧", tenacity, 12)
    $ _tri_l2 = terminal_roll_intro("坚韧", result)
    narrator_voice "[_tri_l2]"
    $ fate_msg_full = fate_message_lines(result)
    narrator_voice "[fate_msg_full]"
    $ fate_msg = fate_message(result)
    $ renpy.show_screen("fate_notify", fate_msg, "口里铁腥味落定：[dice]+[bonus]=[total]")

    if result == "critical_success":
        mika "成……这一回我把命字写你名字边上了，奈尔。别给我瞎涂改。"
        $ mika_trust += 2
    elif success:
        mika "懂不全，也不怕。脚后跟先替你抬一步；你说往西，我今日先不往东。"
        $ mika_trust += 1
    elif result == "critical_failure":
        mika "停。今日这张嘴张太阔，我给你缝半针，省得风向跟着你跑偏。"
    else:
        mika "让我喘三口。信与不信各占一半；那一半我等你自己递过来。"

    narrator_voice "舌根那根弦松下去，耳朵里才腾出空去听墙里旧账：旧殿走廊封了一截，抄本误译把封条点爆，回声在石里刮了整夜。"
    narrator_voice "镇口巡防桌上堆满蜡印文书——一半催干净报告，一半想把名册黑花押闷死在里面。"

    narrator_voice "夜里你在神殿门口等到了塞西尔。门柱上还粘着旧殿看守团的残封条。"
    narrator_voice "米迦抱臂靠墙，下颌朝门内一撇，像在帮你把问号先递进去；火光在他睫毛上跳着，绿眼睛却仍盯着你口唇，等你落声。"
    mika "他怎么说？"
    narrator_voice "你说话时霜气从口里呵出；他听见了，喉咙轻轻一动，像在替你把寒意咽下去半截。"
    you "他留下。"
    narrator_voice "米迦肩头那道绷了一整夜的线忽然塌半寸，又立刻用笑意撑回去——笑纹浅得像怕惊动门里的蜡；他仍借火光扫你半眼，确认没把轻松演成薄情。"
    mika "那行。人多一口气，也多一盏灯。"

    $ recruited_count += 1
    $ loop_count += 1
    call early_resolution_check(loop_count)
    jump loop_three


# ============================================
# LOOP THREE
# ============================================
label loop_three:
    call show_stats

    narrator_voice "第三次醒来，头里像压着潮水。"
    narrator_voice "潮声还在耳蜗里打转，你便往镇口望——那儿果然多了一个旅人：卷册贴在肋侧，走一步拍一下，像替谁数心跳里漏掉的那一拍。"
    narrator_voice "扣子收到顶还不够，黄铜夹又胡乱夹住几缕蹿出的红发；你便多看一眼，猜他是怕错漏从领口先冒出来。"
    narrator_voice "然后他摘下手套，纸页与药草的苦香先替他报上来路；开口短，落点硬——卡修斯。"
    narrator_voice "他看你一眼，目光从额角滑到指尖，像在核对抄本缺了哪一行落款；指腹蹭过手记焦黑的一角皮绳——那晚条文与伤口同时见血，后来他再也不肯把这一条系松。"
    narrator_voice "镇公所门槛上摊着一本泡湿的抄本。卡修斯把页角按平，指节只敲一行：这里缺了半句经注；缺的半句今夜会换人一条命。"
    narrator_voice "他咽下一口不知从哪舀来的冷茶，胃脘无声地拧紧，却仍把最重的那几个词整整齐齐码在舌尖上。"
    narrator_voice "文书嘴唇发白。米迦喉结动了一下，先扯出笑：学者吵架我围观，真拔刀再喊我。"
    narrator_voice "卡修斯没接茬。他把学团徽记翻过去扣在案上，像扣住一枚不想让人读正面朝上的币。"
    $ oral_register("cassius")
    $ oral_entry_day = oral_run_week(3)
    $ _oral_wb = oral_week_bridge(3, oral_entry_day)
    narrator_voice "[_oral_wb]"

    menu:
        "对米迦说，跟我来":
            you "跟上。掉队的人连灰都不配吃热的。"
            mika "行行行，今日听你喊拍子；我管腿，你管往哪儿蹚。"
            narrator_voice "他答得爽快，眼底却浮着一层压不平的疑问。"
            $ sync += 1

        "带他去旧神殿":
            you "神殿今日会裂开一口窗；信不信由你，潮气会先教你低头。"
            mika "行啊，闻着就像闹鬼的冰窖。走，谁先腿软谁先叫对方爷爷，嗯？"
            narrator_voice "风掠过路旁枯草，细碎的窸窣声贴着靴底爬过去。"
            $ awareness += 1
            $ clue_shrine = True

        "聊他炉火砖缝里那点私藏和旧事":
            you "你小时候把钱藏在炉灶与外墙砌筑夹层里的暗影中。"
            mika "你到底翻了我多少底啊？"
            narrator_voice "他嘴上发狠，耳根却先热了，像火星落在冷铜上。"
            $ tenacity += 1
            $ mika_trust += 1

        "去看卡修斯带来的法术书":
            cassius "啧，抄本上只登应验的，不登好听话。"
            you "那它也不肯把我的死期抹成逗号。"
            narrator_voice "他把书页合上，羊皮纸的旧甜味在空气里慢慢散开。"
            $ cecil_bond += 1
            $ clue_elder = True
            $ clue_cecil = True

        "提河对面的梦":
            you "黑水河里那个人，每次都看着你。"
            mika "我看不清脸。可水那边一直有人站着。"
            narrator_voice "他的声音压得很低，像怕一抬高就把那条河从梦里惊出来。"
            $ awareness += 1
            $ mika_knows_me = True
            $ mika_trust += 1

        "把轮回真相说到明面":
            you "这是第三次。前两次你都死了。"
            mika "那你……每次都在？"
            narrator_voice "他说出口时没有笑，那张总带油滑的脸忽然清了，只剩下冷静和一点发紧的呼吸。"
            $ authority += 1
            $ tenacity += 1
            $ mika_knows_me = True

        "让卡修斯读你掌心旧裂纹（呼吸短停，指骨发凉）":
            cassius "这道口子每天在往里收拢半分。再拖两轮就翻不回来；到那时你连灶灰潮不潮都未必记得住。"
            narrator_voice "他指尖很冷，像把一枚细针压在皮肤上。"
            narrator_voice "你听见自己呼吸慢了半拍。"
            $ thread_revelation += 1
            $ thread_erosion += 1

    $ dice, bonus, total, success, result = roll_check("同步", sync, 12)
    $ _tri_l3 = terminal_roll_intro("同步", result)
    narrator_voice "[_tri_l3]"
    $ fate_msg_full = fate_message_lines(result)
    narrator_voice "[fate_msg_full]"
    $ fate_msg = fate_message(result)
    $ renpy.show_screen("fate_notify", fate_msg, "两腔呼吸对上拍了：[dice]+[bonus]=[total]")

    if result == "critical_success":
        mika "好——算上这回第三遍了。这话我认了。"
        narrator_voice "他把手伸过来，掌心有剑柄磨出来的硬茧，热得像活火。"
        $ mika_trust += 2
        $ mika_knows_me = True
    elif success:
        mika "行，我先跟。后头你再慢慢讲……嗯，我听着。"
        narrator_voice "那层嬉皮笑脸的壳薄了很多，风一吹就像会裂。"
        $ mika_trust += 1
    elif result == "critical_failure":
        mika "你先别说了。"
        narrator_voice "你喉咙发苦，肺里像塞进一团湿透的灰。神殿铜锈味一下子呛上来。"
    else:
        narrator_voice "他看着你，很久都没有出声。高窗里的风吹下来，发出尖细的低鸣。"

    narrator_voice "你把胸口悬着的气呼尽了，白昼里粘在耳背的碎话才算成行：雾港在传遗物拍卖夜，围堵撕开一道口子，人仍从缝里漏得出去；雾里有人压得极低地笑半声，辨不清庆贺还是吓唬自己。"
    narrator_voice "灰原车棚那边的闲话更稠：哗变草草收场，私兵补缺接岗，羊皮纸上三色界线被擦掉又重写，指腹蹭过去却仍摸得到底下渗着一层旧痕。"

    narrator_voice "临走前，米迦又问了一次你的名字。"
    you "奈尔。"
    mika "记住了。下次别把我落在门后。"

    $ loop_count += 1
    call early_resolution_check(loop_count)
    jump loop_four


# ============================================
# LOOP FOUR
# ============================================
label loop_four:
    call show_stats
    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(4, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)

    narrator_voice "第四次醒来，舌根有淡淡血腥味。"
    narrator_voice "你抬手时看见影子变薄，阳光从指缝穿过去，地上像铺一层快要熄灭的银尘。"
    narrator_voice "石阶下摆开两盏小灯：一盏照着听证抄本，一盏照着还没拆线的胳膊。苦橙药酒味先漫上来，先把廊下的喧哗按低半衔。"
    narrator_voice "卢西恩蹲在光与影的缝上，指下还在数脉，声线平得发紧。"
    narrator_voice "触脉以前，他已把廊下沸声暗自裁成两段呼吸的长度：先教人喘匀，再许人吵。"
    if not know_lucien:
        $ oral_register("lucien")
    else:
        narrator_voice "北街认得的那缕淡金与灰绿又回来了：他照旧先指腹触脉门，才把石阶灯影里的争执交回你们唇齿之间。"
    lucien "血先止住，再高抬争辩——不迟。唔，纸上的名姓，也不跟着嗓门高低改。"
    narrator_voice "他抬眼只看你们一瞬，又把干净药包塞进兵丁手里；对方接手时指节一缩，像接了半截推不掉的差事。"
    $ oral_entry_day = oral_run_week(4)
    $ _oral_wb = oral_week_bridge(4, oral_entry_day)
    narrator_voice "[_oral_wb]"
    $ tinted_line = tinted_gate_narration("loop4_gate", companion_lens, lens_level, "entry")
    narrator_voice "[tinted_line]"

    menu:
        "问米迦，记得我吗":
            you "记得我吗？"
            mika "记得一点。梦一样，醒了还扎手。"
            narrator_voice "他说这句时下眼睑红得透着干痕，风里盐粉似的细末起在他睫毛边角；手背忙里偷闲蹭过眼尾一记，才敢把那点湿按回去。"
            $ tenacity += 1
            $ mika_knows_me = True

        "去神殿看戒指":
            mika "上次我在神殿里找到了这个。"
            narrator_voice "戒指嵌在他掌心，锈色把皮肤都染成暗红。上面的刻痕摸上去像裂开的骨。"
            $ awareness += 1
            $ clue_shrine = True

        "谈公告牌上的字":
            you "公告牌上写了规则。每一回都在改。七灯教义的旧符号也被人重描过。"
            mika "我看不见。哎，可你说出来以后，我后背还是发冷。"
            narrator_voice "木板在风里轻轻晃，像有谁隔着另一层雾在上面划字。"
            $ meta_awareness += 1
            $ authority += 1

        "找塞西尔和旧书":
            cecil "你又比夜色先来。唔，好——早到一寸，伤员多换一刻钟。"
            you "因为这次该结束。"
            narrator_voice "卢西恩的药箱就放在台阶下，草药味压住潮石灰味，盖住一半听证用的墨臭。"
            narrator_voice "他把银针在灯焰上过一遍，叮当两下短而硬，压得廊下半格喧哗退去；你听清自己心跳落回肋骨里才敢再抬眼。"
            narrator_voice "铜扣有一道旧撞痕，开合只剩闷闷的一响——他留着那声钝，像在告诉伤者：我还能抓稳这一箱，你便还有下一句话。"
            lucien "手腕给我。另一只手——别去摸门框。震颤会骗人，脉不会，嗯？"
            narrator_voice "他系止血带时用齿咬紧布尾，腾出指尖在你手背敲了两下：一下叫停，一下叫放行。"
            lucien "行了。去看你的旧书。唔……别顺手再揣几个要缝的窟窿回来。"
            $ cecil_bond += 1
            $ clue_elder = True

        "认下执印遗裔之名":
            you "执印在我。旧统这一脉，议会早把账记在我名下了。"
            mika "执印都挂你名下了……旧统那笔账还不够你扛？还来替我挡这一下——你图啥啊。"
            narrator_voice "他嘴角抖了一下，没有拔剑，只有呼吸重了，热气带着一点铁味。"
            $ authority += 1
            $ mika_knows_me = True

        "把救人这件事摊开讲":
            you "我把话摊在桌上：每一趟，我都是冲着你还能喘气才往回走的。"
            mika "这话……你早该说了。"
            narrator_voice "那句埋得太久的话终于出了口，像压在井底的石头被人生生拖上来，水声冷得发颤。"
            $ sync += 1
            $ tenacity += 1
            $ mika_trust += 1
            $ mika_knows_me = True

        "替米迦包扎旧伤（布条吸血，心口回暖）":
            narrator_voice "你把布条一圈圈缠紧。布面吸了血，慢慢发暗。"
            mika "你这手法太熟。布一过伤口，疼都知道往哪退。"
            $ thread_mercy += 1
            $ sync += 1

    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(4, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)
    $ tinted_line = tinted_gate_narration("loop4_gate", companion_lens, lens_level, "post")
    narrator_voice "[tinted_line]"

    $ dice, bonus, total, success, result = roll_check("坚韧与并肩", tenacity + sync, 12)
    $ _tri_l4 = terminal_roll_intro("坚韧与并肩", result)
    narrator_voice "[_tri_l4]"
    $ fate_msg_full = fate_message_lines(result)
    narrator_voice "[fate_msg_full]"
    $ fate_msg = fate_message(result)
    $ renpy.show_screen("fate_notify", fate_msg, "肩与肩咬住同一力道：[dice]+[bonus]=[total]")

    if result == "critical_success":
        narrator_voice "他完全信了。那点默契回到你们之间，疼得像旧伤重新见风。"
        $ mika_trust += 2
    elif success:
        narrator_voice "他没有再追问。那把锈剑压回鞘里，摩擦声干涩得像一声叹息。"
        $ mika_trust += 1
    elif result == "critical_failure":
        mika "今天我只当你被夜风晃了神，先不跟你算。"
        narrator_voice "那层吊儿郎当的笑重新扣回他脸上，像一张临时缝好的面具。"
    else:
        narrator_voice "他盯你到眼眶发涩，却仍不肯吐出一个『肯』字；烛焰偷垂泪，蜡的苦味蛇一样爬上舌。"

    narrator_voice "肩背与肩线叠实的那一瞬，石阶上白昼没咽下去的那场争吵才又回到喉间——学团与看守团整夜撕扯医誓，修院要救人，档案馆要封存，各有各的蜡绳。卢西恩的名字被写进了听证名册：赭墨水淌过装订绳结，在那儿洇开一个迟迟不肯干的斜印。"
    narrator_voice "还有一纸坏消息从谈判桌上炸开：七城契约失手，粮仓按手印按日放粮；领麦子的人低头按指印，旁边另有一支行款笔并排落下看守的名。"
    narrator_voice "连焦墨与铁灰搅在一起的那股呛味你都认得。胃里先于脑子翻出次数：这又是第几回在石廊熬过同一宿。"

    cecil "你打算怎么办？"
    narrator_voice "他问得极简，下巴却略微收紧；紫眼睛里映着你的轮廓，像在把你这句话刻进下一轮站位里。"
    cassius "别死我眼前。真要补脚注——啧，一回就够我胃难受了。"
    narrator_voice "红发垂落遮去半只眼，他却不抬手拨；羽笔在稿边敲了一下，墨点溅成一颗不肯化开的痣。"
    you "跟之前一样。走到最后。"
    narrator_voice "廊柱后铜盘轻轻一碰，银针落水似的极短一声。你知道卢西恩在听脉，却把审判权塞回你们自己手里。"
    narrator_voice "卡修斯没有再续话，只把掌心那点法火轻轻掠灭。"

    $ loop_count += 1
    call early_resolution_check(loop_count)
    jump loop_five


# ============================================
# LOOP FIVE
# ============================================
label loop_five:
    call show_stats
    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(5, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)

    narrator_voice "第五次醒来，风声先到。"
    narrator_voice "公告牌写满了字：木纹缝里楔着陈年灰絮，炭笔的新划口压着旧墨迹，层层叠叠却从不注销——读起来像名册翻到新页却仍黏着前一行的欠债。"
    narrator_voice "卢西恩在廊下点起一盏小灯，灯焰贴着七灯铭纹轻轻发抖；你头一次把这趟折返读成指印叠着欠条摞起来的一张薄纸。"
    narrator_voice "你心里某处的铁栓忽然松了一格：要是不选路，路由人来替你选。"
    narrator_voice "廊柱拐角的酒橱还半阖档板，裸麦粥与醋渍鱼碎在同一柄勺边厮磨，湾岸腌渍的潮腥像借魂还乡；谁先多舀一勺，都像挪走名录里另一人该得的肉筹码。"
    lucien "雾海港的余味，我认得。半碗封顶；再添我会心虚——像在抢别人床位上该分到的那口力气。"
    mika "馋在喉咙里打转，外头榷吏还在磨刀。砖缝里爹妈攒那点屑末……我只敢闻卤水，整块粗盐，真咽不下去。"
    cecil "哎，盐瓮别离我箭囊太近——指节先闷汗。都让开一寸，唔，耳朵才配得上听你们把这餐吵完。"
    cassius "唔……冷茶还替湿本压着胃呢。这一餐要入账——只能落在『合议前慰饷』。啧，别给我写成私底下的欢宴脚注。"
    you "勺沿碰唇前我得先等喉里的铁腥味塌下半格，咽稳了才敢咬第一口热气。"
    $ oral_entry_day = oral_run_week(5)
    $ _oral_wb = oral_week_bridge(5, oral_entry_day)
    narrator_voice "[_oral_wb]"
    $ tinted_line = tinted_gate_narration("loop5_gate", companion_lens, lens_level, "entry")
    narrator_voice "[tinted_line]"
    $ rush_now = False

    menu:
        "问米迦记不记得那些梦":
            mika "记得一点……你总是一步先倒。"
            narrator_voice "他说出这个句子时，声音很轻，绿眼睛却直直落在你脸上，像两枚发冷的钉。"
            $ mika_knows_me = True
            $ mika_trust += 1

        "去找最后一扇门":
            you "神殿里还有最后一扇门。"
            mika "那就走。总有人得撞第一下门——啧，我来。"
            narrator_voice "他把锈剑往肩上一搁，铁味和冷风一起贴过来。"
            $ awareness += 1
            $ clue_truth = True
            $ clue_shrine = True

        "和米迦谈条件":
            mika "这次我有条件——不许再往缝里塞你自己。听见了没。"
            narrator_voice "他说得很平，指节却勒得发白，像把整把剑都攥出了硬响。"
            $ tenacity += 1
            $ mika_trust += 1
            $ mika_knows_me = True

        "先找卡修斯":
            cassius "又来了啊……"
            you "最后一次。"
            narrator_voice "红发侧过来，蓝眼在火里很亮，亮得像刚从深井底部捞上来的冷铁。"
            $ cecil_bond += 1
            $ authority += 1

        "带所有人进神殿":
            you "都跟我走。"
            mika "这趟要是走完，我要抱着锅喝到天亮。"
            cecil "唔，先活到桌前。浓汤……饭后再讲。"
            narrator_voice "两道目光同时落到你身上，空气里的灰和火味一齐沉了沉。"
            $ sync += 1
            $ tenacity += 1
            $ recruited_count += 1

        "直接带线索去旧庭要塞":
            you "目标旧庭棱堡——把卷宗与刀背都带上。"
            narrator_voice "夜风掠过耳廓像薄刃；他的紫瞳在风里也不眨，只听你每个字落下的重量。"
            cecil "路线重排。听着：别逞单人那种英雄名头。"
            narrator_voice "他吐令时唇齿几乎不动，肩背却整张弓开成冷静的弧；指腹在弓弦外侧停住的那一下像在替你扣保险。"
            you "照准。"
            narrator_voice "他没再贫嘴，只是把肩线收成一条更直的线，像先在黑里替你劈出一道指北的硬边。"
            $ authority += 1
            $ awareness += 1
            $ clue_truth = True

        "把门槛上的灰抹在掌心（回声贴掌背呢，腕底脉门自己发沉）":
            narrator_voice "灰黏在掌纹里，你一握拳，指节发凉。"
            narrator_voice "门缝里漏回声，一轻一重拍在石阶上；那节拍却总比你腕底的脉跳慢半瞬，逼得你下意识屏息去对拍。"
            $ thread_obsession += 1
            $ thread_revelation += 1

        "今夜就推门，不再多等（经句压进喉间，决断提前）":
            you "今夜就推门。"
            mika "你这口气像在敲最后一遍钟。"
            narrator_voice "你想起旧卷上的句子：因为门窄，路小，找着的人也少。"
            $ authority += 1
            $ thread_obsession += 1
            $ scripture_mark += 1
            $ rush_now = True

        "再观一轮风向，延后推门（先听风，再动手）":
            you "再等一轮。风还没说完。"
            cassius "退一步能多喘一口气；但这一寸每一寸都要付——活着的人才付得出。"
            narrator_voice "廊下烛火一明一暗，像抄写员在行间留白。"
            $ tenacity += 1
            $ meta_awareness += 1
            $ thread_mercy += 1
            $ rush_now = False

    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(5, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)
    $ tinted_line = tinted_gate_narration("loop5_gate", companion_lens, lens_level, "post")
    narrator_voice "[tinted_line]"

    narrator_voice "选项落定才听见远处封哨追上来——裂谷前哨锁三条要道声响，特许样本揉成废纸团，靴印盖住地图像在盖邮戳。"
    narrator_voice "夜审名单同夜掉进酒馆闲话，账本与讲坛名字并排，挨家木闩都发出一声短促吱呀。"

    narrator_voice "白天争过的面子入了夜都像矮半截。钟声把人赶向同一条缝里。"
    narrator_voice "神殿最深处那扇门微微开了一线。门缝里涌出冷风，吹过皮肤会起细小颗粒感，像冬夜里第一把雪。"
    $ loop_count += 1
    call early_resolution_check(loop_count)
    if rush_now:
        jump final_resolution
    jump loop_six


# ============================================
# LOOP SIX
# ============================================
label loop_six:
    call show_stats
    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(6, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)

    narrator_voice "第六次醒来，钟楼还没响。"
    narrator_voice "雾把整条街按得很低。旧殿台阶上多了一枚断蜡印，印文只剩半截经句。"
    $ oral_entry_day = oral_run_week(6)
    $ _oral_wb = oral_week_bridge(6, oral_entry_day)
    narrator_voice "[_oral_wb]"
    $ tinted_line = tinted_gate_narration("loop6_gate", companion_lens, lens_level, "entry")
    narrator_voice "[tinted_line]"
    $ rush_now = False

    menu:
        "让卢西恩再查一次伤口（药酒苦橙味，时间感反向）":
            lucien "触诊上还说得过去——创面在收口，体感却像在逆着钟摆走。"
            lucien "今晚别再硬顶着巡夜了。这样下去，明日下中殿台阶——膝会先打颤，唔。"
            $ thread_mercy += 1
            $ tenacity += 1

        "把七灯教义读给米迦听（教义一句句落地，你跟米迦的呼吸才慢慢对上）":
            you "灯照脚前，也照审判。"
            mika "那就念慢些——一字一顿，别拿经文砸自己的脚踝。"
            narrator_voice "他把剑平放在膝上，铁器在雾里泛冷光。"
            $ scripture_mark += 1
            $ sync += 1
            $ meta_awareness += 1

        "逼问卡修斯裂谷坐标（他应声时像在交付一把会烫伤手的钥匙）":
            you "把裂谷坐标给我。"
            cassius "难得你只问怎么走。两组坐标都在这里——羊皮上也有落款注释：炉灶潮灰那一段气味，要写进你以后回忆的誓词里；从今往后记起裂谷来，鼻头多半先骗你一个心跳。除非你转身走远，唔，最好别听我念到最后一句。"
            narrator_voice "羊皮地图摊开，墨线像干涸的血丝。"
            $ awareness += 1
            $ authority += 1
            $ thread_obsession += 1

        "于圣所列像座前的誓石边，折断旧钥匙（断裂声里，同时有退让与抬头）":
            narrator_voice "钥匙应声断折，泠泠一记清音像骨节沉在寒泉底下互碰。"
            narrator_voice "你听见心里有空处倏然塌方，余响不及扑到耳边，就先跌进那口空里。"
            $ thread_erosion += 1
            $ thread_revelation += 1

        "再等最后一轮（把门边的余地留给还没说完的话）":
            you "还差一轮。"
            narrator_voice "你说话时指节下意识蹭过门框旧纹，像在摸一道还没结痂的口子。"
            cecil "唔……你总算肯给合议外头留一息回旋。慢一点无妨——慢而稳的人，往往能把自己拖回拱门内侧。"
            narrator_voice "他垂下眼睫一瞬，紫瞳再抬起已软了半分；唇线仍直，掌心却朝你摊开半寸，像把「等」字放在你看得见的实体上。"
            $ thread_mercy += 1
            $ mika_trust += 1
            $ rush_now = False

        "立刻开门（夜还深，门先回应你）":
            you "现在开门。"
            narrator_voice "你掌心发热，像握着一枚还在跳动的印章。"
            $ authority += 1
            $ scripture_mark += 1
            $ rush_now = True

    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(6, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)
    $ tinted_line = tinted_gate_narration("loop6_gate", companion_lens, lens_level, "post")
    narrator_voice "[tinted_line]"

    $ dice, bonus, total, success, result = roll_check("坚韧与并肩", tenacity + sync, 12)
    $ _tri_l6 = terminal_roll_intro("坚韧与并肩", result)
    narrator_voice "[_tri_l6]"
    $ fate_msg_full = fate_message_lines(result)
    narrator_voice "[fate_msg_full]"
    $ fate_msg = fate_message(result)
    $ renpy.show_screen("fate_notify", fate_msg, "肩与肩咬住同一力道：[dice]+[bonus]=[total]")

    narrator_voice "门边的脚步终于肯一齐收住，白昼里被告示和嗓门塞满的那股嚣响才又回到舌底：雾灯会拿命名遗物换药喘。议会当场撕作两派墨迹，墨瓶在桌面上炸开星屑。"
    narrator_voice "钟舌无风而动，满城互告版本——有的说裂隙升阶，有的说实验越轨，抄写员却把两张纸贴进同一阵风。"

    $ loop_count += 1
    call early_resolution_check(loop_count)
    if rush_now:
        jump final_resolution
    jump loop_seven


# ============================================
# LOOP SEVEN
# ============================================
label loop_seven:
    call show_stats
    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(7, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)

    narrator_voice "第七次，天亮像在门外迟了一拍，街口静得不合章程。"
    narrator_voice "幔旌沿高耸石壁曳下，风里剥出一阵裂帛细碎之响——似有目于门后以残页私语，行行贴着骨髓往里渗。"
    narrator_voice "边境临时军法在午夜生效。议会接管钟楼与粮仓，看守团申请全面封印遗迹，学团公开反对知识封禁。"
    narrator_voice "五方势力的使者都到了镇口。每一盏灯下都有人在等你表态。"
    narrator_voice "你忽然明白，某些门并非通向彼岸，只是通向你的代价。"
    $ oral_entry_day = oral_run_week(7)
    $ _oral_wb = oral_week_bridge(7, oral_entry_day)
    narrator_voice "[_oral_wb]"
    $ tinted_line = tinted_gate_narration("loop7_gate", companion_lens, lens_level, "entry")
    narrator_voice "[tinted_line]"

    menu:
        "为米迦系紧护腕（布条勒紧时，他把额头抵过来一瞬）":
            narrator_voice "你把皮带扣到最后一孔。皮革有旧雨味。"
            mika "这次别把我丢在门后。"
            narrator_voice "他用额角极轻地抵过你肩侧一霎又撤开——像碰触也是借来的胆量；绿眼睛里那一闪发亮，热气扑在你领口，乱得顾不上再挂玩笑。"
            $ thread_mercy += 1
            $ sync += 1
            $ mika_trust += 1

        "把自己的名字写进封蜡（蜡油先咬住指腹发烫，疼了半拍，才把名字按实）":
            narrator_voice "蜡油一卷先咬住指腹的皮热；皮肉下意识缩半分，你还是把名字摁进软蜡。"
            narrator_voice "印冷下来时指腹却还在烫，胃里像无端多坠一枚冷铅——咽不净也吐不出，只好任它与那一笔一起沉入门槛阴影里。"
            $ thread_revelation += 1
            $ scripture_mark += 1
            $ authority += 1

        "让卡修斯朗读禁章（字音刮过墙皮，灰线就扑簌掉点渣）":
            cassius "听着——尘土仍归于尘；凡受赐气息者，仍将气息交还造物之手。"
            narrator_voice "每一个字都像细小铁钉，敲进你耳后。"
            $ meta_awareness += 1
            $ thread_erosion += 1
            $ scripture_mark += 1

        "沉默推门（门轴替你开口）":
            narrator_voice "你没有说话。门轴吐出一声长叹。"
            $ tenacity += 1
            $ awareness += 1

    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(7, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)
    $ tinted_line = tinted_gate_narration("loop7_gate", companion_lens, lens_level, "post")
    narrator_voice "[tinted_line]"

    $ loop_count += 1
    call early_resolution_check(loop_count)
    jump final_resolution


# ============================================
# FINAL RESOLUTION
# ============================================
label final_resolution:
    narrator_voice "你们走到最后一扇门前。石壁内部传来低低的轰鸣，像有什么巨大东西正隔着岩层缓慢翻身。"
    $ companion_lens = pick_companion_lens(mika_trust, cecil_bond, clue_elder, thread_mercy, authority)
    $ lens_level = calc_lens_level(8, meta_awareness, thread_revelation, scripture_mark, thread_erosion, authority)
    $ tinted_line = tinted_gate_narration("final_gate", companion_lens, lens_level, "entry")
    narrator_voice "[tinted_line]"
    $ dice, bonus, total, success, result = roll_check("坚韧与并肩", tenacity + sync, 12)
    $ m = meta_roll()

    $ _tri_fin = terminal_roll_intro("坚韧与并肩", result)
    narrator_voice "[_tri_fin]"
    $ fate_msg_full = fate_message_lines(result)
    narrator_voice "[fate_msg_full]"
    $ fate_msg = fate_message(result)
    $ renpy.show_screen("fate_notify", fate_msg, "门框里回声落定：[dice]+[bonus]=[total]")

    if meta_awareness >= 2 and m == 20 and thread_revelation >= 2:
        $ renpy.show_screen("fate_notify", "……有什么东西变了。一道裂缝。在那片虚无的最深处，出现了一道不该存在的裂缝。", "纸背渗水，像在替你揭开一行尚未公证的合议脚注")
        narrator_voice "……有什么东西变了。一道裂缝。在那片虚无的最深处，出现了一道不该存在的裂缝。"
        jump ending_author

    if loop_count <= 5 and scripture_mark >= 1 and m >= 12:
        narrator_voice "你过早推开了门。灯先照到你脚下，也照见你背后的空处。"
        jump ending_pilgrim

    if loop_count >= 7 and scripture_mark >= 3 and thread_revelation >= 4 and m >= 12:
        narrator_voice "门内传来许多声音，像同一本书被多人同时诵读。"
        jump ending_judgement

    if loop_count >= 7 and thread_mercy >= 4 and success:
        narrator_voice "你把刀背朝向自己。门后的风忽然缓下来。"
        jump ending_covenant

    if thread_obsession >= 4 and m >= 15:
        narrator_voice "命运的丝线忽然勒紧了你的腕骨。你听见自己的名字在石壁里回响。"
        jump ending_throne

    if thread_mercy >= 3 and success and m >= 10:
        narrator_voice "命运的丝线贴着你的掌心回暖。某个决定在舌底下慢慢摊开，像终于肯换一口气。"
        jump ending_sacrifice

    if thread_erosion >= 3 and not success:
        narrator_voice "命运的丝线在你指间打滑。你抓住了一瞬，下一瞬又从原处跌回。"
        jump ending_eternal

    if result == "critical_success":
        if mika_knows_me:
            jump ending_ascension
        else:
            jump ending_true

    if result == "critical_failure":
        if authority >= 2 and tenacity >= 2:
            jump ending_throne
        else:
            jump ending_eternal

    if success:
        menu:
            "最后抉择":
                "并肩离开（把手留给活人）":
                    jump ending_true
                "留下断后（把背影留给风）":
                    jump ending_sacrifice
    else:
        if tenacity >= 2:
            menu:
                "最后抉择":
                    "留下断后（把背影留给风）":
                        jump ending_sacrifice
                    "再入轮回（把问题留到下次）":
                        jump ending_eternal
        else:
            jump ending_eternal


# ============================================
# ENDINGS
# ============================================
label ending_true:
    stop music fadeout 2.0
    narrator_voice "石柱崩坼，尘埃如晚冬之雪纷扬洒落，覆满你们眉睫。"
    narrator_voice "米迦对峙而立，发梢雪粉簌簌，目中霜色却缓缓退潮。"
    mika "收队。"
    narrator_voice "他又牵了牵嘴角——那笑稀薄如长夜尽头地平线才泄出的一线霜白。"
    you "奈尔。"
    mika "后面并肩。"
    scene black
    with dissolve
    narrator_voice "晨光沿阶徐行，冷白、肃穆，像听证会羊皮上滴漆未干的终审——不许涂改，只许领受。"
    narrator_voice "塞西尔把弓背回归肩窝，食指仍轻颤，似自寒渊捞回半寸人间温。"
    narrator_voice "卡修斯将最厚手稿紧抵心口，未尝展卷，惟仰首窥天光一线。"
    narrator_voice "卢西恩半蹲侧畔，挨次探你们鼻息，苦橙药雾随吐纳盘绕不散。"
    narrator_voice "后来你们在边境小镇租住下来，租契、麦香、巡夜铃此起彼伏，将岁月裁成可数之页。"
    narrator_voice "米迦习得晨间记账，塞西尔将夜巡弧线缩成更短的守护，卡修斯偶于杯渍之侧添半行笺注。"
    narrator_voice "至深秘辛被束之高阁，铁柜潮夜微胀，似有人于黑暗里悄翻残章。"
    narrator_voice "你心知肚明那门未曾消亡，仅把嚣音按至低不可闻，候下一位敢称自己姓名的人。"
    narrator_voice "你终获日常可守，却要习惯薄麦粥与晨霭为伴，偶有深处沙响如鼠啮旧纸；那声息不灭，只在岁月里被磨成骨血中的一根细刺。"
    return


label ending_sacrifice:
    stop music fadeout 2.0
    narrator_voice "你倾塌之际，高壁碎砾如瀑，砸在肩颈，冷意直透井底铸铁。"
    narrator_voice "米迦扑至身侧，咽喉仅挤出一缕破音。"
    narrator_voice "塞西尔唇畔仍噙薄谑，箭却已就弦，腕如磐石。"
    you "我没事……"
    mika "你每回都这么说。"
    cecil "我去开路。你们别回头。"
    narrator_voice "心音渐弱，似沉水鼓点遥不可及。"
    narrator_voice "卢西恩死勒止血带至指节失血，绷布终为殷红蚕食。"
    narrator_voice "卡修斯蹲守你左肩，喃念逆转术咒，声线平抑如怕惊你走得太轻。"
    narrator_voice "米迦眸中光柱寸寸坍圮，复又强行擎起；他咬肌鼓突，似与无形判官角力。"
    scene black
    with dissolve
    narrator_voice "嗣后每至残焰将熄、每至须站队之刻，总有人低唤你名。"
    narrator_voice "塞西尔惯于默半拍后引弦；卢西恩阖箱抬眼，望向最晦暝支路。"
    narrator_voice "你的名字，成了队中旧创，触之即痛，痛后却叫人背脊笔挺。"
    narrator_voice "边境稚童长成，会听说曾有人在扉将严合之瞬，以己身换他者明日。"
    narrator_voice "你换得生途过亮，亮至你再也踏入不得；尘世间从此多一盏长明灯芯，却永远照不到你所立之影。"
    return


label ending_throne:
    stop music fadeout 2.0
    narrator_voice "裂罅于前洞开，风里卷铁锈、陈血与余烈余温。"
    you "我还你。"
    narrator_voice "你将米迦掷过门限，己身独留晦影。"
    narrator_voice "塞西尔振弦，黑翎箭掠风，惟一记短痛割开静夜。"
    narrator_voice "石柱轰然闭阖，黑暗壅起如迟来太久的宝座。"
    narrator_voice "你落座之上，寒流沿椎骨攀升，细针似的刺入后颈。"
    scene black
    with dissolve
    narrator_voice "初夜门外犹有跫音，次夜仅余回音，至第七夜连回音亦学会缄舌。"
    narrator_voice "你落下第一道加盖议会蜡封的命令，城头火炬齐举，风中铁味陡增。"
    narrator_voice "第二道蜡封滚过案角，仓廪、钟楼、巡线同寂，众生的吐纳竟随你节律起伏。"
    narrator_voice "冠冕的尖与环予你千钧重负，亦剥你人间姓名一层又一层。"
    narrator_voice "米迦偶至，立长阶之极底，仰视如望孤星邈远。"
    narrator_voice "塞西尔的箭簇再不向你，他只负弓如影碑伫立。"
    narrator_voice "你握权柄之极，再难听闻有人平视唤你本名；公文与典册各司其职，或称执印者，或称门后之眼，惟长风犹记奈尔二字。"
    narrator_voice "你换得序列与砝码，换不得平视之面：王座要你永无谬误，而『被读懂』终成违禁之词。"
    return


label ending_ascension:
    stop music fadeout 2.0
    narrator_voice "你探掌，米迦五指扣合。"
    narrator_voice "光自指隙滋生，先点燃皮肤纹理，再把神殿、石壁与回声一层层推远，直至天幕像被人从内侧揭开，露出其后过曝的空白。"
    mika "你还在这……"
    you "一直都在。"
    narrator_voice "塞西尔矗立你后方，弓影斜曳，谑色虽薄却从未撤离。"
    narrator_voice "卡修斯据阶侧，赤发乘风，瞳若冬汛海面上的冷月色带。"
    narrator_voice "苍穹裂帛，四人并立新路尽头，足下生风，极目有光。"
    narrator_voice "卢西恩最后一个跟上来，药箱在背后轻撞，铜扣闷响一记，像在替他把「还跟得上」咽成半截气。"
    scene black
    with dissolve
    narrator_voice "你们渡光刹那，影子被拽得绵长，宛若另一卷尚未滴蜡签封的命册。"
    narrator_voice "城楼河桥渐缩为地图上折进口的淡线。"
    narrator_voice "吐纳在风中趋同，似两缕脉动相贴却始终留隙。"
    narrator_voice "代价不镌于创痕而烙于追忆：昨夜言辞将褪，惟一掌余温执迷不化。"
    narrator_voice "某晨米迦忽然驻足反顾，问你昨夜是否复述同一句对白。"
    narrator_voice "你点头却又描摹不清全豹，只记得风透亮、掌心灼热、前路如新纸。"
    narrator_voice "你们不止前行，宛若把旧纪元掷在肩后灰烬里，同时为一片尚未记入海图的无名疆域授名。"
    narrator_voice "你要的光辉与蹊径俱在，独「何故启程」将在风中层层剥落。"
    narrator_voice "你化作新人间的火种，却亦将慢慢遗忘自己曾经是谁的火。"
    return


label ending_eternal:
    stop music fadeout 2.0
    narrator_voice "轮回继续。"
    narrator_voice "你又立回村口，曦光倾角纹丝未移，木牌那道旧裂痕仍如犬齿獠列。"
    mika "古怪……我总觉得这风口我们站过许多遍……"
    narrator_voice "米迦瞥你，唇瓣翕动，终归把话硬生生咽作一口冰。"
    narrator_voice "风穿行罅隙，青苔伏低，似闻某道熟稔至麻木的口令。"
    scene black
    with dissolve
    narrator_voice "你抬趾，循旧径再踏一回。"
    narrator_voice "闭环如表针，幽秘、执念，泛金属涩味。"
    narrator_voice "告示纸虽日新，句子却永远在同一位折返。"
    narrator_voice "塞西尔黄昏仍至，弦响分秒未差；卡修斯午后仍展卷，指尖止于恒常那行。"
    narrator_voice "卢西恩苦酒药气总于门前那阵风悄然浮起，一触即沉。"
    narrator_voice "你照旧颔首照旧行，似在一张染过圣油又浸过雨的誓约羊皮上反复按指——指温融不开旧蜡。"
    narrator_voice "偶尔你抢前半步欲改一词，世界却瞬抹你足印使平。"
    narrator_voice "梦魇里有无名手重注边批，墨尚湿，次轮晨曦已泼入窗。"
    narrator_voice "轮回不躁不嚣，只把众生活成熟练戏子。"
    narrator_voice "这里没有终卷的蜡封落下，只有同一道石缝里，被反复复写的第一行起手式。"
    narrator_voice "至酷在于熟稔——你预知每步将痛，却仍踏下。熟到最后，你连恨都倦怠施予轮回一眼。"
    return


label ending_author:
    stop music fadeout 3.0
    narrator_voice "耳畔有人唤你，音线贴骨，如细针徐徐画圆于铜盘。"
    narrator_voice "活见鬼——殿风皆止，嗓音却愈迫愈近。"
    narrator_voice "门影起皱，你的手背随之龟裂，肌理翻成细密活字，霉潮与墨香扑袭。"
    mika "页边在收口……"
    narrator_voice "米迦举目，碧瞳如冷焰将熄的灯芯。"
    narrator_voice "塞西尔指端战栗，紫外碎光沿路排成注脚阵列。卡修斯缄口，蓝瞳坚如盐卤久渍琉璃。"
    narrator_voice "你想谑骂半句轻松，喉间却仅剩铁腥。"
    you "别翻页。"
    narrator_voice "卢西恩猛扣药箱于地，脆响刺穿耳鼓；他盯你手背活字，宛若初见无法缝合之灵伤。"
    narrator_voice "门框稀薄，石理退成网格，烛焰抖成失真星斗。"
    narrator_voice "纸涛轰然，似海潮入室，潮气浸满陈墨与焚灰。"
    narrator_voice "轩窗黯去，黑绢翻卷，他们步步踏出框外，靴跟敲击长夜有如远廊钟摆。"
    narrator_voice "米迦临走悄然反顾，唇齿无声开合，你猜那是在唤你名讳。"
    scene black
    with dissolve
    narrator_voice "故事戛然于此行，足音却迤逦外延。"
    narrator_voice "你立于行间背面，见新濡墨沿陈年字迹蜒行。"
    narrator_voice "转瞬行距咬合，段落封缄，呼吸亦化为标点。你抬腕欲阻，掌心所触惟字。"
    narrator_voice "你终碰触叙事边疆，却已身化他人指掌间一句注——识得结构的代价，是再无能佯装看客。"
    return


label ending_pilgrim:
    stop music fadeout 2.0
    narrator_voice "你先举步越阈，足下骤寒，宛若履及初退礁石。"
    narrator_voice "背脊之后唤声次第：首声贴耳，再声已在半街之外。"
    narrator_voice "你几欲回眸，唇齿却塞满沙尘涩味。"
    narrator_voice "古语于颅内翻掀：寻者得散，驻足者更名。"
    scene black
    with dissolve
    narrator_voice "石径漫长得失其拐，尽头孤灯或昂或俯，似风中倦眼。"
    narrator_voice "你笼袖徐行，砂砾啮靴，窸窣如身后有人暗数步拍。"
    narrator_voice "每进一步，焰芯即短一毫，夜幕便多一枚难解批注。"
    narrator_voice "米迦话音至第三唤后荡然；塞西尔弦颤亦随风葬尽。"
    narrator_voice "卡修斯留于你脑际的页眉评注，终会缩成几颗冷字节抵后脑。"
    narrator_voice "卢西恩掖你掌心那方药绫尚温，行至半程那点余温亦散尽。"
    narrator_voice "此途无存根，惟有向。你携疑而进，候后人代为终点题名。"
    narrator_voice "某夜你见石壁己影叠出双层轮廓，似有人并肩却永隐其形。"
    narrator_voice "你不再回首——回首路窄，向前夜深。"
    narrator_voice "朝圣至极，连『你是谁』亦磨成寂然一问。"
    narrator_voice "你换得前程，换不得归巢；每粒砂记你，每盏灯皆拒留你名。"
    return


label ending_judgement:
    stop music fadeout 2.5
    narrator_voice "门扉启至半掌，炽白先灼睑，再灼喉。"
    narrator_voice "七记轻敲连环落进石板，七盏灯应声齐燃。"
    mika "奈尔，挑一盏。手别抖。"
    narrator_voice "你探掌，掌纹灼烫，陈灰起辉，湿壁被火线逐行映亮。"
    narrator_voice "你霎时彻悟：神殿的裁断先烙在你身上，随后才轮到众生自陈。"
    scene black
    with dissolve
    narrator_voice "焰苗次第寂灭，中殿只剩拱廊底下那种又低又长的穿风。"
    narrator_voice "门板吞啮你名，刻槽灼手，指腹按之如细刺密阵。"
    narrator_voice "你携真相而出，亦留一截骨血于门腹。"
    narrator_voice "塞西尔守你左畔，弓未张弦，指尖却恒扣槽际，似捂即将崩弦之瞬。"
    narrator_voice "卡修斯撕经末页为二，半扬于风，半压灯台。"
    narrator_voice "卢西恩睹你掌中辉脉，睫颤不已，终只吐半句：别把自己全典当在此。"
    narrator_voice "你无声颔首，仍将掌印重重捺下。"
    narrator_voice "此后凡临此门者，先诵你供状，再闻己身裁决。"
    narrator_voice "或惧或跪或遁，扉不言不挽，只教人亲书当承之一行。"
    narrator_voice "你予尘世一面可宣读之真相镜，却自铸为镜脊那层凛冽锡箔——仰望你传奇者再看不见镜里你真实容颜。"
    return


label ending_covenant:
    stop music fadeout 2.0
    narrator_voice "你推扉亦释刃。"
    narrator_voice "米迦越阈为先，塞西尔与卡修斯相继，无人催迫。"
    narrator_voice "卢西恩于廊下阖箱，铜扣铿然，似一句迟来却终于落地的结语。"
    scene black
    with dissolve
    narrator_voice "曙色将倾，你们席地分啮干饼与冷茶，风砭骨，喉间却渐涌暖意。"
    narrator_voice "卢西恩挨次按脉、察创、听息，将每人肩上沉荷拆作可咽之剂。"
    narrator_voice "塞西尔重誊夜巡表，把最危一格留予己名。"
    narrator_voice "卡修斯划去满纸聪明捷径，仅余数行「明日若活」之眉批。"
    narrator_voice "米迦踞门槛啃一块冷硬荞麦饼，腮帮用力得仿佛要把夜也嚼碎吞下。"
    mika "活着真贵——可还是值。"
    narrator_voice "你们皆笑，笑声极轻，似恐惊破将亮未亮的天。"
    narrator_voice "无人被宣判凯旋，惟誓以漫长岁月公摊同一债册。"
    narrator_voice "账本将厚创将复迸，前路犹有无数扉与夜及代价。"
    narrator_voice "然此回不各自署名——每页末皆摁下五指纹。"
    narrator_voice "你们换来的乃同一张分期券，痛楚可复印，痊愈亦可复印。"
    narrator_voice "再无人能独自啮紧牙关谎称『我没事了』于心无愧。"
    return
