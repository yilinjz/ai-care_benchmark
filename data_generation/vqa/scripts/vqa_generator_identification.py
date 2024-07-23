import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(SCRIPT_DIR)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
sys.path.append(parent)

import json

from variable_identification import scene_tag, category_tag, scene_ids, question_pool
from utils.const import language_list
from utils.helper import generate_open_questions


output = []
# loop through each image
for i, scene_id in enumerate(scene_ids):
    scene_object = {}
    scene_object['scene_id'] = scene_id
    qa_pairs = []

    # loop through all questions for each image
    open_question_pool = generate_open_questions(question_pool)
    for j, question in enumerate(open_question_pool):
        qa_object = {}

        qa_object['qid'] = str(j)
        qa_object['question'] = {}
        for language in language_list:
            qa_object['question'][language.value] = question[language]

        qa_pairs.append(qa_object)

    scene_object['qa_pairs'] = qa_pairs
    output.append(scene_object)

with open(f'data_generation/vqa/{category_tag}/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
