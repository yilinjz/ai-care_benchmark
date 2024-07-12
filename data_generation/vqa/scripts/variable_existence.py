from utils.const import LANGUAGE

### ========== CONSTANT ========== ###

category_tag = "existence"

question_pool = [
    {
        LANGUAGE.EN_US: f"Is there a [dt] in the scene?",
        LANGUAGE.ZH_CN: f"场景中有[dt]吗？",
        LANGUAGE.ZH_HK: f"場景中有冇[dt]啊?",
    },
    {
        LANGUAGE.EN_US: f"Can you tell me if a [dt] is present in the view?",
        LANGUAGE.ZH_CN: f"能不能告诉我画面中是否有[dt]？",
        LANGUAGE.ZH_HK: f"你可唔可以話我畫面中有冇[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Is a [dt] visible in the current scene?",
        LANGUAGE.ZH_CN: f"当前场景中能不能看到[dt]啊？",
        LANGUAGE.ZH_HK: f"呢個場景入面有無見到[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Could you check if there's a [dt] in what you can see?",
        LANGUAGE.ZH_CN: f"检查一下你看到的内容中是否有[dt]？",
        LANGUAGE.ZH_HK: f"可唔可以檢查下你見到嘅嘢入面有冇[dt]啊?",
    },
    {
        LANGUAGE.EN_US: f"Do you detect a [dt] in the surroundings?",
        LANGUAGE.ZH_CN: f"你能否感应到在周围环境中有无[dt]？",
        LANGUAGE.ZH_HK: f"你感唔感應到周圍環境有冇[dt]?",
    },
    {
        LANGUAGE.EN_US: f"Am I near a [dt], according to the scene captured?",
        LANGUAGE.ZH_CN: f"根据拍摄到的场景，我是在[dt]附近吗？",
        LANGUAGE.ZH_HK: f"根據攝到嘅畫面，我係咪喺[dt]附近？",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ========== #
# scene_tag = "bathroom" # change
# frame_num = [44, 49, 170, 500, 505, 509, 656] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['toothbrush', 'toilet', 'toothpaste', 'cell phone'],
#     ['bottle', 'sink', 'bucket', 'towel'],
#     ['toilet', 'sink', 'toothbrush', 'toothpaste'],
#     ['bottle', 'toothbrush', 'hair dryer', 'air conditioner'],
#     ['toilet', 'bottle', 'screwdriver', 'soap'],
#     ['cup', 'toothbrush', 'mop', 'toilet paper'],
#     ['cup', 'sink', 'trash can', 'shower head']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No']
# ]

# ========== bedroom ========== #
# scene_tag = "bedroom" # change
# frame_num = [70, 176, 178, 181, 281, 401, 525, 946] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bed', 'vase', 'potted plant', 'shoe'],
#     ['backpack', 'book', 'person', 'lamp'],
#     ['couch', 'cup', 'chair', 'sports ball'],
#     ['keyboard', 'remote', 'clock', 'window'],
#     ['bed', 'teddy bear', 'chair', 'carpet'],
#     ['bed', 'teddy bear', 'book', 'person'],
#     ['laptop', 'dining table', 'map', 'backpack'],
#     ['bed', 'chair', 'tv', 'mouse']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'Yes']
# ]

# ========== dining room ========== #
# scene_tag = "dining_room" # change
# frame_num = [54, 746, 757, 783, 824, 852, 879, 880, 1436] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['laptop', 'chair', 'microwave', 'mouse'], 
#     ['toaster', 'bottle', 'knife', 'cup'],
#     ['dining table', 'chair', 'tv', 'window'],
#     ['backpack', 'lamp', 'refrigerator', 'window'],
#     ['bowl', 'refrigerator', 'potted plant', 'apple'],
#     ['banana', 'orange', 'toaster', 'sink'],
#     ['chair', 'vase', 'laptop', 'couch'],
#     ['microwave', 'oven', 'carpet', 'keyboard'],
#     ['dining table', 'lamp', 'trash can', 'cell phone']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'No', 'No']
# ]

# ========== doorway ========== #
# scene_tag = "doorway" # change
# frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bowl', 'wine glass', 'book', 'shoe'], 
#     ['refrigerator', 'person', 'mop', 'trash can'],
#     ['vase', 'tv', 'book', 'lamp'],
#     ['chair', 'microwave', 'tv', 'person'],
#     ['potted plant', 'chair', 'carpet', 'cell phone'],
#     ['potted plant', 'chair', 'kite', 'sports ball'],
#     ['tv', 'couch', 'keyboard', 'skis'],
#     ['person', 'microwave', 'frisbee', 'snowboard'],
#     ['person', 'dog', 'cat', 'backpack']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No']
# ]

# ========== kitchen ========== #
# scene_tag = "kitchen" # change
# frame_num = [138, 139, 199, 203, 204, 253, 560, 849] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['sink', 'bowl', 'fork', 'oven'], 
#     ['microwave', 'knife', 'spoon', 'cup'],
#     ['cup', 'toaster', 'oven', 'apple'],
#     ['sink', 'microwave', 'trash can', 'air conditioner'],
#     ['scissors', 'clock', 'wine glass', 'toothbrush'],
#     ['refrigerator', 'bottle', 'cup', 'wine glass'],
#     ['microwave', 'sink', 'bottle', 'vase'],
#     ['toaster', 'bowl', 'knife', 'potted plant']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'Yes'], 
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'No', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No']
# ]

# ========== living room ========== #
# scene_tag = "living_room" # change
# frame_num = [50, 156, 166, 200, 201, 261, 350, 356, 583, 1304] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['couch', 'laptop', 'keyboard', 'bed'], 
#     ['tv', 'chair', 'remote', 'person'],
#     ['dining table', 'vase', 'trash can', 'plate'],
#     ['tv', 'bottle', 'backpack', 'cup'],
#     ['sports ball', 'tv', 'lamp', 'book'],
#     ['laptop', 'clock', 'mouse', 'donut'],
#     ['snowboard', 'cell phone', 'bicycle', 'keyboard'],
#     ['couch', 'book', 'oven', 'bicycle'],
#     ['backpack', 'couch', 'remote', 'laptop'],
#     ['tv', 'vase', 'person', 'chair']
# ]

# # change
# answer_keys = [
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'Yes'], 
#     ['No', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'No', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['No', 'Yes', 'No', 'Yes']
# ]

# ========== playroom ========== #
# scene_tag = "playroom" # change
# frame_num = [425, 426, 428, 437, 1081, 1084, 1157, 1203] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['sports ball', 'backpack', 'frisbee', 'kite'],
#     ['dining table', 'tv', 'sports ball', 'bicycle'],
#     ['suitcase', 'backpack', 'couch', 'laptop'],
#     ['teddy bear', 'tv', 'chair', 'cat'],
#     ['bed', 'book', 'vase', 'motorcycle'],
#     ['mouse', 'book', 'remote', 'dining table'],
#     ['sports ball', 'tie', 'teddy bear', 'bed'],
#     ['suitcase', 'fire hydrant', 'traffic light', 'bench']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'Yes', 'Yes', 'No'],
#     ['No', 'No', 'Yes', 'Yes'],
#     ['Yes', 'No', 'No', 'No']
# ]

# ========== lobby ========== #
# scene_tag = "lobby" # change
# frame_num = [9, 36, 619, 625, 1251, 1253] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['refrigerator', 'tv', 'cup', 'suitcase'],
#     ['tie', 'clock', 'dining table', 'window'],
#     ['potted plant', 'cell phone', 'sandwich', 'vase'],
#     ['chair', 'backpack', 'bottle', 'mouse'],
#     ['couch', 'book', 'dining table', 'cell phone'],
#     ['potted plant', 'chair', 'tv', 'person']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'No', 'No']
# ]

# ========== meeting room ========== #
# scene_tag = "meeting_room" # change
# frame_num = [5, 27, 39, 341] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['dining table', 'chair', 'tv', 'laptop'],
#     ['chair', 'clock', 'bottle', 'window'],
#     ['chair', 'cell phone', 'sandwich', 'suitcase'],
#     ['potted plant', 'chair', 'dining table', 'backpack']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No']
# ]

# ========== pantry ========== #
# scene_tag = "pantry" # change
# frame_num = [1, 410, 412, 415, 417] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['refrigerator', 'lamp', 'microwave', 'towel'],
#     ['sink', 'bottle', 'cup', 'cake'],
#     ['dining table', 'toaster', 'clock', 'apple'],
#     ['cup', 'bicycle', 'laptop', 'backpack'],
#     ['cell phone', 'keyboard', 'remote', 'refrigerator']
# ]

# # change
# answer_keys = [
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'No', 'No', 'Yes']
# ]

# ========== workstation ========== #
# scene_tag = "workstation" # change
# frame_num = [4, 23, 371, 388, 393, 453, 455, 474] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['bottle', 'cup', 'laptop', 'remote'],
#     ['clock', 'book', 'cell phone', 'air conditioner'],
#     ['carpet', 'person', 'cup', 'keyboard'],
#     ['handbag', 'tv', 'suitcase', 'backpack'],
#     ['chair', 'wine glass', 'remote', 'banana'],
#     ['book', 'tie', 'clock', 'bowl'],
#     ['potted plant', 'keyboard', 'tv', 'baseball bat'],
#     ['couch', 'baseball glove', 'window', 'dining table']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'No', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'No', 'Yes']
# ]

# ========== bookstore ========== #
scene_tag = "bookstore" # change
frame_num = [88, 89, 91, 112, 119] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# change
item_lists = [
    ['clock', 'fire hydrant', 'book', 'tennis racket'],
    ['book', 'bottle', 'wine glass', 'cup'],
    ['suitcase', 'backpack', 'person', 'screwdriver'],
    ['laptop', 'mouse', 'tv', 'cell phone'],
    ['dining table', 'window', 'shoe', 'person']
]

# change
answer_keys = [
    ['Yes', 'No', 'Yes', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'No', 'No', 'Yes']
]

# ========== classroom ========== #
# scene_tag = "classroom" # change
# frame_num = [297, 301, 323, 325, 326] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['laptop', 'backpack', 'suitcase', 'book'],
#     ['chair', 'dining table', 'tie', 'mop'],
#     ['chair', 'sports ball', 'book', 'teddy bear'],
#     ['towel', 'carpet', 'dining table', 'couch'],
#     ['chair', 'bottle', 'sink', 'dining table']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'No', 'Yes', 'Yes'],
#     ['No', 'Yes', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'Yes']
# ]

# ========== coffee shop ========== #
# scene_tag = "coffee_shop" # change
# frame_num = [120, 122, 123, 223, 225, 228, 238, 244] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['potted plant', 'snowboard', 'umbrella', 'bench'],
#     ['vase', 'bed', 'toaster', 'cell phone'],
#     ['person', 'toaster', 'scissors', 'hot dog'],
#     ['chair', 'couch', 'sandwich', 'handbag'],
#     ['person', 'cup', 'bottle', 'knife'],
#     ['bowl', 'vase', 'potted plant', 'dining table'],
#     ['chair', 'bowl', 'person', 'bicycle'],
#     ['couch', 'laptop', 'trash can', 'bed']
# ]

# # change
# answer_keys = [
#     ['Yes', 'No', 'No', 'Yes'],
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'No', 'No', 'Yes'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No']
# ]

# ========== computer lab ========== #
# scene_tag = "computer lab" # change
# frame_num = [272, 279, 333, 335, 337, 338] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['chair', 'keyboard', 'tv', 'mouse'],
#     ['tv', 'keyboard', 'mouse', 'remote'],
#     ['keyboard', 'mouse', 'tv', 'person'],
#     ['keyboard', 'chair', 'tv', 'shoe'],
#     ['tv', 'keyboard', 'book', 'backpack'],
#     ['book', 'keyboard', 'mouse', 'cell phone']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No'],
#     ['Yes', 'Yes', 'No', 'No'],
#     ['Yes', 'Yes', 'Yes', 'No']
# ]

# ========== dorm ========== #
# scene_tag = "dorm" # change
# frame_num = [128, 130, 131, 143, 267, 569] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# # change
# item_lists = [
#     ['spoon', 'bottle', 'fork', 'knife'],
#     ['soap', 'sink', 'oven', 'refrigerator'],
#     ['microwave', 'toaster', 'knife', 'sandwich'],
#     ['bottle', 'fork', 'sink', 'spoon'],
#     ['person', 'refrigerator', 'wine glass', 'oven'],
#     ['banana', 'orange', 'chair', 'sink']
# ]

# # change
# answer_keys = [
#     ['Yes', 'Yes', 'No', 'No'],
#     ['No', 'Yes', 'Yes', 'Yes'],
#     ['Yes', 'No', 'Yes', 'No'],
#     ['Yes', 'No', 'Yes', 'Yes'],
#     ['Yes', 'Yes', 'No', 'Yes'],
#     ['Yes', 'No', 'Yes', 'Yes']
# ]
