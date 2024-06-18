import json
from variable_existence import scene_ids, item_lists, generate_question, answer_key, ENUS_TO_ZHHK

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
        qa_object['query'] = generate_question(item)
        qa_object['answer'] = {
            "en-US": answer_key[i][j],
            "zh-HK": ENUS_TO_ZHHK[answer_key[i][j]]
        } 
        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open('VQA/existence/bathroom_existence.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
