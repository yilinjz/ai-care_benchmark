import random

# ========== bathroom ==========
scene_tag = "bathroom"
category_tag = "multi-location"

frame_num = [44, 49, 170, 500, 505, 509, 656]
scene_ids = [f"{scene_tag}_{x}" for x in frame_num]

item_lists = [
    [['toilet', 'sink'], ['toothbrush', 'sink'], ['cup', 'toothbrush']],
    [['toilet', 'sink'], ['toothbrush', 'toothpaste'], ['bottle', 'toothbrush']],
    [['toilet', 'sink'], ['person', 'sink'], ['person', 'toilet']],
    [['toilet', 'sink'], ['toothbrush', 'sink'], ['person', 'sink']],
    [['toilet', 'sink'], ['bottle', 'sink'], ['bottle', 'toilet']],
    [['toothbrush', 'sink'], ['toothbrush', 'bottle'], ['sink', 'bottle']],
    [['toilet', 'sink'], ['bottle', 'toilet'], ['cup', 'sink']]
]

answer_keys = [
    ['down and left', 'top/top and left', 'right'],
    ['down and left', 'left', 'left'],
    ['down and left', 'up', 'up and right'],
    ['down and right', 'left', 'up'],
    ['left/down and left', 'up/up and left/up and right', 'up and right'],
    ['up', 'up/up and right', 'right'],
    ['down and left', 'up', 'up/up and left']
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

def generate_question(target, reference):
    pool = [
        {
            "en-US": f"Where is {target} located relative to {reference}?",
            "zh-HK": f"{ENUS_TO_ZHHK[target]}喺在{ENUS_TO_ZHHK[reference]}的邊度?"
        },
        {
            "en-US": f"How do I reach {target} from {reference}?",
            "zh-HK": f"我點樣可以由{ENUS_TO_ZHHK[reference]}去到{ENUS_TO_ZHHK[target]}？"
        },
        {
            "en-US": f"Can you point me towards {target} from where {reference} is?",
            "zh-HK": f"你可以指俾我睇，由{ENUS_TO_ZHHK[reference]}點樣揾到{ENUS_TO_ZHHK[target]}？"
        },
        {
            "en-US": f"From {reference}, which direction should I move to find {target}?",
            "zh-HK": f"我由{ENUS_TO_ZHHK[reference]}要行邊個方向去揾{ENUS_TO_ZHHK[target]}？"
        },
        {
            "en-US": f"If I'm facing {reference}, in which direction is {target}?",
            "zh-HK": f"我對住{ENUS_TO_ZHHK[reference]}，{ENUS_TO_ZHHK[target]}喺邊個方向？"
        },
        {
            "en-US": f"If {reference} is in front of me, where should I look for {target}?",
            "zh-HK": f"{ENUS_TO_ZHHK[reference]}喺在我面前，我應該望邊度搵{ENUS_TO_ZHHK[target]}？"
        },
    ]
    return random.choice(pool)
