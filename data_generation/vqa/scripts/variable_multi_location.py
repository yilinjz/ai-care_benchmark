from utils.const import LANGUAGE

### ========== CONSTANT ========== ###

category_tag = "multi-location"

question_pool = [
    {
        LANGUAGE.EN_US: f"Where is [dt] located relative to [rf]?",
        LANGUAGE.ZH_CN: f"[dt]是在[rf]的哪边?",
        LANGUAGE.ZH_HK: f"[dt]喺在[rf]的邊度?",
    },
    {
        LANGUAGE.EN_US: f"How do I reach [dt] from [rf]?",
        LANGUAGE.ZH_CN: f"我怎样可以从[rf]摸到[dt]?",
        LANGUAGE.ZH_HK: f"我點樣可以由[rf]揾到[dt]?",
    },
    {
        LANGUAGE.EN_US: f"Can you point me towards [dt] from where [rf] is?",
        LANGUAGE.ZH_CN: f"你能否指引我怎样从[rf]到[dt]?",
        LANGUAGE.ZH_HK: f"你可以指俾我睇，由[rf]點樣揾到[dt]?",
    },
    {
        LANGUAGE.EN_US: f"From [rf], which direction should I move to find [dt]?",
        LANGUAGE.ZH_CN: f"我从[rf]开始往哪个方向移动可以到[dt]?",
        LANGUAGE.ZH_HK: f"我由[rf]要行邊個方向去揾[dt]?",
    },
    {
        LANGUAGE.EN_US: f"If I'm facing [rf], in which direction is [dt]?",
        LANGUAGE.ZH_CN: f"我现在正面对[rf], [dt]在哪个方向?",
        LANGUAGE.ZH_HK: f"我對住[rf], [dt]喺邊個方向？",
    },
    {
        LANGUAGE.EN_US: f"If [rf] is in front of me, where should I look for [dt]?",
        LANGUAGE.ZH_CN: f"如果[rf]在我正前方，我应该往哪边找[dt]?",
        LANGUAGE.ZH_HK: f"[rf]喺在我面前，我應該望邊度搵[dt]?",
    }
]

### ========== VARIABLE ========== ###

# ========== bathroom ==========
scene_tag = "bathroom"


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
