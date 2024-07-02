import json
from variable_identification import scene_tag, category_tag, scene_ids, question_pool

output = []

### each scene
for i, scene_id in enumerate(scene_ids):
    scene_object = {}
    scene_object['scene_id'] = scene_id
    qa_pairs = []

    # each question
    for j, question in enumerate(question_pool):
        qa_object = {}
        qa_object['qid'] = str(j)
        qa_object['query'] = question
        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open(f'VQA/{category_tag}/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
