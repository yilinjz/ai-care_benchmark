import random

# ========== bathroom ==========
scene_tag = "bathroom"
category_tag = "existence"

frame_num = [44, 49, 170, 500, 505, 509, 656]
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

item_lists = [
    ['toothbrush', 'toilet', 'toothpaste', 'phone'],
    ['bottle', 'sink', 'bucket', 'towel'],
    ['toilet', 'sink', 'toothbrush', 'toothpaste'],
    ['bottle', 'toothbrush', 'hair dryer', 'air conditioner'],
    ['toilet', 'bottle', 'screwdriver', 'soap'],
    ['cup', 'toothbrush', 'mop', 'toilet paper'],
    ['cup', 'sink', 'trash can', 'shower head']
]

answer_key = [
    ['Yes', 'Yes', 'Yes', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'No', 'No']
]

ENUS_TO_ZHHK = {
    "Yes": "係/有",
    "No": "唔係/冇",
    "toothbrush": "牙刷",
    "toilet": "廁所",
    "toothpaste": "牙膏",
    "phone": "手機",
    "bottle": "瓶子",
    "hair dryer": "風筒",
    "air conditioner": "空調",
    "screwdriver": "螺絲批",
    "soap": "肥皂",
    "cup": "杯子",
    "mop": "地拖",
    "toilet paper": "廁紙",
    "sink": "水槽",
    "trash can": "垃圾桶",
    "shower head": "淋浴花灑",
    "bucket": "桶",
    "towel": "毛巾",
}

def generate_question(item):
    pool = [
        {
            "en-US": f"Is there a {item} in the scene?",
            "zh-HK": f"場景中有冇{ENUS_TO_ZHHK[item]}啊?"
        },
        {
            "en-US": f"Can you tell me if a {item} is present in the view?",
            "zh-HK": f"你可唔可以話我畫面中有冇{ENUS_TO_ZHHK[item]}啊？"
        },
        {
            "en-US": f"Is a {item} visible in the current scene?",
            "zh-HK": f"呢個場景入面有無見到{ENUS_TO_ZHHK[item]}啊？"
        },
        {
            "en-US": f"Could you check if there's a {item} in what you can see?",
            "zh-HK": f"你可唔可以檢查下你見到嘅嘢入面有冇{ENUS_TO_ZHHK[item]}啊?"
        },
        {
            "en-US": f"Do you detect a {item} in the surroundings?",
            "zh-HK": f"你感唔感應到周圍環境有冇{ENUS_TO_ZHHK[item]}?"
        },
        {
            "en-US": f"Am I near a {item}, according to the scene captured?",
            "zh-HK": f"根據攝到嘅畫面，我係咪喺{ENUS_TO_ZHHK[item]}附近？"
        }
    ]
    return random.choice(pool)
