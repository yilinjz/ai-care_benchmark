import random
import copy
import json

from utils.const import SUBTASK
from utils.dictionary import WORD_DICTIONARY

# translate #
def translate_word(word, language):
    return WORD_DICTIONARY[word][language]

# pre-processing context data #
def process_context(context_json, language):
    context = []
    for obj in context_json:
        text = obj['TEXT']
        text = translate_word(text, language)
        if 'slightly' in obj['ORIENTATION']:
            raw_oritentation = obj['ORIENTATION'].split()
            oritentation = [translate_word(word, language) for word in raw_oritentation]
            oritentation = ' '.join(oritentation)
        else:
            oritentation = translate_word(obj['ORIENTATION'], language)
        depth = obj['DEPTH']
        # position = obj['POSITION']
        # context.append(f"({text}, {oritentation}, {depth}, {position})")
        context.append(f"({text}, {oritentation}, {depth})")
    return context

# match benchmark -> instruction prompt #
def get_instruction_prompt_type(benchmark_name):
    instruction_prompt_type = ""
    if SUBTASK.OBJECT_DETECTION.value in benchmark_name:
        instruction_prompt_type = SUBTASK.OBJECT_DETECTION.value
    elif SUBTASK.SEMANTIC_MATCHING.value in benchmark_name:
        instruction_prompt_type = SUBTASK.SEMANTIC_MATCHING.value
    elif SUBTASK.QUESTION_GENERATION.value in benchmark_name:
        instruction_prompt_type = SUBTASK.QUESTION_GENERATION.value
    else:
        raise ValueError("Unknown Instruction Prompt Type!")
    return f"{instruction_prompt_type}_instruction_prompt"

# pick question from pool #
def generate_questions(category_tag, question_pool, item, language_list):
    if category_tag == SUBTASK.OBJECT_DETECTION:
        question = copy.deepcopy(random.choice(question_pool))
        for language in language_list:
            question[language] = question[language].replace('[dt]', translate_word(item, language))
        return question
    elif category_tag == SUBTASK.SEMANTIC_MATCHING:
        return random.choice(question_pool[item])
    elif category_tag == SUBTASK.QUESTION_GENERATION:
        pass
    else:
        print(category_tag)
        raise ValueError("Unknown Subtask!")

# generate answer for semantic matching #
def generate_semantic_matching_answers(context, item):
    candidate_pool = []
    for obj in context:
        if obj['TEXT'] == item:
            candidate = obj['ORIENTATION'].replace('slightly-', '')
            if candidate not in candidate_pool:
                candidate_pool.append(candidate)
    if not candidate_pool:
        print(context)
        print(item)
        raise ValueError("Item Not Found In Context!")
    return candidate_pool

# evaluate #
def calculate_score(result_path, category_tag, tested_languages):
     data = json.load(open(result_path, encoding="utf8"))
     for language in tested_languages:
        total_count, correct_count = 0, 0
        for scene in data:
            for qa_pair in scene['qa_pairs']:
                total_count += 1
                if category_tag == SUBTASK.OBJECT_DETECTION:
                    answer = qa_pair['answer'][language.value].replace(" ", "")
                    result = qa_pair['result'][language.value].replace(" ", "")
                    if result == answer:
                        correct_count += 1
                elif category_tag == SUBTASK.QUESTION_GENERATION:
                    answers = json.loads(qa_pair['answer'][language.value])
                    for i, answer in enumerate(answers):
                        answers[i] = answer.replace(" ", "")
                    result = qa_pair['result'][language.value].replace(" ", "")
                    if result in answers:
                        correct_count += 1
                else:
                    raise ValueError("Unknown Subtask!")

        print(f"LANGUAGE: {language.value} | CORRECT: {correct_count} | TOTAL: {total_count} | SCORE: {correct_count/total_count}")  
