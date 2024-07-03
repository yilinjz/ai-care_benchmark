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

# ========== bathroom ==========
scene_tag = "bathroom"

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
