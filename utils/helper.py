import random

from utils.dictionary import WORD_DICTIONARY

def process_context(context_json):
    context = []
    for object in context_json:
        text = object['TEXT']
        oritentation = object['ORIENTATION']
        depth = object['DEPTH']
        position = object['POSITION']
        context.append(f"({text}, {oritentation}, {depth}, {position})")
    return context

def get_instruction_type(benchmark_name):
    instruction_type = ""
    if "existence" in benchmark_name:
        instruction_type = "existence"
    elif "identification" in benchmark_name:
        instruction_type = "identification"
    elif "multi-location" in benchmark_name:
        instruction_type = "multi-location"
    elif "location" in benchmark_name:
        instruction_type = "location"
    elif "hand_guidance" in benchmark_name:
        instruction_type = "hand_guidance"
    else:
        raise ValueError("Unknown Instruction Type")
    return f"{instruction_type}_instruction"

def translate_word(word, language):
    return WORD_DICTIONARY[word][language]

def generate_questions(index_pool, question_pool, item, language_list):
    if not index_pool:
        index_pool = list(range((0, len(question_pool))))
    else:
        idx = random.choice(index_pool)
        index_pool.remove(idx)
        question = question_pool[idx]
        for language in language_list:
            question[language] = question[language].replace('[dt]', translate_word(item, language))
        return index_pool, question
    
def generate_questions_with_item_pair(index_pool, question_pool, item_pair, language_list):
    if not index_pool:
        index_pool = list(range((0, len(question_pool))))
    else:
        idx = random.choice(index_pool)
        index_pool.remove(idx)
        question = question_pool[idx]
        for language in language_list:
            # target
            question[language] = question[language].replace('[dt]', translate_word(item_pair[0], language))
            # reference
            question[language] = question[language].replace('[rf]', translate_word(item_pair[1], language))
        return index_pool, question
    