from utils.const import SUBTASK, LANGUAGE

### ========== CONSTANT ========== ###

category_tag = SUBTASK.SEMANTIC_MATCHING

question_pool = {
    # ===== YoloV8 Class IDs ===== #
    "person": [
        {
            LANGUAGE.EN_US: "Is there someone nearby?",
            LANGUAGE.ZH_CN: "附近有人吗？",
            LANGUAGE.ZH_HK: "附近有人嗎？"
        },
        {
            LANGUAGE.EN_US: "Is someone standing near me?",
            LANGUAGE.ZH_CN: "有人站在我附近吗？",
            LANGUAGE.ZH_HK: "有人企喺我附近啊？"
        },
    ],
    "bicycle": [
        {
            LANGUAGE.EN_US: "Where can I find something to ride to get to school quickly?",
            LANGUAGE.ZH_CN: "我在哪里可以找到可以骑着快速上学的东西？",
            LANGUAGE.ZH_HK: "我喺邊度可以搵到可以騎住快速返學嘅嘢？"
        },
    ],
    "bench": [
        {
            LANGUAGE.EN_US: "Where can our basketball team sit and relax for a moment?",
            LANGUAGE.ZH_CN: "我们的篮球队可以在哪里坐下来放松片刻？",
            LANGUAGE.ZH_HK: "我哋嘅籃球隊可以喺邊度坐低放鬆片刻？"
        },
    ],
    "dog": [
        {
            LANGUAGE.EN_US: "Where is the barking coming from?",
            LANGUAGE.ZH_CN: "吠叫是从哪里来的？",
            LANGUAGE.ZH_HK: "吠叫係由邊度嚟嘅？"
        },
    ],
    "backpack": [
        {
            LANGUAGE.EN_US: "Where can I put my things and carry them while walking around?",
            LANGUAGE.ZH_CN: "我可以把我的东西放在哪里，并在走动时携带它们？",
            LANGUAGE.ZH_HK: "我可以將我嘅嘢放喺邊度，並喺走動時攜帶它們？"
        },
    ],
    "umbrella": [
        {
            LANGUAGE.EN_US: "Where can I find something to keep me dry in the rain?",
            LANGUAGE.ZH_CN: "我在哪里可以找到在雨中保持干爽的东西？",
            LANGUAGE.ZH_HK: "我喺邊度可以搵到喺雨中保持乾爽嘅嘢？"
        },
    ],
    "handbag": [
        {
            LANGUAGE.EN_US: "Where can I store my wallet and makeup while I'm out?",
            LANGUAGE.ZH_CN: "外出时，我可以把钱包和化妆品放在哪里？",
            LANGUAGE.ZH_HK: "外出時，我可以將銀包同化妝品放喺邊度？"
        },
    ],
    "tie": [
        {
            LANGUAGE.EN_US: "Where can I find something to wear around my neck for a formal look?",
            LANGUAGE.ZH_CN: "我在哪里可以找到可以戴在脖子上来打造正式的造型的东西？",
            LANGUAGE.ZH_HK: "我喺邊度可以搵到可以戴喺脖子上嚟打造正式嘅造型嘅嘢？"
        },
    ],
    "suitcase": [
        {
            LANGUAGE.EN_US: "Where can find something to pack my clothes for a trip?",
            LANGUAGE.ZH_CN: "在哪里可以找到为旅行打包衣服的东西？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到為旅行打包衫嘅嘢？"
        },
    ],
    "sports ball": [
        {
            LANGUAGE.EN_US: "Where can I find something to play a sport game with children?",
            LANGUAGE.ZH_CN: "在哪里可以找到与孩子们一起玩体育游戏的东西？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到與仔們一起玩體育遊戲嘅嘢？"
        },
    ],
    "bottle": [
        {
            LANGUAGE.EN_US: "Where can I get something to hold my drink?",
            LANGUAGE.ZH_CN: "在哪里可以买到盛饮料的东西？",
            LANGUAGE.ZH_HK: "喺邊度可以買到盛飲料嘅嘢？"
        },
    ],
    "wine glass": [
        {
            LANGUAGE.EN_US: "Where can I pour my wine?",
            LANGUAGE.ZH_CN: "我可以把酒倒在哪里？",
            LANGUAGE.ZH_HK: "我可以將酒倒喺邊度？"
        },
    ],
    "cup": [
        {
            LANGUAGE.EN_US: "Where can I pour my coffee or tea? ",
            LANGUAGE.ZH_CN: "我可以把咖啡或茶倒在哪里？",
            LANGUAGE.ZH_HK: "我可以將咖啡或茶倒喺邊度？"
        },
    ],
    "fork": [
        {
            LANGUAGE.EN_US: "Where can I find something to eat my salad with?",
            LANGUAGE.ZH_CN: "我在哪里可以找到吃沙拉的东西？",
            LANGUAGE.ZH_HK: "我喺邊度可以搵到食沙拉嘅嘢？"
        },
    ],
    "knife": [
        {
            LANGUAGE.EN_US: "Where can I find something to cut my food with?",
            LANGUAGE.ZH_CN: "哪里可以找到切食物的工具？",
            LANGUAGE.ZH_HK: "邊度可以搵到切食物嘅工具？"
        },
    ],
    "spoon": [
        {
            LANGUAGE.EN_US: "Where can I find something to eat my soup with?",
            LANGUAGE.ZH_CN: "在哪里可以找到喝汤的东西？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到飲湯嘅嘢？"
        }, 
    ],
    "bowl": [
        {
            LANGUAGE.EN_US: "Where can I put my cereal or soup? ",
            LANGUAGE.ZH_CN: "我可以把麦片或汤放在哪里？",
            LANGUAGE.ZH_HK: "我可以將麥片或湯放喺邊度？"
        },
    ],
    "banana": [
        {
            LANGUAGE.EN_US: "Where can I find a quick, healthy snack?",
            LANGUAGE.ZH_CN: "在哪里可以找到快速、健康的零食？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到快速、健康嘅零食？"
        },
    ],
    "chair": [
        {
            LANGUAGE.EN_US: "I'm tired. Where can I sit down?",
            LANGUAGE.ZH_CN: "我累了。我可以在哪里坐下？",
            LANGUAGE.ZH_HK: "我攰喇. 我可以喺邊度坐低？"
        },
        {
            LANGUAGE.EN_US: "Where can I sit down comfortably?",
            LANGUAGE.ZH_CN: "我可以在哪里舒服地坐下来？",
            LANGUAGE.ZH_HK: "我可以喺邊度舒服咁坐落嚟？"
        }
    ],
    "couch": [
        {
            LANGUAGE.EN_US: "Where can I lounge and watch TV?",
            LANGUAGE.ZH_CN: "我可以在哪里休息和看电视？",
            LANGUAGE.ZH_HK: "我可以喺邊度休息同睇电视？"
        },
    ],
    "potted plant": [
        {
            LANGUAGE.EN_US: "I need to water my flowers. Where are they?",
            LANGUAGE.ZH_CN: "我需要给我的花浇水。他们在哪？",
            LANGUAGE.ZH_HK: "我需要畀我嘅花澆水。 佢哋喺邊?"
        },
        {
            LANGUAGE.EN_US: "Where can I find some greenery indoors?",
            LANGUAGE.ZH_CN: "在室内哪里可以找到绿色植物？",
            LANGUAGE.ZH_HK: "喺室內邊度可以搵到綠色植物？"
        },
    ],
    "bed": [
        {
            LANGUAGE.EN_US: "Where can I sleep?",
            LANGUAGE.ZH_CN: "我可以在哪里睡觉？",
            LANGUAGE.ZH_HK: "我可以喺邊度瞓覺？"
        },
        {
            LANGUAGE.EN_US: "Where can I lie down for a while?",
            LANGUAGE.ZH_CN: "我可以在哪里躺一会儿？",
            LANGUAGE.ZH_HK: "我可以喺邊度躺一陣？"
        },
    ],
    "dining table": [
        {
            LANGUAGE.EN_US: "Where can I sit and eat my meals?",
            LANGUAGE.ZH_CN: "我可以坐在哪里用餐？",
            LANGUAGE.ZH_HK: "我可以坐喺邊度用餐？"
        },
    ],
    "toilet": [
        {
            LANGUAGE.EN_US: "Where can I go to relieve myself?",
            LANGUAGE.ZH_CN: "我可以去哪里解手？",
            LANGUAGE.ZH_HK: "我可以去邊度解手？"
        },
    ],
    "tv": [
        {
            LANGUAGE.EN_US: "Where can I watch my favorite shows?",
            LANGUAGE.ZH_CN: "在哪里可以观看我喜爱的节目？",
            LANGUAGE.ZH_HK: "喺邊度可以觀看我喜愛嘅節目？"
        },
    ],
    "laptop": [
        {
            LANGUAGE.EN_US: "I need to check my email. Where is my device?",
            LANGUAGE.ZH_CN: "我需要查看电子邮件。我的设备在哪里？",
            LANGUAGE.ZH_HK: "我需要查看電子郵件。 我嘅設備喺邊度？"
        },
        {
            LANGUAGE.EN_US: "Where can I work on my computer while on the go?",
            LANGUAGE.ZH_CN: "在旅途中，我可以在哪里使用电脑？",
            LANGUAGE.ZH_HK: "在旅途中，我可以喺邊度使用電腦？"
        },
    ],
    "mouse": [
        {
            LANGUAGE.EN_US: "Where can I find a device to navigate my computer screen?",
            LANGUAGE.ZH_CN: "在哪里可以找到操作电脑屏幕的设备？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到操作電腦屏幕嘅設備？"
        },
    ],
    "remote": [
        {
            LANGUAGE.EN_US: "Where can I find the device to change the channel?",
            LANGUAGE.ZH_CN: "在哪里可以找到转换频道的设备？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到轉換頻道嘅設備？"
        },
    ],
    "keyboard": [
        {
            LANGUAGE.EN_US: "I need to type something. Where is my tool?",
            LANGUAGE.ZH_CN: "我需要输入一些东西。我的工具在哪里？",
            LANGUAGE.ZH_HK: "我需要輸入一些嘢。 我嘅工具喺邊度？"
        },
        {
            LANGUAGE.EN_US: "Where can I type my documents?",
            LANGUAGE.ZH_CN: "我可以在哪里输入文件？",
            LANGUAGE.ZH_HK: "我可以喺邊度輸入文件？"
        },
    ],
    "cell phone": [
        {
            LANGUAGE.EN_US: "Where can I make a call or send a text?",
            LANGUAGE.ZH_CN: "在哪里可以打电话或发短信？",
            LANGUAGE.ZH_HK: "喺邊度可以打電話或發短信？"
        },
    ],
    "microwave": [
        {
            LANGUAGE.EN_US: "Where can I quickly heat up my food? ",
            LANGUAGE.ZH_CN: "哪里可以快速加热食物？",
            LANGUAGE.ZH_HK: "邊度可以快速加熱食物？"
        },
    ],
    "oven": [
        {
            LANGUAGE.EN_US: "Where can I bake a cake or roast a chicken? ",
            LANGUAGE.ZH_CN: "哪里可以烤蛋糕或烤鸡？",
            LANGUAGE.ZH_HK: "邊度可以烤蛋糕或烤雞？"
        },
    ],
    "toaster": [
        {
            LANGUAGE.EN_US: "Where can I cook toasted bread?",
            LANGUAGE.ZH_CN: "我在哪里可以做烤面包？",
            LANGUAGE.ZH_HK: "我喺邊度可以做多士？"
        },
        {
            LANGUAGE.EN_US: "Where can I make my bread crispy?",
            LANGUAGE.ZH_CN: "怎样才能让面包变脆？",
            LANGUAGE.ZH_HK: "怎樣才能令麵包變脆？"
        },
    ],
    "sink": [
        {
            LANGUAGE.EN_US: "Where can I wash my hands or dishes? ",
            LANGUAGE.ZH_CN: "我可以在哪里洗手或洗碗？",
            LANGUAGE.ZH_HK: "我可以喺邊度洗手或洗碗？"
        },
    ],
    "refrigerator": [
        {
            LANGUAGE.EN_US: "Where can I get iced coke?",
            LANGUAGE.ZH_CN: "我在哪里可以拿到冰镇可乐？",
            LANGUAGE.ZH_HK: "我喺邊度可以拿到雪藏可樂？"
        },
        {
            LANGUAGE.EN_US: "Where can I store my perishable food items?",
            LANGUAGE.ZH_CN: "易腐食品可以存放在哪里？",
            LANGUAGE.ZH_HK: "易腐食品可以存放喺邊度？"
        },
    ],
    "book": [
        {
            LANGUAGE.EN_US: "Where can I find something to read?",
            LANGUAGE.ZH_CN: "我在哪里可以找到一些读物？",
            LANGUAGE.ZH_HK: "我喺邊度可以搵到啲讀物？"
        },
    ],
    "clock": [
        {
            LANGUAGE.EN_US: "Where can I check the time right now?",
            LANGUAGE.ZH_CN: "我现在在哪里可以查看时间？",
            LANGUAGE.ZH_HK: "我而家喺邊度可以查看時間？"
        },
    ],
    "vase": [
        {
            LANGUAGE.EN_US: "I bought some rose. Where can I put it?",
            LANGUAGE.ZH_CN: "我买了一些玫瑰。我可以把它放在哪里？",
            LANGUAGE.ZH_HK: "我買咗啲玫瑰。 我可以將佢放喺邊度？"
        },
        {
            LANGUAGE.EN_US: "Where can I put these flowers?",
            LANGUAGE.ZH_CN: "我可以把这些花放在哪里？",
            LANGUAGE.ZH_HK: "我可以將呢啲花放喺邊度？"
        },
    ],
    "teddy bear": [
        {
            LANGUAGE.EN_US: "Where can I find a cuddly toy? ",
            LANGUAGE.ZH_CN: "在哪里可以找到可爱的玩具？",
            LANGUAGE.ZH_HK: "喺邊度可以搵到得意嘅玩具？"
        },
    ],
    "toothbrush": [
        {
            LANGUAGE.EN_US: "Where can I clean my teeth?",
            LANGUAGE.ZH_CN: "我在哪里可以清洁牙齿？",
            LANGUAGE.ZH_HK: "我喺邊度可以清潔牙齒？"
        },
    ]
}

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
        ['toothbrush', 'toilet', 'sink', 'cup'],
        ['toothbrush', 'sink', 'toilet', 'bottle'],
        ['toilet', 'sink', 'bottle', 'person'],
        ['bottle', 'toothbrush', 'sink', 'toilet'],
        ['toilet', 'bottle', 'sink', 'toothbrush'],
        ['cup', 'toothbrush', 'sink', 'bottle'],
        ['cup', 'sink', 'bottle', 'toilet']
    ],
    "bedroom": [
        ['bed', 'vase', 'potted plant', 'dog'],
        ['backpack', 'book', 'bed', 'handbag'],
        ['couch', 'bed', 'chair', 'backpack'],
        ['keyboard', 'remote', 'tv', 'book'],
        ['bed', 'teddy bear', 'chair', 'cup'],
        ['bed', 'teddy bear', 'chair'],
        ['laptop', 'dining table', 'bed', 'backpack'],
        ['bed', 'chair', 'tv', 'mouse']
    ],
    "dining_room": [
        ['laptop', 'chair', 'book', 'bottle'], 
        ['toaster', 'bottle', 'chair', 'microwave'],
        ['dining table', 'chair', 'tv', 'sink'],
        ['bottle', 'cup', 'bowl', 'backpack'],
        ['bowl', 'refrigerator', 'potted plant', 'chair'],
        ['banana', 'dining table', 'bowl', 'sink'],
        ['chair', 'vase', 'tv', 'dining table'],
        ['microwave', 'oven', 'dining table', 'chair'],
        ['dining table', 'chair', 'vase', 'potted plant']
    ],
    "doorway": [
        ['microwave', 'wine glass', 'book', 'bowl'], 
        ['refrigerator', 'sink', 'oven', 'couch'],
        ['vase', 'tv', 'book', 'potted plant'],
        ['chair', 'microwave', 'refrigerator', 'cup'],
        ['potted plant', 'chair', 'tv', 'dining table'],
        ['potted plant', 'chair', 'vase'],
        ['tv', 'couch', 'keyboard', 'book'],
        ['person', 'microwave', 'oven', 'refrigerator'],
        ['person', 'dog', 'sink', 'bowl']
    ],
    "kitchen": [
        ['sink', 'bowl', 'microwave', 'oven'], 
        ['microwave', 'knife', 'bowl', 'bottle'],
        ['cup', 'bowl', 'oven', 'knife'],
        ['sink', 'microwave', 'oven', 'cup'],
        ['refrigerator', 'bowl', 'wine glass', 'toothbrush'],
        ['refrigerator', 'bottle', 'microwave', 'sink'],
        ['microwave', 'sink', 'bottle'],
        ['toaster', 'bowl', 'sink', 'bowl']
    ],
    "living_room": [
        ['couch', 'potted plant', 'book', 'tv'], 
        ['tv', 'chair', 'remote', 'couch'],
        ['dining table', 'vase', 'chair', 'handbag'],
        ['tv', 'bottle', 'chair', 'cup'],
        ['couch', 'tv', 'dining table', 'book'],
        ['laptop', 'clock', 'bowl', 'potted plant'],
        ['potted plant', 'chair', 'bicycle', 'keyboard'],
        ['couch', 'book', 'potted plant', 'tv'],
        ['backpack', 'couch', 'remote', 'tv'],
        ['couch', 'vase', 'book', 'chair']
    ],
    "playroom": [
        ['sports ball', 'backpack', 'chair'],
        ['couch', 'tv', 'sports ball', 'chair'],
        ['suitcase', 'dining table', 'couch', 'chair'],
        ['teddy bear', 'tv', 'chair'],
        ['bed', 'book', 'chair'],
        ['chair', 'book', 'remote', 'tv'],
        ['chair', 'backpack', 'teddy bear', 'bed'],
        ['suitcase', 'backpack', 'couch']
    ],
    "lobby": [
        ['refrigerator', 'tv', 'bottle', 'chair'],
        ['couch', 'clock', 'dining table', 'chair'],
        ['potted plant', 'couch', 'vase'],
        ['chair', 'backpack', 'bottle', 'microwave'],
        ['couch', 'book', 'tv'],
        ['potted plant', 'book', 'couch']
    ],
    "meeting_room": [
        ['dining table', 'chair'],
        ['chair', 'dining table', 'bottle'],
        ['chair', 'dining table'],
        ['potted plant', 'chair', 'dining table']
    ],
    "pantry": [
        ['refrigerator', 'chair', 'microwave', 'sink'],
        ['sink', 'bottle', 'cup', 'microwave'],
        ['dining table', 'toaster', 'clock', 'sink'],
        ['cup', 'chair', 'refrigerator', 'dining table'],
        ['cell phone', 'handbag', 'chair', 'sink']
    ],
    "workstation": [
        ['bottle', 'cup', 'laptop', 'chair'],
        ['clock', 'book', 'chair', 'laptop'],
        ['laptop', 'book', 'cup', 'keyboard'],
        ['handbag', 'tv', 'book', 'chair'],
        ['chair', 'laptop', 'remote', 'backpack'],
        ['book', 'chair', 'clock'],
        ['potted plant', 'keyboard', 'tv', 'chair'],
        ['couch', 'book', 'chair', 'dining table']
    ],
    "bookstore": [
        ['clock', 'book'],
        ['book', 'bottle'],
        ['suitcase', 'backpack', 'person'],
        ['laptop', 'mouse', 'tv', 'book'],
        ['dining table', 'chair', 'book']
    ],
    "classroom": [
        ['laptop', 'backpack', 'dining table', 'book'],
        ['chair', 'dining table', 'tv', 'keyboard'],
        ['chair', 'dining table', 'book', 'teddy bear'],
        ['chair', 'couch'],
        ['chair', 'bottle', 'sink', 'dining table']
    ],
    "coffee_shop": [
        ['potted plant', 'dining table', 'chair', 'bench'],
        ['vase', 'bottle', 'toaster', 'potted plant'],
        ['person', 'toaster'],
        ['chair', 'couch', 'dining table'],
        ['person', 'cup', 'bottle', 'chair'],
        ['bowl', 'chair', 'dining table'],
        ['chair', 'bowl', 'person', 'dining table'],
        ['couch', 'laptop', 'person', 'dining table']
    ],
    "computer_lab": [
        ['chair', 'keyboard', 'tv', 'mouse'],
        ['tv', 'keyboard', 'chair'],
        ['keyboard', 'mouse', 'tv'],
        ['keyboard', 'chair', 'tv'],
        ['tv', 'keyboard', 'chair'],
        ['book', 'keyboard', 'mouse']
    ],
    "dorm": [
        ['spoon', 'bottle', 'cup', 'oven'],
        ['bottle', 'sink', 'oven', 'refrigerator'],
        ['microwave', 'cup', 'knife', 'oven'],
        ['bottle', 'bowl', 'sink', 'spoon'],
        ['person', 'refrigerator', 'bottle', 'oven'],
        ['banana', 'refrigerator', 'chair', 'sink']
    ]
}
