import random
import copy
from collections import Counter

from utils.dictionary import WORD_DICTIONARY

# pre-processing json data
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

# match benchmark to json
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

# translate
def translate_word(word, language):
    return WORD_DICTIONARY[word][language]

def generate_open_questions(question_pool):
    return [
        random.choice(question_pool[0:5]),
        random.choice(question_pool[5:11]),
        random.choice(question_pool[11:17]),
        random.choice(question_pool[17:23]),
        random.choice(question_pool[23:29])
    ]

# pick question from pool
def generate_questions(question_pool, item):
    return random.choice(question_pool[item])
    
def generate_questions_with_item_pair(question_pool, item_pair, language_list):
    question = copy.deepcopy(random.choice(question_pool))
    for language in language_list:
        # target
        question[language] = question[language].replace('[dt]', translate_word(item_pair[0], language))
        # reference
        question[language] = question[language].replace('[rf]', translate_word(item_pair[1], language))
    return question

def generate_location_answers(context, item):
    candidate_pool = []

    for obj in context:
        if obj['TEXT'] == item:
            candidate_pool.append(obj['ORIENTATION'].replace('slightly-', ''))
    if not candidate_pool:
        print(context)
        print(item)
        raise ValueError("Item Not Found In Context!")
    
    counts = Counter(candidate_pool)
    answer = max(counts, key=counts.get)
    return WORD_DICTIONARY[answer]
    