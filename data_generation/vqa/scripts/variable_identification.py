from utils.const import LANGUAGE

### ========== CONSTANT ========== ###

category_tag = "identification"

question_pool = [
    {
        LANGUAGE.EN_US: f"What object is directly in front of me?",
        LANGUAGE.ZH_CN: f"我的正前方是什么物体？",
        LANGUAGE.ZH_HK: f"乜嘢物體就喺我面前？",
    },
    {
        LANGUAGE.EN_US: f"Can you identify the item on my left side?",
        LANGUAGE.ZH_CN: f"你能否识别我左边是什么物体？",
        LANGUAGE.ZH_HK: f"你可唔可以認出我左邊嘅物品啊？",
    },
    {
        LANGUAGE.EN_US: f"Can you identify the item on my right side?",
        LANGUAGE.ZH_CN: f"你能否识别我右边是什么物体？",
        LANGUAGE.ZH_HK: f"你可唔可以認出我右邊嘅物品啊？",
    },
    {
        LANGUAGE.EN_US: f"What item is the closest to me?",
        LANGUAGE.ZH_CN: f"离我最近的物体是什么？",
        LANGUAGE.ZH_HK: f"乜嘢物品離我最近？",
    },
    {
        LANGUAGE.EN_US: f"What is the object closest to the center of the frame?",
        LANGUAGE.ZH_CN: f"离画面中心最近的物体是什么？",
        LANGUAGE.ZH_HK: f"離畫面中心最近嘅物體係乜嘢？",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ========== #
# scene_tag = "bathroom" # change
# frame_num = [44, 49, 170, 500, 505, 509, 656] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== bedroom ========== #
# scene_tag = "bedroom" # change
# frame_num = [70, 176, 178, 181, 281, 401, 525, 946] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== dining room ========== #
# scene_tag = "dining_room" # change
# frame_num = [54, 746, 757, 783, 824, 852, 879, 880, 1436] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== doorway ========== #
# scene_tag = "doorway" # change
# frame_num = [53, 251, 262, 263, 459, 460, 485, 562, 564] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== kitchen ========== #
# scene_tag = "kitchen" # change
# frame_num = [138, 139, 199, 203, 204, 253, 560, 849] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== living room ========== #
# scene_tag = "living_room" # change
# frame_num = [50, 156, 166, 200, 201, 261, 350, 356, 583, 1304] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== playroom ========== #
# scene_tag = "playroom" # change
# frame_num = [425, 426, 428, 437, 1081, 1084, 1157, 1203] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== lobby ========== #
# scene_tag = "lobby" # change
# frame_num = [9, 36, 619, 625, 1251, 1253] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== meeting room ========== #
# scene_tag = "meeting_room" # change
# frame_num = [5, 27, 39, 341] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== pantry ========== #
# scene_tag = "pantry" # change
# frame_num = [1, 410, 412, 415, 417] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== workstation ========== #
# scene_tag = "workstation" # change
# frame_num = [4, 23, 371, 388, 393, 453, 455, 474] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== bookstore ========== #
scene_tag = "bookstore" # change
frame_num = [88, 89, 91, 112, 119] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== classroom ========== #
# scene_tag = "classroom" # change
# frame_num = [297, 301, 323, 325, 326] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== coffee shop ========== #
# scene_tag = "coffee_shop" # change
# frame_num = [120, 122, 123, 223, 225, 228, 238, 244] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== computer lab ========== #
# scene_tag = "computer lab" # change
# frame_num = [272, 279, 333, 335, 337, 338] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

# ========== dorm ========== #
# scene_tag = "dorm" # change
# frame_num = [128, 130, 131, 143, 267, 569] # change
# scene_ids = [f"{scene_tag}_{x}" for x in frame_num]
