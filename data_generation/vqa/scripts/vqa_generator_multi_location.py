import json
from variable_multi_location import scene_tag, category_tag, scene_ids, item_lists, generate_question

output = []

### each scene
for i, scene_id in enumerate(scene_ids):
    scene_object = {}
    scene_object['scene_id'] = scene_id
    qa_pairs = []

    # each question
    item_list = item_lists[i]
    for j, item_pair in enumerate(item_list):
        qa_object = {}
        qa_object['qid'] = str(j)
        qa_object['query'] = generate_question(item_pair[0], item_pair[1])
        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open(f'VQA/{category_tag}/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
