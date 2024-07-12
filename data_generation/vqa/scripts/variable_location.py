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
        LANGUAGE.EN_US: f"Where is the closest [dt] in relation to me?",
        LANGUAGE.ZH_CN: f"离我最近的[dt]在哪里?",
        LANGUAGE.ZH_HK: f"離我最近嘅[dt]喺邊度？",
    },
    {
        LANGUAGE.EN_US: f"In which direction is the [dt] from my current position?",
        LANGUAGE.ZH_CN: f"[dt]在我当前位置的什么方向?",
        LANGUAGE.ZH_HK: f"[dt]由我而家嘅位置喺邊個方向？",
    },
    {
        LANGUAGE.EN_US: f"Find where the [dt] is, please.",
        LANGUAGE.ZH_CN: f"请帮我找下[dt]在哪里。",
        LANGUAGE.ZH_HK: f"請幫我搵吓[dt]喺邊。",
    },
    {
        LANGUAGE.EN_US: f"Could you guide me to the position of the [dt]?",
        LANGUAGE.ZH_CN: f"你可以引导我去到[dt]的位置嗎?",
        LANGUAGE.ZH_HK: f"你可以引導我去到[dt]嘅位置嗎？",
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
#     ['toothbrush', 'sink', 'toilet', 'toothpaste'],
#     ['toilet', 'sink', 'bottle', 'person'],
#     ['bottle', 'toothbrush', 'sink', 'toilet'],
#     ['towel', 'bottle', 'sink', 'toothbrush'],
#     ['cup', 'toothbrush', 'sink', 'bottle'],
#     ['cup', 'sink', 'towel', 'toilet']
# ]

# ========== bedroom ========== #
# scene_tag = "bedroom" # change
# frame_num = [70, 176, 178, 181, 281, 401, 525, 946] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bed', 'vase', 'potted plant', 'dog'],
#     ['backpack', 'book', 'bed', 'lamp'],
#     ['couch', 'bed', 'chair', 'backpack'],
#     ['keyboard', 'remote', 'tv', 'book'],
#     ['bed', 'teddy bear', 'chair', 'carpet'],
#     ['bed', 'teddy bear', 'chair'],
#     ['laptop', 'dining table', 'map', 'backpack'],
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
# scene_tag = "doorway" # change
# frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['microwave', 'wine glass', 'book', 'bowl'], 
#     ['refrigerator', 'sink', 'oven', 'couch'],
#     ['vase', 'tv', 'book', 'potted plant'],
#     ['chair', 'microwave', 'refrigerator', 'cup'],
#     ['potted plant', 'chair', 'tv', 'dining table'],
#     ['potted plant', 'chair', 'vase'],
#     ['tv', 'couch', 'keyboard', 'book'],
#     ['person', 'microwave', 'oven', 'refrigerator'],
#     ['person', 'dog', 'sink', 'bowl']
# ]

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
# scene_tag = "computer lab" # change
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
scene_tag = "dorm" # change
frame_num = [128, 130, 131, 143, 267, 569] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# change
item_lists = [
    ['spoon', 'bottle', 'cup', 'oven'],
    ['bottle', 'sink', 'oven', 'refrigerator'],
    ['microwave', 'cup', 'knife', 'oven'],
    ['bottle', 'bowl', 'sink', 'spoon'],
    ['person', 'refrigerator', 'bottle', 'oven'],
    ['banana', 'refrigerator', 'chair', 'sink']
]
