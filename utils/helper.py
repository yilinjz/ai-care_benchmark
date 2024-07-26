import random
import copy

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
    orientation = None
    for obj in context:
        if obj['TEXT'] == item:
            orientation = obj['ORIENTATION']
    if not orientation:
        print(context)
        print(item)
        raise ValueError("Item Not Found In Context!")
    
    orientation = orientation.split()
    x_axis, y_axis = None, None
    for direction in orientation:
        if direction == 'up':
            y_axis = 1
        elif direction == 'down':
            y_axis = -1
        elif direction == 'slightly-up' or direction == 'slightly-down':
            y_axis = 0
        elif direction == 'left':
            x_axis = -1
        elif direction == 'right':
            x_axis = 1
        elif direction == 'slightly-left' or direction == 'slightly-right':
            x_axis = 0
        else:
            continue

    if x_axis == None and y_axis == None:
        print(orientation)
        raise ValueError("Cannot Decide Direction!")
    elif x_axis == None:
        x_axis = 0
    elif y_axis == None:
        y_axis = 0
    
    if x_axis == -1 and y_axis == -1:
        return WORD_DICTIONARY['down and left']
    elif x_axis == -1 and y_axis == 0:
        return WORD_DICTIONARY['left']
    elif x_axis == -1 and y_axis == 1:
        return WORD_DICTIONARY['up and left']
    elif x_axis == 0 and y_axis == -1:
        return WORD_DICTIONARY['down']
    elif x_axis == 0 and y_axis == 0:
        return WORD_DICTIONARY['center']
    elif x_axis == 0 and y_axis == 1:
        return WORD_DICTIONARY['up']
    elif x_axis == 1 and y_axis == -1:
        return WORD_DICTIONARY['down and right']
    elif x_axis == 1 and y_axis == 0:
        return WORD_DICTIONARY['right']
    elif x_axis == 1 and y_axis == 1:
        return WORD_DICTIONARY['up and right']
    else:
        return ValueError("Cannot Decide Quadrant!")
    