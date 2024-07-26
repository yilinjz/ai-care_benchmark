from utils.const import LANGUAGE

WORD_DICTIONARY = {
    # ===== PROMPT WORD ===== #
    "Question": {
        LANGUAGE.EN_US: "Question",
        LANGUAGE.ZH_CN: "问题",
        LANGUAGE.ZH_HK: "問題",
    },
    "Context": {
        LANGUAGE.EN_US: "Context",
        LANGUAGE.ZH_CN: "上下文",
        LANGUAGE.ZH_HK: "上下文",
    },
    # ===== ANSWER WORD ===== #
    "Yes": {
        LANGUAGE.EN_US: "Yes",
        LANGUAGE.ZH_CN: "是/有",
        LANGUAGE.ZH_HK: "係/有",
    },
    "No": {
        LANGUAGE.EN_US: "No",
        LANGUAGE.ZH_CN: "不是/没有",
        LANGUAGE.ZH_HK: "唔係/冇",
    },
    "and": {
        LANGUAGE.EN_US: "and",
        LANGUAGE.ZH_CN: "且",
        LANGUAGE.ZH_HK: "且",
    },
    # ===== OREINTATION ===== #
    "up": {
        LANGUAGE.EN_US: "up",
        LANGUAGE.ZH_CN: "上",
        LANGUAGE.ZH_HK: "上",
    },
    "down": {
        LANGUAGE.EN_US: "down",
        LANGUAGE.ZH_CN: "下",
        LANGUAGE.ZH_HK: "下",
    },
    "left": {
        LANGUAGE.EN_US: "left",
        LANGUAGE.ZH_CN: "左",
        LANGUAGE.ZH_HK: "左",
    },
    "right": {
        LANGUAGE.EN_US: "right",
        LANGUAGE.ZH_CN: "右",
        LANGUAGE.ZH_HK: "右",
    },
    "up and left": {
        LANGUAGE.EN_US: "up and left",
        LANGUAGE.ZH_CN: "左上",
        LANGUAGE.ZH_HK: "左上",
    },
    "up and right": {
        LANGUAGE.EN_US: "up and right",
        LANGUAGE.ZH_CN: "右上",
        LANGUAGE.ZH_HK: "右上",
    },
    "down and left": {
        LANGUAGE.EN_US: "down and left",
        LANGUAGE.ZH_CN: "左下",
        LANGUAGE.ZH_HK: "左下",
    },
    "down and right": {
        LANGUAGE.EN_US: "down and right",
        LANGUAGE.ZH_CN: "右下",
        LANGUAGE.ZH_HK: "右下",
    },
    "center": {
        LANGUAGE.EN_US: "center",
        LANGUAGE.ZH_CN: "中间",
        LANGUAGE.ZH_HK: "中間",
    },
    # ORENTATION (PRE-PROCESSING) #
    "slightly-up": {
        LANGUAGE.EN_US: "slightly-up",
        LANGUAGE.ZH_CN: "稍微偏上",
        LANGUAGE.ZH_HK: "稍微偏上",
    },
    "slightly-down": {
        LANGUAGE.EN_US: "slightly-down",
        LANGUAGE.ZH_CN: "稍微偏下",
        LANGUAGE.ZH_HK: "稍微偏下",
    },
    "slightly-left": {
        LANGUAGE.EN_US: "slightly-left",
        LANGUAGE.ZH_CN: "稍微偏左",
        LANGUAGE.ZH_HK: "稍微偏左",
    },
    "slightly-right": {
        LANGUAGE.EN_US: "slightly-right",
        LANGUAGE.ZH_CN: "稍微偏右",
        LANGUAGE.ZH_HK: "稍微偏右",
    },
    # ===== YoloV8 Class IDs ===== #
    "person": {
        LANGUAGE.EN_US: "person",
        LANGUAGE.ZH_CN: "人",
        LANGUAGE.ZH_HK: "人",
    },
    "bicycle": {
        LANGUAGE.EN_US: "bicycle",
        LANGUAGE.ZH_CN: "自行车",
        LANGUAGE.ZH_HK: "單車",
    },
    "motorcycle": {
        LANGUAGE.EN_US: "motorcycle",
        LANGUAGE.ZH_CN: "摩托车",
        LANGUAGE.ZH_HK: "電單車",
    },
    "traffic light": {
        LANGUAGE.EN_US: "traffic light",
        LANGUAGE.ZH_CN: "红绿灯",
        LANGUAGE.ZH_HK: "信號燈",
    },
    "fire hydrant": {
        LANGUAGE.EN_US: "fire hydrant",
        LANGUAGE.ZH_CN: "消防栓",
        LANGUAGE.ZH_HK: "消防栓",
    },
    "stop sign": {
        LANGUAGE.EN_US: "stop sign",
        LANGUAGE.ZH_CN: "停止标志",
        LANGUAGE.ZH_HK: "停止標誌",
    },
    "parking meter": {
        LANGUAGE.EN_US: "parking meter",
        LANGUAGE.ZH_CN: "停车计时器",
        LANGUAGE.ZH_HK: "泊車計時器",
    },
    "bench": {
        LANGUAGE.EN_US: "bench",
        LANGUAGE.ZH_CN: "长椅",
        LANGUAGE.ZH_HK: "長椅",
    },
    "cat": {
        LANGUAGE.EN_US: "cat",
        LANGUAGE.ZH_CN: "猫",
        LANGUAGE.ZH_HK: "貓",
    },
    "dog": {
        LANGUAGE.EN_US: "dog",
        LANGUAGE.ZH_CN: "狗",
        LANGUAGE.ZH_HK: "狗",
    },
    "backpack": {
        LANGUAGE.EN_US: "backpack",
        LANGUAGE.ZH_CN: "背包",
        LANGUAGE.ZH_HK: "背囊",
    },
    "umbrella": {
        LANGUAGE.EN_US: "umbrella",
        LANGUAGE.ZH_CN: "雨伞",
        LANGUAGE.ZH_HK: "雨傘",
    },
    "handbag": {
        LANGUAGE.EN_US: "handbag",
        LANGUAGE.ZH_CN: "手袋",
        LANGUAGE.ZH_HK: "手袋",
    },
    "tie": {
        LANGUAGE.EN_US: "tie",
        LANGUAGE.ZH_CN: "领带",
        LANGUAGE.ZH_HK: "領呔",
    },
    "suitcase": {
        LANGUAGE.EN_US: "suitcase",
        LANGUAGE.ZH_CN: "行李箱",
        LANGUAGE.ZH_HK: "行李箱",
    },
    "frisbee": {
        LANGUAGE.EN_US: "frisbee",
        LANGUAGE.ZH_CN: "飞盘",
        LANGUAGE.ZH_HK: "飛盤",
    },
    "skis": {
        LANGUAGE.EN_US: "skis",
        LANGUAGE.ZH_CN: "双板滑雪板",
        LANGUAGE.ZH_HK: "雙板滑雪板",
    },
    "snowboard": {
        LANGUAGE.EN_US: "snowboard",
        LANGUAGE.ZH_CN: "单板滑雪板",
        LANGUAGE.ZH_HK: "單板滑雪板",
    },
    "sports ball": {
        LANGUAGE.EN_US: "sports ball",
        LANGUAGE.ZH_CN: "运动用球",
        LANGUAGE.ZH_HK: "運動波",
    },
    "kite": {
        LANGUAGE.EN_US: "kite",
        LANGUAGE.ZH_CN: "风筝",
        LANGUAGE.ZH_HK: "風箏",
    },
    "baseball bat": {
        LANGUAGE.EN_US: "baseball bat",
        LANGUAGE.ZH_CN: "棒球棒",
        LANGUAGE.ZH_HK: "棒球棒",
    },
    "baseball glove": {
        LANGUAGE.EN_US: "baseball glove",
        LANGUAGE.ZH_CN: "棒球手套",
        LANGUAGE.ZH_HK: "棒球手套",
    },
    "skateboard": {
        LANGUAGE.EN_US: "skateboard",
        LANGUAGE.ZH_CN: "滑板",
        LANGUAGE.ZH_HK: "滑板",
    },
    "surfboard": {
        LANGUAGE.EN_US: "surfboard",
        LANGUAGE.ZH_CN: "冲浪板",
        LANGUAGE.ZH_HK: "衝浪板",
    },
    "tennis racket": {
        LANGUAGE.EN_US: "tennis racket",
        LANGUAGE.ZH_CN: "网球拍",
        LANGUAGE.ZH_HK: "網球拍",
    },
    "bottle": {
        LANGUAGE.EN_US: "bottle",
        LANGUAGE.ZH_CN: "瓶子",
        LANGUAGE.ZH_HK: "瓶子",
    },
    "wine glass": {
        LANGUAGE.EN_US: "wine glass",
        LANGUAGE.ZH_CN: "酒杯",
        LANGUAGE.ZH_HK: "酒杯",
    },
    "cup": {
        LANGUAGE.EN_US: "cup",
        LANGUAGE.ZH_CN: "杯子",
        LANGUAGE.ZH_HK: "杯",
    },
    "fork": {
        LANGUAGE.EN_US: "fork",
        LANGUAGE.ZH_CN: "叉子",
        LANGUAGE.ZH_HK: "叉",
    },
    "knife": {
        LANGUAGE.EN_US: "knife",
        LANGUAGE.ZH_CN: "刀",
        LANGUAGE.ZH_HK: "刀",
    },
    "spoon": {
        LANGUAGE.EN_US: "spoon",
        LANGUAGE.ZH_CN: "勺子",
        LANGUAGE.ZH_HK: "勺",
    },
    "bowl": {
        LANGUAGE.EN_US: "bowl",
        LANGUAGE.ZH_CN: "碗",
        LANGUAGE.ZH_HK: "碗",
    },
    "banana": {
        LANGUAGE.EN_US: "banana",
        LANGUAGE.ZH_CN: "香蕉",
        LANGUAGE.ZH_HK: "香蕉",
    },
    "apple": {
        LANGUAGE.EN_US: "apple",
        LANGUAGE.ZH_CN: "苹果",
        LANGUAGE.ZH_HK: "蘋果",
    },
    "sandwich": {
        LANGUAGE.EN_US: "sandwich",
        LANGUAGE.ZH_CN: "三明治",
        LANGUAGE.ZH_HK: "三文治",
    },
    "orange": {
        LANGUAGE.EN_US: "orange",
        LANGUAGE.ZH_CN: "橘子",
        LANGUAGE.ZH_HK: "橘子",
    },
    "broccoli": {
        LANGUAGE.EN_US: "broccoli",
        LANGUAGE.ZH_CN: "西兰花",
        LANGUAGE.ZH_HK: "西蘭花",
    },
    "carrot": {
        LANGUAGE.EN_US: "carrot",
        LANGUAGE.ZH_CN: "胡萝卜",
        LANGUAGE.ZH_HK: "胡蘿蔔",
    },
    "hot dog": {
        LANGUAGE.EN_US: "hot dog",
        LANGUAGE.ZH_CN: "热狗",
        LANGUAGE.ZH_HK: "熱狗",
    },
    "pizza": {
        LANGUAGE.EN_US: "pizza",
        LANGUAGE.ZH_CN: "披萨",
        LANGUAGE.ZH_HK: "比薩餅",
    },
    "donut": {
        LANGUAGE.EN_US: "donut",
        LANGUAGE.ZH_CN: "甜甜圈",
        LANGUAGE.ZH_HK: "甜甜圈",
    },
    "cake": {
        LANGUAGE.EN_US: "cake",
        LANGUAGE.ZH_CN: "蛋糕",
        LANGUAGE.ZH_HK: "蛋糕",
    },
    "chair": {
        LANGUAGE.EN_US: "chair",
        LANGUAGE.ZH_CN: "椅子",
        LANGUAGE.ZH_HK: "椅子",
    },
    "couch": {
        LANGUAGE.EN_US: "couch",
        LANGUAGE.ZH_CN: "沙发",
        LANGUAGE.ZH_HK: "梳化",
    },
    "potted plant": {
        LANGUAGE.EN_US: "potted plant",
        LANGUAGE.ZH_CN: "盆栽",
        LANGUAGE.ZH_HK: "盆栽",
    },
    "bed": {
        LANGUAGE.EN_US: "bed",
        LANGUAGE.ZH_CN: "床",
        LANGUAGE.ZH_HK: "床",
    },
    "dining table": {
        LANGUAGE.EN_US: "dining table",
        LANGUAGE.ZH_CN: "餐桌",
        LANGUAGE.ZH_HK: "餐桌",
    },
    "toilet": {
        LANGUAGE.EN_US: "toilet",
        LANGUAGE.ZH_CN: "马桶",
        LANGUAGE.ZH_HK: "馬桶",
    },
    "tv": {
        LANGUAGE.EN_US: "tv",
        LANGUAGE.ZH_CN: "电视",
        LANGUAGE.ZH_HK: "電視",
    },
    "laptop": {
        LANGUAGE.EN_US: "laptop",
        LANGUAGE.ZH_CN: "笔记本电脑",
        LANGUAGE.ZH_HK: "筆記本電腦",
    },
    "mouse": {
        LANGUAGE.EN_US: "mouse",
        LANGUAGE.ZH_CN: "鼠标",
        LANGUAGE.ZH_HK: "鼠標",
    },
    "remote": {
        LANGUAGE.EN_US: "remote",
        LANGUAGE.ZH_CN: "遥控器",
        LANGUAGE.ZH_HK: "遙控器",
    },
    "keyboard": {
        LANGUAGE.EN_US: "keyboard",
        LANGUAGE.ZH_CN: "键盘",
        LANGUAGE.ZH_HK: "鍵盤",
    },
    "cell phone": {
        LANGUAGE.EN_US: "cell phone",
        LANGUAGE.ZH_CN: "手机",
        LANGUAGE.ZH_HK: "手機",
    },
    "microwave": {
        LANGUAGE.EN_US: "microwave",
        LANGUAGE.ZH_CN: "微波炉",
        LANGUAGE.ZH_HK: "微波爐",
    },
    "oven": {
        LANGUAGE.EN_US: "oven",
        LANGUAGE.ZH_CN: "烤箱",
        LANGUAGE.ZH_HK: "焗爐",
    },
    "toaster": {
        LANGUAGE.EN_US: "toaster",
        LANGUAGE.ZH_CN: "烤面包机",
        LANGUAGE.ZH_HK: "多士爐",
    },
    "sink": {
        LANGUAGE.EN_US: "sink",
        LANGUAGE.ZH_CN: "水槽",
        LANGUAGE.ZH_HK: "水槽",
    },
    "refrigerator": {
        LANGUAGE.EN_US: "refrigerator",
        LANGUAGE.ZH_CN: "电冰箱",
        LANGUAGE.ZH_HK: "電冰箱",
    },
    "book": {
        LANGUAGE.EN_US: "book",
        LANGUAGE.ZH_CN: "书",
        LANGUAGE.ZH_HK: "書",
    },
    "clock": {
        LANGUAGE.EN_US: "clock",
        LANGUAGE.ZH_CN: "时钟",
        LANGUAGE.ZH_HK: "時鐘",
    },
    "vase": {
        LANGUAGE.EN_US: "vase",
        LANGUAGE.ZH_CN: "花瓶",
        LANGUAGE.ZH_HK: "花瓶",
    },
    "scissors": {
        LANGUAGE.EN_US: "scissors",
        LANGUAGE.ZH_CN: "剪刀",
        LANGUAGE.ZH_HK: "剪刀",
    },
    "teddy bear": {
        LANGUAGE.EN_US: "teddy bear",
        LANGUAGE.ZH_CN: "泰迪熊",
        LANGUAGE.ZH_HK: "啤啤熊",
    },
    "hair dryer": {
        LANGUAGE.EN_US: "hair dryer",
        LANGUAGE.ZH_CN: "吹风机",
        LANGUAGE.ZH_HK: "風筒",
    },
    "toothbrush": {
        LANGUAGE.EN_US: "toothbrush",
        LANGUAGE.ZH_CN: "牙刷",
        LANGUAGE.ZH_HK: "牙刷",
    },
    # ===== Addtional Class IDs =====
    "toothpaste": {
        LANGUAGE.EN_US: "toothpaste",
        LANGUAGE.ZH_CN: "牙膏",
        LANGUAGE.ZH_HK: "牙膏",
    },
    "air conditioner": {
        LANGUAGE.EN_US: "air conditioner",
        LANGUAGE.ZH_CN: "空调",
        LANGUAGE.ZH_HK: "空調",
    },
    "screwdriver": {
        LANGUAGE.EN_US: "screwdriver",
        LANGUAGE.ZH_CN: "螺丝刀",
        LANGUAGE.ZH_HK: "螺絲批",
    },
    "soap": {
        LANGUAGE.EN_US: "soap",
        LANGUAGE.ZH_CN: "肥皂",
        LANGUAGE.ZH_HK: "肥皂",
    },
    "mop": {
        LANGUAGE.EN_US: "mop",
        LANGUAGE.ZH_CN: "拖布",
        LANGUAGE.ZH_HK: "地拖",
    },
    "toilet paper": {
        LANGUAGE.EN_US: "toilet paper",
        LANGUAGE.ZH_CN: "厕纸",
        LANGUAGE.ZH_HK: "廁紙",
    },
    "trash can": {
        LANGUAGE.EN_US: "trash can",
        LANGUAGE.ZH_CN: "垃圾桶",
        LANGUAGE.ZH_HK: "垃圾桶",
    },
    "shower head": {
        LANGUAGE.EN_US: "shower head",
        LANGUAGE.ZH_CN: "淋雨花洒",
        LANGUAGE.ZH_HK: "淋浴花灑",
    },
    "bucket": {
        LANGUAGE.EN_US: "bucket",
        LANGUAGE.ZH_CN: "桶",
        LANGUAGE.ZH_HK: "桶",
    },
    "towel": {
        LANGUAGE.EN_US: "towel",
        LANGUAGE.ZH_CN: "毛巾",
        LANGUAGE.ZH_HK: "毛巾",
    },
    "shoe": {
        LANGUAGE.EN_US: "shoe",
        LANGUAGE.ZH_CN: "鞋",
        LANGUAGE.ZH_HK: "鞋",
    },
    "lamp": {
        LANGUAGE.EN_US: "lamp",
        LANGUAGE.ZH_CN: "台灯",
        LANGUAGE.ZH_HK: "台灯",
    },
    "window": {
        LANGUAGE.EN_US: "window",
        LANGUAGE.ZH_CN: "窗户",
        LANGUAGE.ZH_HK: "窗戶",
    },
    "carpet": {
        LANGUAGE.EN_US: "carpet",
        LANGUAGE.ZH_CN: "地毯",
        LANGUAGE.ZH_HK: "地毯",
    },
    "map": {
        LANGUAGE.EN_US: "map",
        LANGUAGE.ZH_CN: "地图",
        LANGUAGE.ZH_HK: "地圖",
    },
    "plate": {
        LANGUAGE.EN_US: "plate",
        LANGUAGE.ZH_CN: "盘子",
        LANGUAGE.ZH_HK: "碟",
    }
}
