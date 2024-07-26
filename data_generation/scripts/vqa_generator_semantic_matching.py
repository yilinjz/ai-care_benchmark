import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(SCRIPT_DIR)
parent = os.path.dirname(parent)
sys.path.append(parent)

import json

from variable_semantic_matching import category_tag, question_pool, scene_tags, frame_nums_by_scene, item_lists_by_scene
from utils.const import language_list
from utils.helper import translate_word, generate_questions, generate_semantic_matching_answers


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
            qa_object['qid'] = str(j)

            ### QUESTION ###
            qa_object['question'] = {}
            question = generate_questions(category_tag, question_pool, item, language_list)
            for language in language_list:
                qa_object['question'][language.value] = question[language]

            ### ANSWER ###
            context = json.load(open(f'benchmark/context/{scene_id}.json', encoding="utf8"))
            candidate_pool = generate_semantic_matching_answers(context, item)
            qa_object['answer'] = {}
            for language in language_list:
                answers = [translate_word(candidate, language) for candidate in candidate_pool]
                qa_object['answer'][language.value] = json.dumps(answers, ensure_ascii=False)
            
            qa_pairs.append(qa_object)

        scene_object['qa_pairs'] = qa_pairs
        output.append(scene_object)


    with open(f'data_generation/vqa/{category_tag.value}/{scene_tag}_{category_tag.value}.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    with open(f'benchmark/vqa/{category_tag.value}/{scene_tag}_{category_tag.value}.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    