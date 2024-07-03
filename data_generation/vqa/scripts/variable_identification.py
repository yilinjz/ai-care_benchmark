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
        LANGUAGE.EN_US: f"What item is the closest to me?",
        LANGUAGE.ZH_CN: f"离我最近的物体是什么？",
        LANGUAGE.ZH_HK: f"乜嘢物品離我最近？",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ========== #
scene_tag = "bathroom" # change
frame_num = [44, 49, 170, 500, 505, 509, 656] # change
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]
