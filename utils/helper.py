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
