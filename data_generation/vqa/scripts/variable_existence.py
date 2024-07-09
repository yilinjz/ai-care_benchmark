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
#     ['toothbrush', 'toilet', 'toothpaste', 'phone'],
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
#     ['couch', 'cup', 'chair', 'basketball'],
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
#     ['dining table', 'lamp', 'trash can', 'phone']
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
scene_tag = "doorway" # change
frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# change
item_lists = [
    ['bowl', 'wine glass', 'book', 'shoe'], 
    ['refrigerator', 'person', 'mop', 'trash can'],
    ['vase', 'tv', 'book', 'lamp'],
    ['chair', 'microwave', 'tv', 'person'],
    ['potted plant', 'chair', 'carpet', 'phone'],
    ['potted plant', 'chair', 'kite', 'sports ball'],
    ['tv', 'couch', 'keyboard', 'skis'],
    ['person', 'microwave', 'frisbee', 'snowboard'],
    ['person', 'dog', 'cat', 'backpack']
]

# change
answer_keys = [
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'No', 'No', 'No'],
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No']
]