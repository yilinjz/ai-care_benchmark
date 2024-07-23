from utils.const import LANGUAGE

### ========== CONSTANT ========== ###

category_tag = "location"

question_pool = [
    {
        LANGUAGE.EN_US: f"Can you locate the [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你能在场景中找到[dt]吗？",
        LANGUAGE.ZH_HK: f"你可以喺房入面搵到[dt]嗎?",
    },
    {
        LANGUAGE.EN_US: f"Can you find the [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你能在场景中找到[dt]吗？",
        LANGUAGE.ZH_HK: f"你可唔可以喺場景中搵到[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Are you able to locate the [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你能在场景中找到[dt]吗？",
        LANGUAGE.ZH_HK: f"你可唔可以喺場景中搵到[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Can you point out the [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你能指出场景中的[dt]吗？",
        LANGUAGE.ZH_HK: f"你可唔可以指出場景中嘅[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Is the [dt] visible in the scene?",
        LANGUAGE.ZH_CN: f"[dt]在场景中是否可见？",
        LANGUAGE.ZH_HK: f"[dt]在場景中是否可見？",
    },
    {
        LANGUAGE.EN_US: f"Can you identify where the [dt] is in the scene?",
        LANGUAGE.ZH_CN: f"你能确定[dt]在场景中的位置吗？",
        LANGUAGE.ZH_HK: f"你能肯定[dt]喺場景中嘅位置呀？",
    },
    {
        LANGUAGE.EN_US: f"Where is the closest [dt] in relation to me?",
        LANGUAGE.ZH_CN: f"离我最近的[dt]在哪里?",
        LANGUAGE.ZH_HK: f"離我最近嘅[dt]喺邊度？",
    },
    {
        LANGUAGE.EN_US: f"Where is the nearest [dt] to me?",
        LANGUAGE.ZH_CN: f"离我最近的[dt]在哪里？",
        LANGUAGE.ZH_HK: f"離我最近嘅[dt]喺邊度？",
    },
    {
        LANGUAGE.EN_US: f"Can you tell me the location of the closest [dt] to me?",
        LANGUAGE.ZH_CN: f"你能告诉我离我最近的[dt]的位置吗？",
        LANGUAGE.ZH_HK: f"你可唔可以話我离我最近嘅[dt]嘅位置啊？",
    },
    {
        LANGUAGE.EN_US: f"Where is the [dt] that is closest to me?",
        LANGUAGE.ZH_CN: f"离我最近的[dt]在哪里？",
        LANGUAGE.ZH_HK: f"離我最近嘅[dt]喺邊度？",
    },
    {
        LANGUAGE.EN_US: f"What is the position of the nearest [dt] relative to me?",
        LANGUAGE.ZH_CN: f"离我最近的[dt]的位置是什么？",
        LANGUAGE.ZH_HK: f"離我最近嘅[dt]嘅位置係乜嘢？",
    },
    {
        LANGUAGE.EN_US: f"Where can I find the closest [dt] to me?",
        LANGUAGE.ZH_CN: f"在哪里可以找到离我最近的[dt]？",
        LANGUAGE.ZH_HK: f"喺邊度可以搵到離我最近嘅[dt]？",
    },
    {
        LANGUAGE.EN_US: f"In which direction is the [dt] from my current position?",
        LANGUAGE.ZH_CN: f"[dt]在我当前位置的什么方向?",
        LANGUAGE.ZH_HK: f"[dt]由我而家嘅位置喺邊個方向？",
    },
    {
        LANGUAGE.EN_US: f"Which direction is the [dt] located from where I am now?",
        LANGUAGE.ZH_CN: f"[dt]位于我现在所在的哪个方向？",
        LANGUAGE.ZH_HK: f"[dt]位於我而家所在嘅邊個方向？",
    },
    {
        LANGUAGE.EN_US: f"From my current position, which way is the [dt]?",
        LANGUAGE.ZH_CN: f"从我目前的位置来看，[dt]是哪个方向？",
        LANGUAGE.ZH_HK: f"從我目前的位置來看，[dt]是邊個方向？",
    },
    {
        LANGUAGE.EN_US: f"Can you tell me the direction of the [dt] from my current location?",
        LANGUAGE.ZH_CN: f"你能告诉我[dt]相对于我当前位置的方向吗？",
        LANGUAGE.ZH_HK: f"你能告訴我[dt]相對于我當前位置的方向嗎？",
    },
    {
        LANGUAGE.EN_US: f"Where is the [dt] in relation to my current position?",
        LANGUAGE.ZH_CN: f"相对于我当前位置，[dt]在哪里？",
        LANGUAGE.ZH_HK: f"相對于我當前位置，[dt]喺邊度？",
    },
    {
        LANGUAGE.EN_US: f"Which way should I look to find the [dt] from here?",
        LANGUAGE.ZH_CN: f"我应该从这里往哪个方向寻找[dt]？",
        LANGUAGE.ZH_HK: f"我應該從這裡往哪個方向尋找[dt]？",
    },
    {
        LANGUAGE.EN_US: f"Find where the [dt] is, please.",
        LANGUAGE.ZH_CN: f"请帮我找下[dt]在哪里。",
        LANGUAGE.ZH_HK: f"請幫我搵吓[dt]喺邊。",
    },
    {
        LANGUAGE.EN_US: f"Can you please locate the [dt]?",
        LANGUAGE.ZH_CN: f"你能找到[dt]吗？",
        LANGUAGE.ZH_HK: f"你可唔可以搵到[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Please find the location of the [dt].",
        LANGUAGE.ZH_CN: f"请找到[dt]的位置。",
        LANGUAGE.ZH_HK: f"請搵到[dt]嘅位置。",
    },
    {
        LANGUAGE.EN_US: f"Could you identify where the [dt] is?",
        LANGUAGE.ZH_CN: f"你能确定[dt]在哪里吗？",
        LANGUAGE.ZH_HK: f"你能肯定[dt]喺邊度呀？",
    },
    {
        LANGUAGE.EN_US: f"Please tell me where the [dt] is.",
        LANGUAGE.ZH_CN: f"请告诉我[dt]在哪里。",
        LANGUAGE.ZH_HK: f"請告訴我[dt]喺邊度。",
    },
    {
        LANGUAGE.EN_US: f"Can you show me where the [dt] is?",
        LANGUAGE.ZH_CN: f"你能告诉我[dt]在哪里吗？",
        LANGUAGE.ZH_HK: f"你可唔可以話我[dt]喺邊度啊？",
    },
    {
        LANGUAGE.EN_US: f"Could you guide me to the position of the [dt]?",
        LANGUAGE.ZH_CN: f"你可以引导我去到[dt]的位置嗎?",
        LANGUAGE.ZH_HK: f"你可以引導我去到[dt]嘅位置嗎？",
    },
    {
        LANGUAGE.EN_US: f"Can you direct me to the location of the [dt]?",
        LANGUAGE.ZH_CN: f"你能把我引向[dt]的位置吗？",
        LANGUAGE.ZH_HK: f"你能把我引向[dt]的位置嗎？",
    },
    {
        LANGUAGE.EN_US: f"Could you show me where the [dt] is?",
        LANGUAGE.ZH_CN: f"你能告诉我[dt]在哪里吗？",
        LANGUAGE.ZH_HK: f"你可唔可以話我[dt]喺邊度啊？",
    },
    {
        LANGUAGE.EN_US: f"Can you help me find the position of the [dt]?",
        LANGUAGE.ZH_CN: f"你能帮我找到[dt]的位置吗？",
        LANGUAGE.ZH_HK: f"你可唔可以帮我搵到[dt]的位置吗？",
    },
    {
        LANGUAGE.EN_US: f"Could you point out the location of the [dt] to me?",
        LANGUAGE.ZH_CN: f"你能给我指出[dt]的位置吗？",
        LANGUAGE.ZH_HK: f"你可唔可以畀我指出[dt]嘅位置啊？",
    },
    {
        LANGUAGE.EN_US: f"Can you guide me to where the [dt] is located?",
        LANGUAGE.ZH_CN: f"你能引导我到[dt]的位置吗？",
        LANGUAGE.ZH_HK: f"你能引導我到[dt]的位置嗎？",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ========== #
# scene_tag = "bathroom" # change
# frame_num = [44, 49, 170, 500, 505, 509, 656] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['toothbrush', 'toilet', 'sink', 'cup'],
#     ['toothbrush', 'sink', 'toilet', 'bottle'],
#     ['toilet', 'sink', 'bottle', 'person'],
#     ['bottle', 'toothbrush', 'sink', 'toilet'],
#     ['toilet', 'bottle', 'sink', 'toothbrush'],
#     ['cup', 'toothbrush', 'sink', 'bottle'],
#     ['cup', 'sink', 'bottle', 'toilet']
# ]

# ========== bedroom ========== #
# scene_tag = "bedroom" # change
# frame_num = [70, 176, 178, 181, 281, 401, 525, 946] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bed', 'vase', 'potted plant', 'dog'],
#     ['backpack', 'book', 'bed', 'handbag'],
#     ['couch', 'bed', 'chair', 'backpack'],
#     ['keyboard', 'remote', 'tv', 'book'],
#     ['bed', 'teddy bear', 'chair', 'cup'],
#     ['bed', 'teddy bear', 'chair'],
#     ['laptop', 'dining table', 'bed', 'backpack'],
#     ['bed', 'chair', 'tv', 'mouse']
# ]

# ========== dining room ========== #
# scene_tag = "dining_room" # change
# frame_num = [54, 746, 757, 783, 824, 852, 879, 880, 1436] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['laptop', 'chair', 'book', 'bottle'], 
#     ['toaster', 'bottle', 'chair', 'microwave'],
#     ['dining table', 'chair', 'tv', 'sink'],
#     ['bottle', 'cup', 'bowl', 'backpack'],
#     ['bowl', 'refrigerator', 'potted plant', 'chair'],
#     ['banana', 'dining table', 'bowl', 'sink'],
#     ['chair', 'vase', 'tv', 'dining table'],
#     ['microwave', 'oven', 'dining table', 'chair'],
#     ['dining table', 'chair', 'vase', 'potted plant']
# ]

# ========== doorway ========== #
scene_tag = "doorway" # change
frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# change
item_lists = [
    ['microwave', 'wine glass', 'book', 'bowl'], 
    ['refrigerator', 'sink', 'oven', 'couch'],
    ['vase', 'tv', 'book', 'potted plant'],
    ['chair', 'microwave', 'refrigerator', 'cup'],
    ['potted plant', 'chair', 'tv', 'dining table'],
    ['potted plant', 'chair', 'vase'],
    ['tv', 'couch', 'keyboard', 'book'],
    ['person', 'microwave', 'oven', 'refrigerator'],
    ['person', 'dog', 'sink', 'bowl']
]

# ========== kitchen ========== #
# scene_tag = "kitchen" # change
# frame_num = [138, 139, 199, 203, 204, 253, 560, 849] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['sink', 'bowl', 'microwave', 'oven'], 
#     ['microwave', 'knife', 'bowl', 'bottle'],
#     ['cup', 'bowl', 'oven', 'knife'],
#     ['sink', 'microwave', 'oven', 'cup'],
#     ['refrigerator', 'bowl', 'wine glass', 'toothbrush'],
#     ['refrigerator', 'bottle', 'microwave', 'sink'],
#     ['microwave', 'sink', 'bottle'],
#     ['toaster', 'bowl', 'sink', 'bowl']
# ]

# ========== living room ========== #
# scene_tag = "living_room" # change
# frame_num = [50, 156, 166, 200, 201, 261, 350, 356, 583, 1304] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['couch', 'potted plant', 'book', 'tv'], 
#     ['tv', 'chair', 'remote', 'couch'],
#     ['dining table', 'vase', 'chair', 'handbag'],
#     ['tv', 'bottle', 'chair', 'cup'],
#     ['couch', 'tv', 'dining table', 'book'],
#     ['laptop', 'clock', 'bowl', 'potted plant'],
#     ['potted plant', 'chair', 'bicycle', 'keyboard'],
#     ['couch', 'book', 'potted plant', 'tv'],
#     ['backpack', 'couch', 'remote', 'tv'],
#     ['couch', 'vase', 'book', 'chair']
# ]

# ========== playroom ========== #
# scene_tag = "playroom" # change
# frame_num = [425, 426, 428, 437, 1081, 1084, 1157, 1203] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['sports ball', 'backpack', 'chair'],
#     ['couch', 'tv', 'sports ball', 'chair'],
#     ['suitcase', 'dining table', 'couch', 'chair'],
#     ['teddy bear', 'tv', 'chair'],
#     ['bed', 'book', 'chair'],
#     ['chair', 'book', 'remote', 'tv'],
#     ['chair', 'backpack', 'teddy bear', 'bed'],
#     ['suitcase', 'backpack', 'couch']
# ]

# ========== lobby ========== #
# scene_tag = "lobby" # change
# frame_num = [9, 36, 619, 625, 1251, 1253] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['refrigerator', 'tv', 'bottle', 'chair'],
#     ['couch', 'clock', 'dining table', 'chair'],
#     ['potted plant', 'couch', 'vase'],
#     ['chair', 'backpack', 'bottle', 'microwave'],
#     ['couch', 'book', 'tv'],
#     ['potted plant', 'book', 'couch']
# ]

# ========== meeting room ========== #
# scene_tag = "meeting_room" # change
# frame_num = [5, 27, 39, 341] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['dining table', 'chair'],
#     ['chair', 'dining table', 'bottle'],
#     ['chair', 'dining table'],
#     ['potted plant', 'chair', 'dining table']
# ]

# ========== pantry ========== #
# scene_tag = "pantry" # change
# frame_num = [1, 410, 412, 415, 417] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['refrigerator', 'chair', 'microwave', 'sink'],
#     ['sink', 'bottle', 'cup', 'microwave'],
#     ['dining table', 'toaster', 'clock', 'sink'],
#     ['cup', 'chair', 'refrigerator', 'dining table'],
#     ['cell phone', 'handbag', 'chair', 'sink']
# ]

# ========== workstation ========== #
# scene_tag = "workstation" # change
# frame_num = [4, 23, 371, 388, 393, 453, 455, 474] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bottle', 'cup', 'laptop', 'chair'],
#     ['clock', 'book', 'chair', 'laptop'],
#     ['laptop', 'book', 'cup', 'keyboard'],
#     ['handbag', 'tv', 'book', 'chair'],
#     ['chair', 'laptop', 'remote', 'backpack'],
#     ['book', 'chair', 'clock'],
#     ['potted plant', 'keyboard', 'tv', 'chair'],
#     ['couch', 'book', 'chair', 'dining table']
# ]

# ========== bookstore ========== #
# scene_tag = "bookstore" # change
# frame_num = [88, 89, 91, 112, 119] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['clock', 'book'],
#     ['book', 'bottle'],
#     ['suitcase', 'backpack', 'person'],
#     ['laptop', 'mouse', 'tv', 'book'],
#     ['dining table', 'chair', 'book']
# ]

# ========== classroom ========== #
# scene_tag = "classroom" # change
# frame_num = [297, 301, 323, 325, 326] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['laptop', 'backpack', 'dining table', 'book'],
#     ['chair', 'dining table', 'tv', 'keyboard'],
#     ['chair', 'dining table', 'book', 'teddy bear'],
#     ['chair', 'couch'],
#     ['chair', 'bottle', 'sink', 'dining table']
# ]

# ========== coffee shop ========== #
# scene_tag = "coffee_shop" # change
# frame_num = [120, 122, 123, 223, 225, 228, 238, 244] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['potted plant', 'dining table', 'chair', 'bench'],
#     ['vase', 'bottle', 'toaster', 'potted plant'],
#     ['person', 'toaster'],
#     ['chair', 'couch', 'dining table'],
#     ['person', 'cup', 'bottle', 'chair'],
#     ['bowl', 'chair', 'dining table'],
#     ['chair', 'bowl', 'person', 'dining table'],
#     ['couch', 'laptop', 'person', 'dining table']
# ]

# ========== computer lab ========== #
# scene_tag = "computer_lab" # change
# frame_num = [272, 279, 333, 335, 337, 338] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['chair', 'keyboard', 'tv', 'mouse'],
#     ['tv', 'keyboard', 'chair'],
#     ['keyboard', 'mouse', 'tv'],
#     ['keyboard', 'chair', 'tv'],
#     ['tv', 'keyboard', 'chair'],
#     ['book', 'keyboard', 'mouse']
# ]

# ========== dorm ========== #
# scene_tag = "dorm" # change
# frame_num = [128, 130, 131, 143, 267, 569] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['spoon', 'bottle', 'cup', 'oven'],
#     ['bottle', 'sink', 'oven', 'refrigerator'],
#     ['microwave', 'cup', 'knife', 'oven'],
#     ['bottle', 'bowl', 'sink', 'spoon'],
#     ['person', 'refrigerator', 'bottle', 'oven'],
#     ['banana', 'refrigerator', 'chair', 'sink']
# ]
