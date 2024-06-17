import json

frame_num = [44, 49, 170, 500, 505, 509, 656]
scene_ids = [f"bathroom_{x}" for x in frame_num]
item_lists = [
    ['toothbrush', 'toilet', 'toothpaste', 'phone'],
    ['bottle', 'sink', 'bucket', 'towel'],
    ['toilet', 'sink', 'toothbrush', 'toothpaste'],
    ['bottle', 'toothbrush', 'hair dryer', 'air conditioner'],
    ['toilet', 'bottle', 'screwdriver', 'soap'],
    ['cup', 'toothbrush', 'mop', 'toilet paper'],
    ['cup', 'sink', 'trash can', 'shower head']
]
en_to_hk = {
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

output = []

### each scene
for i, scene_id in enumerate(scene_ids):
    scene_object = {}
    scene_object['scene_id'] = scene_id
    qa_pairs = []

    # each question
    item_list = item_lists[i]
    for j, item in enumerate(item_list):
        qa_object = {}
        qa_object['qid'] = str(j)
        qa_object['query'] = {
            "en-US": f"Is there a {item} in the scene?",
            "zh-HK": f"場景中有冇{en_to_hk[item]}啊?"
        }
        if 0 <= j <= 1:
            qa_object['answer'] = {
                "en-US": f"Yes",
                "zh-HK": f"有"
            } 
        elif 2 <= j <= 3:
            qa_object['answer'] = {
                "en-US": f"No",
                "zh-HK": f"冇"
            } 
        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open('existence/bathroom_existence.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
