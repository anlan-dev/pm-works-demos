# 《雾灯残页》AIGC Prompt 整合文档

版本：2026-05-25 · 基于《角色设定集》《世界观设定集》《故事概览》生成  
用途：Stable Diffusion / ComfyUI / Midjourney / Leonardo.ai 等AIGC工具的提示词参考

---

## 一、通用风格锚定

### 画风基础（所有素材通用）

**正向锚定词**
```
masterpiece, best quality, highly detailed, cinematic lighting, atmospheric, 
dark fantasy, European medieval aesthetic, muted color palette, 
painterly style, oil painting texture, subtle grain
```

**负向通用词**
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, 
fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, 
watermark, username, blurry, anime screencap, chibi, super deformed, 
bright saturated colors, neon glow, modern elements
```

### 风格参考关键词
```
Western dark fantasy, gothic medieval, mist-shrouded, 
ink-wash undertones, muted earth tones with cold accents,
reminiscent of Darkest Dungeon / Blasphemous / Castlevania aesthetic
```

---

## 二、角色立绘 Prompt

---

### 2.1 奈尔（Nier）· 执印遗裔 · 主视角

**核心视觉标签**
- 银白至银灰长发，中分偏三路，低马尾用旧墨绳
- 红宝石至冷玫红瞳，狭长杏眼，冷粉白肤色
- 窄细骨架，薄肌型，站姿重心略偏脚后跟
- 灰青/藏青长摆外袍，系带多打半扣
- 袖口内侧陈年浅裂搔痕，旧墨绳扎发

**基础立绘 Prompt**
```
young man, approximately 23 years old, slim lean build, 172cm,
silver-white to silver-gray hair, medium length to collarbone, 
center-parted, low ponytail tied with worn dark ink-stained cord,
ruby red to cold rose-pink eyes, narrow almond-shaped eyes, 
slightly upturned outer corners, cold pink-white pale skin,
thin angular jawline, low cheekbones, straight nose, thin lips,
expression: calm guarded, slightly downcast chin,
clothing: long gray-blue tunic robe, silver trim edges, 
extra half-knot on chest lacing, worn leather short boots,
right hand resting near sleeve opening, 
subtle old scratch marks visible on inner wrist,
dark fantasy medieval setting, atmospheric lighting,
masterpiece, best quality, highly detailed
```

**表情变体**

| 表情 | 额外提示词 |
|------|-----------|
| 警觉 | `eyes narrowed, scanning left and right, hand tensed near blade, body slightly angled toward exit` |
| 疲惫 | `dark circles under eyes, slightly unfocused gaze, jaw clenched, shoulders heavy, tongue touching teeth` |
| 温柔（稀有） | `soft gaze directed downward, lips slightly parted, hand reaching forward hesitantly` |
| 崩溃临界 | `wide eyes, pupils contracted, veins visible on temple, trembling fingers gripping wrist, shadow beneath eyes deepened` |

**动作变体**

| 动作 | 额外提示词 |
|------|-----------|
| 看门缝 | `leaning slightly forward, one eye peering through door gap, body angled for quick retreat` |
| 系带 | `fingers tying cord lacing with deliberate extra knot, focused downward gaze` |
| 拔剑戒备 | `sword half-drawn, stance low and ready, eyes fixed on threat, cold breath visible` |

---

### 2.2 米迦（Mika）· 勇者职志 · 情感锚点

**核心视觉标签**
- 浓棕至深栗色中长发，偏分碎刘海，半丸子或自然散落
- 草绿至深绿瞳（外圈暗褐渐变），偏圆大眼
- 暖米色偏浅褐肤色，面颊易带薄红
- 圆脸偏方，笑起来面颊隆起
- 左肩背带压得领口发皱，护手腕缠暗褐色旧布打死结
- 腰间锈蚀短剑，护手磨圆，鞘口磨白

**基础立绘 Prompt**
```
young man, approximately 22 years old, athletic compact build, 175cm,
warm tan skin with natural flush on cheeks,
dark brown to chestnut hair, medium length to ear-shoulder, 
side-parted with messy bangs, half-up bun or loose,
green eyes with dark brown outer ring, round large eyes, 
round square face, soft jawline, dimpled when smiling,
slightly upturned nose, visible stubble shadow,
expression: confident grin with hint of alertness,
clothing: travel-worn leather armor, dark brown worn cloth strips 
wrapped around wrist guards in tight knots, frayed edges visible,
left shoulder strap wrinkled from heavy pack,
rust-stained short sword at waist, worn smooth grip, 
leather boots with uneven heel wear,
dark fantasy medieval setting, atmospheric lighting,
masterpiece, best quality, highly detailed
```

**表情变体**

| 表情 | 额外提示词 |
|------|-----------|
| 大笑 | `wide grin, eyes squeezed into crescents, head tilted back, teeth showing, cheeks puffed` |
| 强撑笑 | `forced smile not reaching eyes, jaw tight, glance sideways checking companions, shoulders tense` |
| 愤怒 | `no smile, eyes cold and focused, grip tightening on sword, nostrils flared` |
| 受伤隐忍 | `lips pressed thin, sweat on forehead, hand pressing wound, still trying to stand` |

**动作变体**

| 动作 | 额外提示词 |
|------|-----------|
| 拨人退后 | `one arm extended pushing companion behind, body positioned as shield, facing danger` |
| 杖剑笑骂 | `leaning on rusted sword like cane, other hand gesturing while laughing, casual stance` |
| 嚼面包 | `sitting on stone threshold, tearing bread with teeth, relaxed but watchful` |

---

### 2.3 塞西尔（Cecil）· 弓箭手 · 温和锋刃

**核心视觉标签**
- 纯黑发略带钢蓝高光，披肩至胛骨上缘，偏分长刘海挡右眼
- 紫罗兰至暗紫瞳，细长凤眼，外眦微扬
- 偏冷米色肤色，颧骨外缘陈旧浅白细痕（侧逆光可见）
- 窄长鹅蛋脸，口角默认上扬2mm礼貌笑
- 袖口系带收紧防挂弦，腰间细小磨石袋
- 袍内暗藏旧看守团徽针线走线

**基础立绘 Prompt**
```
young man, approximately 24 years old, lean wiry build, 178cm,
cold pale skin, subtle scar on cheekbone visible in side lighting,
pure black hair with steel-blue sheen, straight, shoulder length,
side-parted long bangs partially covering right eye, low ponytail,
violet to dark purple eyes, narrow phoenix eyes, outer corners upturned,
narrow oval face, sharp clean jawline, polite half-smile default,
thin sharp nose, slightly pointed chin,
expression: calm attentive with habitual polite smile,
clothing: long dark robe with tapered hem, sleeves tied with cords,
soft leather bracer on forearm, small whetstone pouch at waist,
dark hooded cloak draped back, worn leather boots,
longbow carried across back or held at rest,
dark fantasy medieval setting, atmospheric lighting,
masterpiece, best quality, highly detailed
```

**表情变体**

| 表情 | 额外提示词 |
|------|-----------|
| 礼貌笑 | `polite closed-mouth smile, eyes warm but guarded, head slightly tilted` |
| 冷杀意 | `smile gone, eyes flat and calculating, bow drawn, fingers steady on string` |
| 疲惫 | `eyes half-closed, rubbing neck, bow resting against wall, rare unguarded moment` |
| 回忆痛苦 | `gaze distant, fingers touching inner robe where badge is hidden, jaw tight` |

**动作变体**

| 动作 | 额外提示词 |
|------|-----------|
| 拉弓瞄准 | `full draw, elbow aligned, eyes focused on distant target, breath held, perfect form` |
| 井沿擦弦 | `kneeling by stone well, carefully wiping bowstring with cloth, water reflection` |
| 拂弦收弓 | `fingers brushing bowstring checking vibration, bow lowering, alert scan of surroundings` |

---

### 2.4 卡修斯（Cassius）· 旅行法师 · 代价解释器

**核心视觉标签**
- 铜红至深红中长发，不修边幅偏分，黄铜细夹别刘海
- 冰蓝至深钢蓝瞳，略扁杏眼，扫读视感
- 冷白肤色，耳根先红，眼下淡静脉色
- 长方脸，颞部略凹，颧弓清晰，颚角直角微折
- 领口系至第一颗，防止墨灰入领
- 手记边缘有焦痕，学团徽记可反扣

**基础立绘 Prompt**
```
young man, approximately 26 years old, rectangular lean build, 176cm,
cold white skin, faint blue veins under eyes, 
copper-red to deep red hair, medium length below ear, 
messy side-parted, small brass clip holding bangs back,
ice blue to dark steel blue eyes, slightly flat almond shape, 
intense analytical gaze, sharp scanning expression,
long rectangular face, angular cheekbones, straight jaw with slight angle,
straight pointed nose, thin lips with dry crack line,
sharp straight eyebrows, slight furrow,
expression: cold focused, analytical, slight frown,
clothing: high-collared dark academic robe, buttoned to top,
ink stains on fingers, brass buckles and clasps,
leather satchel with singed parchment edges visible,
short sturdy boots, scholar's travel gear,
dark fantasy medieval setting, atmospheric lighting,
masterpiece, best quality, highly detailed
```

**表情变体**

| 表情 | 额外提示词 |
|------|-----------|
| 冷笑 | `one corner of mouth raised, eyes sharp and dismissive, arms crossed` |
| 专注校勘 | `bent over manuscript, finger tracing text, brow furrowed, lips moving silently` |
| 愤怒压抑 | `ears red, jaw clenched, hands gripping table edge, voice controlled but tight` |
| 罕见温和 | `looking up from book, expression softening, slight nod of acknowledgment` |

**动作变体**

| 动作 | 额外提示词 |
|------|-----------|
| 翻页施法 | `one finger turning page precisely, other hand tracing arcane symbols in air, cold light` |
| 报价 | `holding up fingers, expression flat and serious, gesturing toward document` |
| 扣徽记 | `flipping badge face-down on table, deliberate motion, avoiding eye contact` |

---

### 2.5 卢西恩（Lucien）· 医师 · 代价处理器

**核心视觉标签**
- 淡金亚麻色细软发，及颈根耳垂下，细碎刘海剪到眉上
- 灰蓝至灰绿瞳，略圆大眼带轻微下垂，亲和力
- 米白偏粉肤色，面颊鼻尖易薄红，前臂洗手液日晒色差带
- 柔和卵圆脸，面颊略肉，颚线圆弧
- 袖口卷至前臂上三分之一
- 黄铜药箱角有撞痕，铜扣每步哑哑碰响

**基础立绘 Prompt**
```
young man, approximately 26 years old, slender flexible build, 174cm,
pale pinkish-white skin, natural flush on cheeks and nose tip,
faint tan line on forearms from washing,
light golden flaxen hair, fine and soft, neck length,
neatly trimmed short bangs above eyebrows, slightly inward-curved ends,
gray-blue to gray-green eyes, slightly round droopy eyes, gentle gaze,
soft oval face, round jawline, small round nose, warm expression,
thin straight eyebrows, clean and neat,
expression: calm patient gentle, attentive listening posture,
clothing: rolled-up sleeves to upper third of forearm, 
thin gray shawl draped over shoulders, soft-soled leather boots,
brass medicine case with visible dent on corner, copper clasp,
small scissors hanging from belt, bandage roll at hip,
dark fantasy medieval setting, atmospheric lighting,
masterpiece, best quality, highly detailed
```

**表情变体**

| 表情 | 额外提示词 |
|------|-----------|
| 诊脉专注 | `fingers on patient wrist, eyes watching chest rise and fall, expression neutral concentrated` |
| 温和安慰 | `soft smile, eyes warm, hand extended palm-up, posture open and non-threatening` |
| 过劳疲惫 | `dark circles, sleeves stained, staring at medicine case, shoulders slumped` |
| 撤离抉择痛苦 | `eyes wide, hand gripping bandage, looking between two patients, anguish suppressed` |

**动作变体**

| 动作 | 额外提示词 |
|------|-----------|
| 包扎 | `kneeling beside patient, hands steady wrapping bandage, focused efficient movements` |
| 药箱取药 | `opening brass case, copper clasp clicking, selecting vials with practiced fingers` |
| 数呼吸 | `standing still, head slightly bowed, counting with eyes closed, lips moving silently` |

---

## 三、背景场景 Prompt

### 3.1 灰原边境镇（主舞台）

**村口路牌**
```
medieval village entrance, weathered wooden signpost, 
old paint peeling, cracked wood grain visible,
muddy path, scattered pebbles, morning mist,
distant thatched roofs, low stone walls,
pale dawn light, dust motes in air,
atmospheric perspective, muted earth tones,
dark fantasy medieval setting, painterly style
```

**镇内街道**
```
narrow cobblestone street, medieval town,
stone buildings with wooden shutters, market stalls,
notice board with layered old papers, ink smudges,
puddles reflecting gray sky, laundry lines overhead,
faint smoke from chimneys, distant bell tower,
muted color palette, overcast lighting,
dark fantasy atmosphere, European medieval aesthetic
```

**镇公所**
```
medieval town hall interior, heavy wooden table,
scattered parchments and ink bottles, wax seals,
stone walls with tapestries, iron candelabras,
high arched windows with gray light filtering in,
dusty bookshelves, worn wooden floor,
atmospheric, dim warm candlelight mixed with cold window light
```

### 3.2 旧殿（遗迹/封存地）

**旧殿外观**
```
ancient temple ruins, massive stone pillars, 
crumbling archways, overgrown with moss and vines,
faded carved symbols on walls, weathered reliefs,
misty atmosphere, cold blue-gray light,
scattered broken stone blocks, iron gates rusted shut,
dark fantasy gothic architecture, imposing scale
```

**神殿内部**
```
dark temple interior, high vaulted ceiling,
rows of stone columns disappearing into shadow,
ancient murals faded on walls, candle niches,
central altar with worn inscription,
dust floating in shafts of cold light from above,
mysterious atmosphere, sacred and foreboding,
dark fantasy, painterly oil painting style
```

### 3.3 裂谷（异常区域）

**裂谷边缘**
```
massive canyon with unnatural geometry,
glowing cracks in rock face, pale ethereal light,
floating debris defying gravity, distorted air,
dead vegetation, crystallized formations,
eerie silence, sense of wrongness,
dark fantasy, cosmic horror undertones,
cold color palette with occasional warm anomaly glow
```

### 3.4 北境霜脊（卢西恩故乡）

**修院外观**
```
mountain monastery, snow-covered stone buildings,
steep slate roofs, frost on windows,
pine forest backdrop, overcast winter sky,
smoke rising from chimps, worn stone steps,
icy paths, distant mountain peaks,
cold blue-white palette, serene but harsh,
northern European medieval monastic architecture
```

**医舍内部**
```
monastery infirmary, simple wooden beds with linen,
herb drying racks, glass bottles on shelves,
brass medical instruments, bandage rolls,
small window with frost patterns, warm firelight,
smell of herbs and antiseptic implied through visuals,
clean ordered space, practical and compassionate,
warm interior light contrasting cold exterior
```

### 3.5 雾港（遗物交易地）

**港口夜景**
```
foggy harbor at night, lantern lights reflecting on water,
wooden docks, moored sailing ships, cargo crates,
fog rolling in from sea, figures in cloaks,
auction house with warm light spilling out,
wet cobblestones, rope coils, anchor chains,
mysterious atmosphere, clandestine meeting,
dark blue fog palette with warm lantern accents
```

### 3.6 关键剧情场景

**黄昏村口（塞西尔初遇）**
```
village entrance at sunset, golden-orange light,
long shadows stretching across path,
lone figure with bow silhouetted against dying light,
dust particles glowing in sunset rays,
tense standoff atmosphere, beautiful and dangerous,
warm sunset palette, cinematic composition
```

**钟楼（无风自鸣事件）**
```
medieval clock tower, bells swinging without wind,
unusual light emanating from clock face,
birds scattering, people looking up in confusion,
cracks appearing in tower stonework,
ominous atmosphere, supernatural event,
dramatic lighting, dark clouds gathering
```

**门前（终局场景）**
```
massive ancient door, covered in inscriptions,
cracks of light seeping through edges,
five figures standing before it, various expressions,
candlelight and shadow play on stone walls,
weight of final decision in the air,
epic composition, emotional climax lighting,
dark fantasy, painterly, cinematic
```

---

## 四、UI 元素 Prompt

### 4.1 对话框

**主对话框**
```
game UI dialogue box, dark fantasy style,
ornate stone frame with worn edges,
parchment texture background, subtle ink stains,
gothic medieval border design, corner flourishes,
dark wood and iron accents,
transparent center for text,
muted dark palette, atmospheric lighting,
PNG with transparency, clean edges
```

**旁白框**
```
narrative text box, minimal design,
aged paper texture, burned edges,
faded ink marks, wax seal accent,
dark background with subtle grain,
elegant serif typography space,
gothic medieval aesthetic, understated
```

**选择框**
```
choice button, medieval scroll design,
worn leather texture, brass button accent,
slightly curled edges, shadow beneath,
hover state: subtle warm glow,
dark fantasy style, tactile appearance,
multiple size variants needed
```

### 4.2 按钮

**通用按钮**
```
game button, medieval metal plate design,
riveted edges, worn patina texture,
subtle engravings, leather strap accent,
dark iron with brass highlights,
pressed state: deeper shadow, slight indent,
gothic fantasy UI element
```

### 4.3 菜单/状态栏

**生命/代价条**
```
health bar UI, medieval manuscript style,
ornate frame with thorny vine motif,
fill: dark red to crimson gradient,
empty state: faded parchment,
numerical display in gothic script,
border: aged metal with patina
```

**隐藏值指示器（抽象）**
```
abstract status indicator, wax seal design,
different stamps for different values:
mercy: soft worn stamp,
obsession: deeply pressed mark,
erosion: cracked and fading,
revelation: glowing faintly,
scripture: ink bleeding outward,
dark fantasy mystical aesthetic
```

### 4.4 图标

**系统图标**
```
game icon set, medieval style, consistent design,
settings: crossed quill and sword,
save: folded parchment with wax seal,
load: hourglass with flowing sand,
inventory: leather satchel,
map: rolled scroll with compass rose,
muted colors, dark outlines, 64x64 or 128x128
```

---

## 五、特效与氛围素材

### 5.1 裂隙效果

```
rift energy effect, ethereal blue-white glow,
crystalline fracture pattern, 
floating particles, distorted space,
cold light with warm anomaly spots,
dark fantasy magic, subtle and ominous,
PNG sprite sheet or animated frames
```

### 5.2 轮回重启效果

```
temporal reset effect, clock hands spinning backward,
ink dissolving from parchment, 
fading afterimages of previous loops,
sepia to cold blue color shift,
dissolve and reform visual,
emotional weight in the visual language
```

### 5.3 雾气/氛围

```
atmospheric fog layers, various densities,
ground mist, rolling fog, thin haze,
cold blue-gray palette, depth variation,
parallax-ready for layered backgrounds,
transparent PNG, tileable horizontal
```

---

## 六、LoRA 训练素材建议

### 角色一致性训练

为保持角色在不同场景中的一致性，建议：

1. **奈尔 LoRA**
   - 训练素材：15-20张不同角度、表情的基础立绘
   - 触发词：`nier_character, silver hair, red eyes, cold expression`
   - 重点保持：发色、瞳色、体型、服装剪影

2. **米迦 LoRA**
   - 训练素材：15-20张，包含笑和严肃两种状态
   - 触发词：`mika_character, brown hair, green eyes, warm expression`
   - 重点保持：圆脸特征、护手布条、锈剑

3. **塞西尔 LoRA**
   - 训练素材：15-20张，注意礼貌笑和冷杀意的对比
   - 触发词：`cecil_character, black hair, purple eyes, polite smile`
   - 重点保持：刘海遮眼、凤眼、弓箭姿态

4. **卡修斯 LoRA**
   - 训练素材：15-20张，突出学者气质
   - 触发词：`cassius_character, red hair, blue eyes, analytical gaze`
   - 重点保持：红发、领口系紧、手记

5. **卢西恩 LoRA**
   - 训练素材：15-20张，温和与疲惫的对比
   - 触发词：`lucien_character, blonde hair, gray eyes, gentle expression`
   - 重点保持：亚麻色发、药箱、卷袖

---

## 七、生成工作流建议

### 工具选择优先级

1. **ComfyUI + VNCCS**（推荐）
   - 专为视觉小说设计
   - 角色一致性工作流
   - 本地部署，完全免费

2. **Stable Diffusion WebUI**
   - 灵活性高
   - ControlNet支持好
   - 适合精细调整

3. **在线服务**
   - Midjourney：适合概念设计阶段
   - Leonardo.ai：有游戏资产专用功能
   - Tensor.Art：免费额度，社区模型

### 生成顺序建议

1. 先确定画风，生成测试图验证提示词效果
2. 为每个角色生成基础立绘（全身、正面、默认表情）
3. 基于基础图生成表情变体（至少5种核心表情）
4. 生成关键剧情场景的背景图
5. 设计UI元素，确保风格统一
6. 训练角色LoRA以保持一致性
7. 批量生成分支场景素材

### 质量检查清单

- [ ] 角色发色/瞳色是否符合设定
- [ ] 服装细节是否准确（护手布条、旧墨绳、磨石袋等）
- [ ] 表情是否传达正确情绪
- [ ] 背景氛围是否符合世界观（西幻中世纪基调）
- [ ] UI元素风格是否统一
- [ ] 整体色调是否保持暗沉、冷调的基调

---

## 八、参考资源

### 风格参考作品
- **Darkest Dungeon**：暗黑奇幻、压抑氛围、手绘质感
- **Blasphemous**：宗教神秘感、痛苦美学、精细像素
- **Castlevania（Netflix）**：哥特美学、流畅角色设计
- **Dishonored**：蒸汽朋克与奇幻混合、城市氛围
- **The Banner Saga**：手绘动画、史诗感、行旅氛围

### 免费资源网站
- **OpenGameArt**：CC0协议的游戏素材
- **Kenney**：高质量免费游戏资产
- **Freesound**：免费音效
- **Pixabay/Pexels**：免费图片素材（用于参考或纹理）

---

*此文档基于《雾灯残页》设定集生成，如有设定更新请同步修订。*
*最后更新：2026-05-25*
