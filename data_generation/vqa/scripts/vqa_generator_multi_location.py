import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(SCRIPT_DIR)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
sys.path.append(parent)

import json

from variable_multi_location import category_tag, question_pool, scene_tag, scene_ids, item_lists, answer_keys
from utils.const import language_list
from utils.helper import translate_word, generate_questions_with_item_pair


output = []
# loop through each image
for i, scene_id in enumerate(scene_ids):
    scene_object = {}
    scene_object['scene_id'] = scene_id
    qa_pairs = []

    # get the item pairs
    item_list = item_lists[i]
    index_pool = list(range(0, len(question_pool)))
    # make a question for each item pair
    for j, item_pair in enumerate(item_list):
        qa_object = {}

        qa_object['qid'] = str(j)
        qa_object['question'] = {}
        index_pool, question = generate_questions_with_item_pair(index_pool, question_pool, item_pair, language_list)
        for language in language_list:
            qa_object['question'][language.value] = question[language]
        qa_object['answer'] = {}
        for language in language_list:
            qa_object['answer'][language.value] = answer_keys[i][j]

        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open(f'data_generation/vqa/{category_tag}/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
