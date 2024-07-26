from utils.const import SUBTASK, LANGUAGE

### ========== CONSTANT ========== ###

category_tag = SUBTASK.OBJECT_DETECTION

question_pool = [
    {
        LANGUAGE.EN_US: f"Is there a [dt] in the scene?",
        LANGUAGE.ZH_CN: f"场景中有[dt]吗？",
        LANGUAGE.ZH_HK: f"場景中有冇[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Is a [dt] present in the scene?",
        LANGUAGE.ZH_CN: f"场景中是否存在[dt]？",
        LANGUAGE.ZH_HK: f"場景中是否存在[dt]呀？",
    },
    {
        LANGUAGE.EN_US: f"Can you see a [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你能在场景中看到[dt]吗？",
        LANGUAGE.ZH_HK: f"你見唔見到現場有[dt]呀？",
    },
    {
        LANGUAGE.EN_US: f"Is a [dt] visible in the scene?",
        LANGUAGE.ZH_CN: f"场景中是否可见[dt]？",
        LANGUAGE.ZH_HK: f"場景中是否可見[dt]？",
    },
    {
        LANGUAGE.EN_US: f"Is there any [dt] in the scene?",
        LANGUAGE.ZH_CN: f"场景中有[dt]吗？",
        LANGUAGE.ZH_HK: f"場景中有[dt]嗎？",
    },
    {
        LANGUAGE.EN_US: f"Do you sense a [dt] in the scene?",
        LANGUAGE.ZH_CN: f"你感觉到场景中有[dt]吗？",
        LANGUAGE.ZH_HK: f"你感覺到場景中有[dt]嗎？",
    },
    {
        LANGUAGE.EN_US: f"Can you tell me if a [dt] is present in the view?",
        LANGUAGE.ZH_CN: f"能不能告诉我画面中是否有[dt]？",
        LANGUAGE.ZH_HK: f"你可唔可以話我畫面中有冇[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Is there a [dt] in the view that you can tell me about?",
        LANGUAGE.ZH_CN: f"可以告诉我视图中有[dt]吗？",
        LANGUAGE.ZH_HK: f"可唔可以話我视圖中有冇[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Can you see if a [dt] is in the view?",
        LANGUAGE.ZH_CN: f"你能看到视图中是否有[dt]吗？",
        LANGUAGE.ZH_HK: f"你能看到视圖中是否有[dt]啊？",
    },
    {
        LANGUAGE.EN_US: f"Do you notice a [dt] in the view?",
        LANGUAGE.ZH_CN: f"你是否注意到视图中的[dt]？",
        LANGUAGE.ZH_HK: f"你是否注意到視圖中嘅[dt]？",
    },
    {
        LANGUAGE.EN_US: f"Is a [dt] visible in the view?",
        LANGUAGE.ZH_CN: f"[dt]在视图中是否可见？",
        LANGUAGE.ZH_HK: f"[dt]在視圖中是否可見？",
    },
    {
        LANGUAGE.EN_US: f"Can you confirm if a [dt] is present in the view?",
        LANGUAGE.ZH_CN: f"你能否确认视图中是否存在[dt]？",
        LANGUAGE.ZH_HK: f"你能否確認视圖中是否存在[dt]？",
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
    },
    {
        LANGUAGE.EN_US: f"Does the scene captured show that I am near a [dt]?",
        LANGUAGE.ZH_CN: f"拍摄到的场景是否表明我在[dt]附近？",
        LANGUAGE.ZH_HK: f"拍攝到嘅場景是否表明我喺[dt]附近？",
    },
    {
        LANGUAGE.EN_US: f"Based on the scene captured, am I close to a [dt]?",
        LANGUAGE.ZH_CN: f"根据拍摄的场景，我是否接近[dt]？",
        LANGUAGE.ZH_HK: f"根據拍攝的場景，我是否接近[dt]？",
    },
    {
        LANGUAGE.EN_US: f"Can you tell from the scene if I am near a [dt]?",
        LANGUAGE.ZH_CN: f"你能从场景看出我是否在[dt]附近吗？",
        LANGUAGE.ZH_HK: f"你能從場景看出我是否在[dt]附近嗎？",
    },
    {
        LANGUAGE.EN_US: f"Is it evident from the scene that I am near a [dt]?",
        LANGUAGE.ZH_CN: f"从场景中可以明显看出我在[dt]附近吗？",
        LANGUAGE.ZH_HK: f"從場景中可以明顯看出我喺[dt]附近呀？",
    }
]

### ========== VARIABLE ========== ###

scene_tags = [
    "bathroom",
    "bedroom",
    "dining_room",
    "doorway",
    "kitchen",
    "living_room",
    "playroom",
    "lobby",
    "meeting_room",
    "pantry",
    "workstation",
    "bookstore",
    "classroom",
    "coffee_shop",
    "computer_lab",
    "dorm"
]

frame_nums_by_scene = {
    "bathroom": [44, 49, 170, 500, 505, 509, 656],
    "bedroom": [70, 176, 178, 181, 281, 401, 525, 946],
    "dining_room": [54, 746, 757, 783, 824, 852, 879, 880, 1436],
    "doorway": [53, 251, 262, 263, 459, 460, 485, 562, 564],
    "kitchen": [138, 139, 199, 203, 204, 253, 560, 849],
    "living_room": [50, 156, 166, 200, 201, 261, 350, 356, 583, 1304],
    "playroom": [425, 426, 428, 437, 1081, 1084, 1157, 1203],
    "lobby": [9, 36, 619, 625, 1251, 1253],
    "meeting_room": [5, 27, 39, 341],
    "pantry": [1, 410, 412, 415, 417],
    "workstation": [4, 23, 371, 388, 393, 453, 455, 474],
    "bookstore": [88, 89, 91, 112, 119],
    "classroom": [297, 301, 323, 325, 326],
    "coffee_shop": [120, 122, 123, 223, 225, 228, 238, 244],
    "computer_lab": [272, 279, 333, 335, 337, 338],
    "dorm": [128, 130, 131, 143, 267, 569],
}

item_lists_by_scene = {
    "bathroom": [
        ['toothbrush', 'toilet', 'toothpaste', 'cell phone'],
        ['bottle', 'sink', 'bucket', 'towel'],
        ['toilet', 'sink', 'toothbrush', 'toothpaste'],
        ['bottle', 'toothbrush', 'hair dryer', 'air conditioner'],
        ['toilet', 'bottle', 'screwdriver', 'soap'],
        ['cup', 'toothbrush', 'mop', 'toilet paper'],
        ['cup', 'sink', 'trash can', 'shower head']
    ],
    "bedroom": [
        ['bed', 'vase', 'potted plant', 'shoe'],
        ['backpack', 'book', 'person', 'lamp'],
        ['couch', 'cup', 'chair', 'sports ball'],
        ['keyboard', 'remote', 'clock', 'window'],
        ['bed', 'teddy bear', 'chair', 'carpet'],
        ['bed', 'teddy bear', 'book', 'person'],
        ['laptop', 'dining table', 'map', 'backpack'],
        ['bed', 'chair', 'tv', 'mouse']
    ],
    "dining_room": [
        ['laptop', 'chair', 'microwave', 'mouse'], 
        ['toaster', 'bottle', 'knife', 'cup'],
        ['dining table', 'chair', 'tv', 'window'],
        ['backpack', 'lamp', 'refrigerator', 'window'],
        ['bowl', 'refrigerator', 'potted plant', 'apple'],
        ['banana', 'orange', 'toaster', 'sink'],
        ['chair', 'vase', 'laptop', 'couch'],
        ['microwave', 'oven', 'carpet', 'keyboard'],
        ['dining table', 'lamp', 'trash can', 'cell phone']
    ],
    "doorway": [
        ['bowl', 'wine glass', 'book', 'shoe'], 
        ['refrigerator', 'person', 'mop', 'trash can'],
        ['vase', 'tv', 'book', 'lamp'],
        ['chair', 'microwave', 'tv', 'person'],
        ['potted plant', 'chair', 'carpet', 'cell phone'],
        ['potted plant', 'chair', 'kite', 'sports ball'],
        ['tv', 'couch', 'keyboard', 'skis'],
        ['person', 'microwave', 'frisbee', 'snowboard'],
        ['person', 'dog', 'cat', 'backpack']
    ],
    "kitchen": [
        ['sink', 'bowl', 'fork', 'oven'], 
        ['microwave', 'knife', 'spoon', 'cup'],
        ['cup', 'toaster', 'oven', 'apple'],
        ['sink', 'microwave', 'trash can', 'air conditioner'],
        ['scissors', 'clock', 'wine glass', 'toothbrush'],
        ['refrigerator', 'bottle', 'cup', 'wine glass'],
        ['microwave', 'sink', 'bottle', 'vase'],
        ['toaster', 'bowl', 'knife', 'potted plant']
    ],
    "living_room": [
        ['couch', 'laptop', 'keyboard', 'bed'], 
        ['tv', 'chair', 'remote', 'person'],
        ['dining table', 'vase', 'trash can', 'plate'],
        ['tv', 'bottle', 'backpack', 'cup'],
        ['sports ball', 'tv', 'lamp', 'book'],
        ['laptop', 'clock', 'mouse', 'donut'],
        ['snowboard', 'cell phone', 'bicycle', 'keyboard'],
        ['couch', 'book', 'oven', 'bicycle'],
        ['backpack', 'couch', 'remote', 'laptop'],
        ['tv', 'vase', 'person', 'chair']
    ],
    "playroom": [
        ['sports ball', 'backpack', 'frisbee', 'kite'],
        ['dining table', 'tv', 'sports ball', 'bicycle'],
        ['suitcase', 'backpack', 'couch', 'laptop'],
        ['teddy bear', 'tv', 'chair', 'cat'],
        ['bed', 'book', 'vase', 'motorcycle'],
        ['mouse', 'book', 'remote', 'dining table'],
        ['sports ball', 'tie', 'teddy bear', 'bed'],
        ['suitcase', 'fire hydrant', 'traffic light', 'bench']
    ],
    "lobby": [
        ['refrigerator', 'tv', 'cup', 'suitcase'],
        ['tie', 'clock', 'dining table', 'window'],
        ['potted plant', 'cell phone', 'sandwich', 'vase'],
        ['chair', 'backpack', 'bottle', 'mouse'],
        ['couch', 'book', 'dining table', 'cell phone'],
        ['potted plant', 'chair', 'tv', 'person']
    ],
    "meeting_room": [
        ['dining table', 'chair', 'tv', 'laptop'],
        ['chair', 'clock', 'bottle', 'window'],
        ['chair', 'cell phone', 'sandwich', 'suitcase'],
        ['potted plant', 'chair', 'dining table', 'backpack']
    ],
    "pantry": [
        ['refrigerator', 'lamp', 'microwave', 'towel'],
        ['sink', 'bottle', 'cup', 'cake'],
        ['dining table', 'toaster', 'clock', 'apple'],
        ['cup', 'bicycle', 'laptop', 'backpack'],
        ['cell phone', 'keyboard', 'remote', 'refrigerator']
    ],
    "workstation": [
        ['bottle', 'cup', 'laptop', 'remote'],
        ['clock', 'book', 'cell phone', 'air conditioner'],
        ['carpet', 'person', 'cup', 'keyboard'],
        ['handbag', 'tv', 'suitcase', 'backpack'],
        ['chair', 'wine glass', 'remote', 'banana'],
        ['book', 'tie', 'clock', 'bowl'],
        ['potted plant', 'keyboard', 'tv', 'baseball bat'],
        ['couch', 'baseball glove', 'window', 'dining table']
    ],
    "bookstore": [
        ['clock', 'fire hydrant', 'book', 'tennis racket'],
        ['book', 'bottle', 'wine glass', 'cup'],
        ['suitcase', 'backpack', 'person', 'screwdriver'],
        ['laptop', 'mouse', 'tv', 'cell phone'],
        ['dining table', 'window', 'shoe', 'person']
    ],
    "classroom": [
        ['laptop', 'backpack', 'suitcase', 'book'],
        ['chair', 'dining table', 'tie', 'mop'],
        ['chair', 'sports ball', 'book', 'teddy bear'],
        ['towel', 'carpet', 'dining table', 'couch'],
        ['chair', 'bottle', 'sink', 'dining table']
    ],
    "coffee_shop": [
        ['potted plant', 'snowboard', 'umbrella', 'bench'],
        ['vase', 'bed', 'toaster', 'cell phone'],
        ['person', 'toaster', 'scissors', 'hot dog'],
        ['chair', 'couch', 'sandwich', 'handbag'],
        ['person', 'cup', 'bottle', 'knife'],
        ['bowl', 'vase', 'potted plant', 'dining table'],
        ['chair', 'bowl', 'person', 'bicycle'],
        ['couch', 'laptop', 'trash can', 'bed']
    ],
    "computer_lab": [
        ['chair', 'keyboard', 'tv', 'mouse'],
        ['tv', 'keyboard', 'mouse', 'remote'],
        ['keyboard', 'mouse', 'tv', 'person'],
        ['keyboard', 'chair', 'tv', 'shoe'],
        ['tv', 'keyboard', 'book', 'backpack'],
        ['book', 'keyboard', 'mouse', 'cell phone']
    ],
    "dorm": [
        ['spoon', 'bottle', 'fork', 'knife'],
        ['soap', 'sink', 'oven', 'refrigerator'],
        ['microwave', 'toaster', 'knife', 'sandwich'],
        ['bottle', 'fork', 'sink', 'spoon'],
        ['person', 'refrigerator', 'wine glass', 'oven'],
        ['banana', 'orange', 'chair', 'sink']
    ]
}

answer_keys_by_scene = {
    "bathroom": [
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No']
    ],
    "bedroom": [
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'Yes']
    ],
    "dining_room": [
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'No', 'No']
    ],
    "doorway": [
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No']
    ],
    "kitchen": [
        ['Yes', 'Yes', 'No', 'Yes'], 
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'No', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No']
    ],
    "living_room": [
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'Yes'], 
        ['No', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'No', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['No', 'Yes', 'No', 'Yes']
    ],
    "playroom": [
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'Yes', 'Yes', 'No'],
        ['No', 'No', 'Yes', 'Yes'],
        ['Yes', 'No', 'No', 'No']
    ],
    "lobby": [
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'No', 'No']
    ],
    "meeting_room": [
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No']
    ],
    "pantry": [
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'No', 'No', 'Yes']
    ],
    "workstation": [
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'No', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'No', 'Yes']
    ],
    "bookstore": [
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'Yes']
    ],
    "classroom": [
        ['Yes', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'No', 'Yes', 'Yes'],
        ['No', 'Yes', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'Yes']
    ],
    "coffee_shop": [
        ['Yes', 'No', 'No', 'Yes'],
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'No', 'No', 'Yes'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No']
    ],
    "computer_lab": [
        ['Yes', 'Yes', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'Yes', 'No'],
        ['Yes', 'Yes', 'No', 'No'],
        ['Yes', 'Yes', 'Yes', 'No']
    ],
    "dorm": [
        ['Yes', 'Yes', 'No', 'No'],
        ['No', 'Yes', 'Yes', 'Yes'],
        ['Yes', 'No', 'Yes', 'No'],
        ['Yes', 'No', 'Yes', 'Yes'],
        ['Yes', 'Yes', 'No', 'Yes'],
        ['Yes', 'No', 'Yes', 'Yes']
    ]
}
