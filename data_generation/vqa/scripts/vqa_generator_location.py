import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(SCRIPT_DIR)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
sys.path.append(parent)

import json

from variable_location import category_tag, question_pool, scene_tags, frame_nums_by_scene, item_lists_by_scene
from utils.const import language_list
from utils.helper import generate_questions, generate_location_answers


for scene_tag in scene_tags:
    print(scene_tag)
    output = []
    frame_nums = frame_nums_by_scene[scene_tag]
    scene_ids = [f"{scene_tag}_{x}" for x in frame_nums]
    item_lists = item_lists_by_scene[scene_tag]

    # loop through each image
    for i, scene_id in enumerate(scene_ids):
        scene_object = {}
        scene_object['scene_id'] = scene_id
        qa_pairs = []

        # get the items
        item_list = item_lists[i]
        # make a question for each item
        for j, item in enumerate(item_list):
            qa_object = {}

            ### QUESTION ###
            qa_object['qid'] = str(j)
            qa_object['question'] = {}
            question = generate_questions(question_pool, item)
            for language in language_list:
                qa_object['question'][language.value] = question[language]

            ### ANSWER ###
            context = json.load(open(f'benchmark/context/{scene_id}.json', encoding="utf8"))
            answers = generate_location_answers(context, item)
            qa_object['answer'] = {}
            for language in language_list:
                qa_object['answer'][language.value] = answers[language]
            
            qa_pairs.append(qa_object)

        scene_object['qa_pairs'] = qa_pairs
        output.append(scene_object)

    with open(f'data_generation/vqa/{category_tag}/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    with open(f'benchmark/vqa/{scene_tag}_{category_tag}.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    