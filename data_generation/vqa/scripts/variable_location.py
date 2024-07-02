import random

# ========== bathroom ==========
scene_tag = "bathroom"
category_tag = "location"

frame_num = [44, 49, 170, 500, 505, 509, 656]
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

item_lists = [
    ['toothbrush', 'toilet', 'sink', 'cup'],
    ['toothbrush', 'sink', 'toilet', 'toothpaste'],
    ['toilet', 'sink', 'towel', 'person'],
    ['bottle', 'toothbrush', 'sink', 'toilet'],
    ['towel', 'bottle', 'sink', 'toothbrush'],
    ['cup', 'toothbrush', 'sink', 'bottle'],
    ['cup', 'sink', 'towel', 'toilet']
]

ENUS_TO_ZHHK = {
    "person": "人",
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
            "en-US": f"Can you locate the {item} in the scene?",
            "zh-HK": f"你可以喺房入面搵到{ENUS_TO_ZHHK[item]}嗎?"
        },
        {
            "en-US": f"Where is the closest {item} in relation to me?",
            "zh-HK": f"離我最近嘅{ENUS_TO_ZHHK[item]}喺邊度？"
        },
        {
            "en-US": f"In which direction is the {item} from my current position?",
            "zh-HK": f"{ENUS_TO_ZHHK[item]}由我而家嘅位置喺邊個方向？"
        },
        {
            "en-US": f"Find where the {item} is, please.",
            "zh-HK": f"請幫我搵吓{ENUS_TO_ZHHK[item]}喺邊。"
        },
        {
            "en-US": f"Could you guide me to the position of the {item}?",
            "zh-HK": f"你可以引導我去到{ENUS_TO_ZHHK[item]}嘅位置嗎？"
        },
    ]
    return random.choice(pool)
