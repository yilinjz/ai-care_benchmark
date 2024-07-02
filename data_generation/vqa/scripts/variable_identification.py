import random

# ========== bathroom ==========
scene_tag = "bathroom"
category_tag = "identification"

frame_num = [44, 49, 170, 500, 505, 509, 656]
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

question_pool = [
    {
        "en-US": f"What object is directly in front of me?",
        "zh-HK": f"乜嘢物體就喺我面前？"
    },
    {
        "en-US": f"Can you identify the item on my left side?",
        "zh-HK": f"你可唔可以認出我左邊嘅物品啊？"
    },
    {
        "en-US": f"What item is the closest to me?",
        "zh-HK": f"乜嘢物品離我最近？"
    }
]
