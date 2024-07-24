from utils.const import LANGUAGE

### ========== CONSTANT ========== ###

category_tag = "multi-location"

question_pool = [
    {
        LANGUAGE.EN_US: f"Where is [dt] located relative to [rf]?",
        LANGUAGE.ZH_CN: f"[dt]是在[rf]的哪边?",
        LANGUAGE.ZH_HK: f"[dt]喺在[rf]的邊度?",
    },
    {
        LANGUAGE.EN_US: f"What is the position of [dt] in relation to [rf]?",
        LANGUAGE.ZH_CN: f"[dt]相对于[rf]的位置是什么？",
        LANGUAGE.ZH_HK: f"[dt]相對于[rf]嘅位置係乜嘢？",
    },
        {
        LANGUAGE.EN_US: f"How is [dt] situated compared to [rf]?",
        LANGUAGE.ZH_CN: f"与[rf]相比，[dt]的位置如何？",
        LANGUAGE.ZH_HK: f"與[rf]相比，[dt]的位置如何？",
    },
        {
        LANGUAGE.EN_US: f"Where can [dt] be found in relation to [rf]?",
        LANGUAGE.ZH_CN: f"在哪里可以找到与[rf]相关的 [dt]？",
        LANGUAGE.ZH_HK: f"喺邊度可以搵到與[rf]相關嘅[dt]？",
    },
    {
        LANGUAGE.EN_US: f"How do I reach [dt] from [rf]?",
        LANGUAGE.ZH_CN: f"我怎样可以从[rf]摸到[dt]?",
        LANGUAGE.ZH_HK: f"我點樣可以由[rf]揾到[dt]?",
    },
        {
        LANGUAGE.EN_US: f"What is the way to get to [dt] from [rf]?",
        LANGUAGE.ZH_CN: f"从[rf]到达[dt]的方法是什么？",
        LANGUAGE.ZH_HK: f"從[rf]到達[dt]的方法是什麼？",
    },
        {
        LANGUAGE.EN_US: f"How can I get to [dt] starting from [rf]?",
        LANGUAGE.ZH_CN: f"如何从[rf]开始到达[dt]？",
        LANGUAGE.ZH_HK: f"如何由[rf]開始到達[dt]？",
    },
        {
        LANGUAGE.EN_US: f"What route should I take to go from [rf] to [dt]?",
        LANGUAGE.ZH_CN: f"我应该走什么路线从[rf]到[dt]？",
        LANGUAGE.ZH_HK: f"我應該走乜嘢路線由[rf]到[dt]？",
    },
    {
        LANGUAGE.EN_US: f"Can you point me towards [dt] from where [rf] is?",
        LANGUAGE.ZH_CN: f"你能否指引我怎样从[rf]到[dt]?",
        LANGUAGE.ZH_HK: f"你可以指俾我睇，由[rf]點樣揾到[dt]?",
    },
        {
        LANGUAGE.EN_US: f"Can you direct me to [dt] from [rf]'s location?",
        LANGUAGE.ZH_CN: f"你能把我从[rf]的位置引导到[dt]吗？",
        LANGUAGE.ZH_HK: f"你能把我從[rf]的位置引導到[dt]嗎？",
    },
        {
        LANGUAGE.EN_US: f"Can you show me the way to [dt] from [rf]?",
        LANGUAGE.ZH_CN: f"你能告诉我从[rf]到[dt]的方法吗？",
        LANGUAGE.ZH_HK: f"你可唔可以話我由[rf]到[dt]嘅方法啊？",
    },
        {
        LANGUAGE.EN_US: f"Can you guide me to [dt] starting from [rf]?",
        LANGUAGE.ZH_CN: f"你能引导我从[rf]到[dt]吗？",
        LANGUAGE.ZH_HK: f"你能引導我從[rf]到[dt]嗎？",
    },
    {
        LANGUAGE.EN_US: f"From [rf], which direction should I move to find [dt]?",
        LANGUAGE.ZH_CN: f"我从[rf]开始往哪个方向移动可以到[dt]?",
        LANGUAGE.ZH_HK: f"我由[rf]要行邊個方向去揾[dt]?",
    },
        {
        LANGUAGE.EN_US: f"Which way should I go from [rf] to reach [dt]?",
        LANGUAGE.ZH_CN: f"从[rf]到[dt]的路是哪条？",
        LANGUAGE.ZH_HK: f"由[rf]到[dt]嘅路係邊條？",
    },
        {
        LANGUAGE.EN_US: f"What direction should I take from [rf] to get to [dt]?",
        LANGUAGE.ZH_CN: f"我应该从[rf]往什么方向走才能到达[dt]？",
        LANGUAGE.ZH_HK: f"我应该从[rf]往什么方向走才能到达[dt]？",
    },
        {
        LANGUAGE.EN_US: f"In which direction should I head from [rf] to locate [dt]?",
        LANGUAGE.ZH_CN: f"我应该从[rf]朝哪个方向移动才能找到[dt]？",
        LANGUAGE.ZH_HK: f"我應該從[rf]朝哪個方向移動才能找到[dt]？",
    },
    {
        LANGUAGE.EN_US: f"If I'm facing [rf], in which direction is [dt]?",
        LANGUAGE.ZH_CN: f"我现在正面对[rf], [dt]在哪个方向?",
        LANGUAGE.ZH_HK: f"我對住[rf], [dt]喺邊個方向？",
    },
        {
        LANGUAGE.EN_US: f"If [rf] is in front of me, where is [dt] located?",
        LANGUAGE.ZH_CN: f"如果[rf]在我面前，[dt]在哪里？",
        LANGUAGE.ZH_HK: f"如果[rf]在我面前，[dt]喺邊度？",
    },
        {
        LANGUAGE.EN_US: f"Facing [rf], which way is [dt]?",
        LANGUAGE.ZH_CN: f"面对[rf]，[dt]是哪个方向？",
        LANGUAGE.ZH_HK: f"面對[rf]，[dt]係邊個方向？",
    },
        {
        LANGUAGE.EN_US: f"When looking at [rf], where is [dt]?",
        LANGUAGE.ZH_CN: f"当看着[rf]时，[dt]在哪里？",
        LANGUAGE.ZH_HK: f"當睇住[rf]時，[dt]在哪裡？",
    },
    {
        LANGUAGE.EN_US: f"If [rf] is in front of me, where should I look for [dt]?",
        LANGUAGE.ZH_CN: f"如果[rf]在我正前方，我应该往哪边找[dt]?",
        LANGUAGE.ZH_HK: f"[rf]喺在我面前，我應該望邊度搵[dt]?",
    },
        {
        LANGUAGE.EN_US: f"If [rf] is ahead of me, where can I find [dt]?",
        LANGUAGE.ZH_CN: f"如果[rf]在我前面，我在哪里可以找到[dt]？",
        LANGUAGE.ZH_HK: f"如果[rf]喺我前面，我喺邊度可以搵到[dt]？",
    },
        {
        LANGUAGE.EN_US: f"With [rf] in front, where should I search for [dt]?",
        LANGUAGE.ZH_CN: f"前面有[rf]，我应该在哪里搜索[dt]？",
        LANGUAGE.ZH_HK: f"前面有[rf]，我應該喺邊度搜索[dt]？",
    },
        {
        LANGUAGE.EN_US: f"If [rf] is directly ahead, where is [dt] located?",
        LANGUAGE.ZH_CN: f"如果[rf]在正前方，那么[dt]在哪里？",
        LANGUAGE.ZH_HK: f"如果[rf]在正前方，咁[dt]喺邊度？",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ==========
# scene_tag = "bathroom"
# frame_num = [44, 49, 170, 500, 505, 509, 656]
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# item_lists = [
#     [['toilet', 'sink'], ['toothbrush', 'sink'], ['cup', 'toothbrush']],
#     [['toilet', 'sink'], ['toothbrush', 'toothpaste'], ['bottle', 'toothbrush']],
#     [['toilet', 'sink'], ['person', 'sink'], ['person', 'toilet']],
#     [['toilet', 'sink'], ['toothbrush', 'sink'], ['person', 'sink']],
#     [['toilet', 'sink'], ['bottle', 'sink'], ['bottle', 'toilet']],
#     [['toothbrush', 'sink'], ['toothbrush', 'bottle'], ['sink', 'bottle']],
#     [['toilet', 'sink'], ['bottle', 'toilet'], ['cup', 'sink']]
# ]

# # change
# answer_keys = [
#     ['down and left', 'up and left', 'right'],
#     ['down and left', 'left', 'left'],
#     ['down and left', 'up', 'up and right'],
#     ['down and right', 'left', 'up'],
#     ['down and left', 'up and left', 'up and right'],
#     ['up', 'up and right', 'up and right'],
#     ['down and left', 'up', 'left']
# ]

# ========== bedroom ========== #
# scene_tag = "bedroom" # change
# frame_num = [70, 176, 178, 181, 281, 401, 525, 946] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change 
# item_lists = [
#     [['vase', 'bed'], ['potted plant', 'vase'], ['dog', 'potted plant']],
#     [['backpack', 'bed'], ['handbag', 'book'], ['book', 'bed']],
#     [['chair', 'bed'], ['backpack', 'couch'], ['cup', 'chair']],
#     [['keyboard', 'bed'], ['backpack', 'bed'], ['remote', 'tv']],
#     [['teddy bear', 'bed'], ['cup', 'bed'], ['cup', 'teddy bear']],
#     [['teddy bear', 'bed'], ['chair', 'bed']],
#     [['laptop', 'bed'], ['backpack', 'bed'], ['bed', 'dining table']],
#     [['tv', 'bed'], ['chair', 'bed'], ['mouse', 'book']]
# ]

# # change
# answer_keys = [
#     ['up and left', 'up', 'down and right'],
#     ['left', 'down and right', 'left'],
#     ['right', 'down and left', 'left'],
#     ['up and right', 'center', 'down and left'],
#     ['up', 'up and right', 'right'],
#     ['down and left', 'down and left'],
#     ['up and right', 'right', 'down and left'],
#     ['up and right', 'right', 'left']
# ]

# ========== dining room ========== #
# scene_tag = "dining_room" # change
# frame_num = [54, 746, 757, 783, 824, 852, 879, 880, 1436] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['laptop', 'dining table'], ['bottle', 'laptop'], ['microwave', 'bowl']],
#     [['microwave', 'chair'], ['toaster', 'microwave'], ['bottle', 'toaster']],
#     [['dining table', 'sink'], ['sink', 'tv'], ['cup', 'dining table']],
#     [['bottle', 'backpack'], ['cup', 'backpack'], ['bottle', 'bowl']],
#     [['dining table', 'refrigerator'], ['potted plant', 'dining table'], ['bowl', 'potted plant']],
#     [['banana', 'dining table'], ['sink', 'banana'], ['bottle', 'sink']],
#     [['tv', 'dining table'], ['potted plant', 'dining table'], ['tv', 'chair']],
#     [['microwave', 'oven'], ['oven', 'dining table'], ['chair', 'dining table']],
#     [['vase', 'dining table'], ['potted plant', 'dining table'], ['vase', 'chair']]
# ]

# # change
# answer_keys = [
#     ['center', 'up and right', 'up and right'],
#     ['up and left', 'down', 'left'],
#     ['down and right', 'down and left', 'up and left'],
#     ['right', 'right', 'left'],
#     ['left', 'up', 'down'],
#     ['center', 'up and left', 'right'],
#     ['up and right', 'up', 'up and right'],
#     ['up', 'up and right', 'down and right'],
#     ['center', 'up', 'left']
# ]

# ========== doorway ========== #
# scene_tag = "doorway" # change
# frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['microwave', 'book'], ['bowl', 'microwave'], ['wine glass', 'book']],
#     [['sink', 'oven'], ['refrigerator', 'oven'], ['couch', 'sink']],
#     [['vase', 'tv'], ['book', 'tv'], ['tv', 'keyboard']],
#     [['microwave', 'chair'], ['refrigerator', 'chair'], ['dining table', 'microwave']],
#     [['potted plant', 'chair'], ['dining table', 'chair'], ['tv', 'dining table']],
#     [['potted plant', 'tv'], ['chair', 'potted plant'], ['potted plant', 'vase']],
#     [['tv', 'couch'], ['keyboard', 'tv'], ['book', 'couch']],
#     [['microwave', 'person'], ['oven', 'refrigerator'], ['oven', 'microwave']],
#     [['person', 'dog'], ['sink', 'person'], ['bowl', 'sink']]
# ]

# # change
# answer_keys = [
#     ['up', 'down and right', 'up and right'],
#     ['left', 'right', 'up and right'],
#     ['left', 'left', 'up'],
#     ['up', 'up and left', 'down and left'],
#     ['up and left', 'down and right', 'up and left'],
#     ['up and left', 'down and right', 'up'],
#     ['up', 'down and left', 'up and left'],
#     ['left', 'left', 'down'],
#     ['up', 'down and right', 'up']
# ]

# ========== kitchen ========== #
# scene_tag = "kitchen" # change
# frame_num = [138, 139, 199, 203, 204, 253, 560, 849] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['microwave', 'oven'], ['oven', 'bowl'], ['bowl', 'sink']],
#     [['bowl', 'microwave'], ['knife', 'bottle'], ['bottle', 'oven']],
#     [['knife', 'oven'], ['cup', 'oven'], ['bowl', 'oven']],
#     [['oven', 'microwave'], ['sink', 'oven'], ['cup', 'sink']],
#     [['toothbrush', 'sink'], ['wine glass', 'sink'], ['cup', 'wine glass']],
#     [['microwave', 'sink'], ['sink', 'refrigerator'], ['bottle', 'oven']],
#     [['sink', 'microwave'], ['oven', 'sink'], ['bottle', 'oven']],
#     [['toaster', 'sink'], ['bowl', 'oven'], ['bowl', 'sink']]
# ]

# # change
# answer_keys = [
#     ['up', 'left', 'left'],
#     ['right', 'up and right', 'up and left'],
#     ['up', 'right', 'down and right'],
#     ['down', 'down and left', 'right'],
#     ['up and right', 'center', 'left'],
#     ['up and left', 'right', 'up'],
#     ['right', 'down and left', 'up and right'],
#     ['up and right', 'left', 'up and right']
# ]

# ========== living room ========== #
# scene_tag = "living_room" # change
# frame_num = [50, 156, 166, 200, 201, 261, 350, 356, 583, 1304] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['potted plant', 'couch'], ['book', 'couch'], ['book', 'potted plant']],
#     [['tv', 'couch'], ['remote', 'couch'], ['remote', 'tv']],
#     [['vase', 'dining table'], ['dining table', 'couch'], ['chair', 'couch']],
#     [['bottle', 'dining table'], ['chair', 'dining table'], ['tv', 'dining table']],
#     [['tv', 'dining table'], ['tv', 'book'], ['dining table', 'chair']],
#     [['laptop', 'couch'], ['potted plant', 'couch'], ['bowl', 'laptop']],
#     [['bicycle', 'chair'], ['keyboard', 'chair'], ['potted plant', 'bicycle']],
#     [['tv', 'potted plant'], ['book', 'tv'], ['potted plant', 'couch']],
#     [['backpack', 'tv'], ['tv', 'couch'], ['remote', 'backpack']],
#     [['vase', 'couch'], ['potted plant', 'chair'], ['book', 'vase']]
# ]

# # change
# answer_keys = [
#     ['up and left', 'center', 'down and right'],
#     ['up and left', 'left', 'down'],
#     ['up', 'up', 'up'],
#     ['up and left', 'up and right', 'up and right'],
#     ['up and right', 'left', 'down'],
#     ['down and left', 'up and right', 'left'],
#     ['left', 'up', 'up and right'],
#     ['up and right', 'left', 'down'],
#     ['down and right', 'up and left', 'down and left'],
#     ['right', 'down and left', 'down and left']
# ]

# ========== playroom ========== #
scene_tag = "playroom" # change
frame_num = [425, 426, 428, 437, 1081, 1084, 1157, 1203] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# change
item_lists = [
    [['sports ball', 'chair'], ['backpack', 'sports ball'], ['backpack', 'dining table']],
    [['tv', 'couch'], ['couch', 'chair'], ['sports ball', 'tv']],
    [['suitcase', 'couch'], ['chair', 'couch'], ['couch', 'dining table']],
    [['tv', 'chair'], ['teddy bear', 'tv'], ['chair', 'dog']],
    [['chair', 'bed'], ['book', 'bed'], ['book', 'chair']],
    [['tv', 'chair'], ['chair', 'book'], ['remote', 'tv']],
    [['teddy bear', 'bed'], ['book', 'backpack'], ['teddy bear', 'book']],
    [['backpack', 'couch'], ['suitcase', 'couch'], ['backpack', 'chair']]
]

# change
answer_keys = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# ========== lobby ========== #
# scene_tag = "lobby" # change
# frame_num = [9, 36, 619, 625, 1251, 1253] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['bottle', 'chair'], ['chair', 'tv']],
#     [['clock', 'couch'], ['dining table', 'chair'], ['chair', 'couch']],
#     [['vase', 'couch'], ['potted plant', 'chair']],
#     [['tv', 'chair'], ['microwave', 'tv'], ['backpack', 'chair']],
#     [['couch', 'tv'], ['book', 'tv'], ['book', 'chair']],
#     [['book', 'couch'], ['dining table', 'couch'], ['dining table', 'book']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== meeting room ========== #
# scene_tag = "meeting_room" # change
# frame_num = [5, 27, 39, 341] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['dining table', 'chair'], ['microwave', 'dining table'], ['microwave', 'chair']],
#     [['tv', 'chair'], ['mouse', 'tv'], ['mouse', 'bottle']],
#     [['dining table', 'chair']],
#     [['potted plant', 'dining table'], ['vase', 'chair'], ['potted plant', 'vase']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== pantry ========== #
# scene_tag = "pantry" # change
# frame_num = [1, 410, 412, 415, 417] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['microwave', 'refrigerator'], ['microwave', 'chair'], ['sink', 'microwave']],
#     [['microwave', 'sink'], ['microwave', 'bottle'], ['sink', 'bottle']],
#     [['dining table', 'refrigerator'], ['sink', 'dining table'], ['toaster', 'sink']],
#     [['refrigerator', 'dining table'], ['cup', 'refrigerator'], ['chair', 'refrigerator']],
#     [['sink', 'chair'], ['cell phone', 'chair'], ['cell phone', 'handbag']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== workstation ========== #
# scene_tag = "workstation" # change
# frame_num = [4, 23, 371, 388, 393, 453, 455, 474] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['cup', 'bottle'], ['laptop', 'cup'], ['laptop', 'chair']],
#     [['laptop', 'chair'], ['clock', 'laptop'], ['book', 'laptop']],
#     [['laptop', 'chair'], ['keyboard', 'laptop'], ['cup', 'chair']],
#     [['tv', 'chair'], ['handbag', 'chair'], ['book', 'handbag']],
#     [['chair', 'backpack'], ['remote', 'book'], ['laptop', 'remote']],
#     [['clock', 'chair'], ['book', 'clock'], ['laptop', 'clock']],
#     [['tv', 'chair'], ['potted plant', 'chair'], ['laptop', 'potted plant']],
#     [['dining table', 'chair'], ['keyboard', 'chair'], ['couch', 'chair']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== bookstore ========== #
# scene_tag = "bookstore" # change
# frame_num = [88, 89, 91, 112, 119] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['clock', 'book']],
#     [['bottle', 'book']],
#     [['backpack', 'chair'], ['suitcase', 'chair']],
#     [['laptop', 'book'], ['tv', 'book'], ['mouse', 'keyboard']],
#     [['chair', 'book'], ['dining table', 'chair'], ['book', 'dining table']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== classroom ========== #
# scene_tag = "classroom" # change
# frame_num = [297, 301, 323, 325, 326] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['backpack', 'dining table'], ['laptop', 'backpack'], ['book', 'laptop']],
#     [['keyboard', 'tv'], ['laptop', 'tv'], ['keyboard', 'chair']],
#     [['teddy bear', 'chair'], ['book', 'chair'], ['book', 'teddy bear']],
#     [['chair', 'couch']],
#     [['sink', 'chair'], ['dining table', 'chair'], ['bottle', 'sink']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== coffee shop ========== #
# scene_tag = "coffee_shop" # change
# frame_num = [120, 122, 123, 223, 225, 228, 238, 244] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['dining table', 'bench'], ['potted plant', 'dining table'], ['chair', 'bench']],
#     [['potted plant', 'bottle'], ['toaster', 'potted plant'], ['vase', 'potted plant']],
#     [['person', 'toaster'], ['toaster', 'potted plant'], ['potted plant', 'person']],
#     [['couch', 'chair'], ['dining table', 'couch']],
#     [['person', 'couch'], ['dining table', 'couch'], ['cup', 'dining table']],
#     [['bowl', 'person'], ['bowl', 'dining table'], ['cup', 'bowl']],
#     [['chair', 'dining table'], ['bowl', 'dining table'], ['person', 'chair']],
#     [['chair', 'couch'], ['person', 'chair'], ['dining table', 'couch']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# ========== computer lab ========== #
# scene_tag = "computer lab" # change
# frame_num = [272, 279, 333, 335, 337, 338] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['person', 'tv'], ['mouse', 'keyboard'], ['chair', 'tv']],
#     [['keyboard', 'tv'], ['chair', 'tv']],
#     [['tv', 'keyboard'], ['mouse', 'keyboard'], ['chair', 'tv']],
#     [['tv', 'chair'], ['keyboard', 'chair'], ['keyboard', 'tv']],
#     [['tv', 'keyboard'], ['tv', 'chair'], ['mouse', 'keyboard']],
#     [['book', 'tv'], ['keyboard', 'chair'], ['tv', 'chair']]
# ]

# ========== dorm ========== #
# scene_tag = "dorm" # change
# frame_num = [128, 130, 131, 143, 267, 569] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     [['bottle', 'cup'], ['spoon', 'bottle'], ['oven', 'spoon']],
#     [['sink', 'oven'], ['refrigerator', 'sink'], ['bottle', 'refrigerator']],
#     [['microwave', 'oven'], ['refrigerator', 'microwave'], ['knife', 'oven']],
#     [['bowl', 'sink'], ['spoon', 'bowl'], ['cup', 'spoon']],
#     [['refrigerator', 'person'], ['person', 'oven'], ['bottle', 'person']],
#     [['banana', 'oven'], ['refrigerator', 'oven'], ['microwave', 'banana']]
# ]

# # change
# answer_keys = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]
