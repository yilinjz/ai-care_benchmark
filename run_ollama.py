# coding: utf-8
import logging
import json

import ollama

from utils.const import model_id, tested_languages, benchmark_list, SUBTASK
from utils.helper import translate_word, process_context, get_instruction_prompt_type, calculate_score


def ai_agent_remote(question, context, system_prompt, language):
    '''
    Client call to ollama
    '''
    question_prompt = f"{translate_word('Question', language)}: {question}\n"
    context_prompt = f"{translate_word('Context', language)}: {context}\n"
    messages = [
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": f"{question_prompt}{context_prompt}"}
    ]

    client = ollama.Client(host = "http://127.0.0.1:11434")
    response = client.chat(model=model_id.value, messages=messages)
    # print(response)
    print(response['message']['content'])
    return response['message']['content']

def cmd_agent():
    '''
    Runs experiment
    '''
    log.info("SYSTEM: cmd agent start >>>>>")

    ### loops through list of benchmark files
    for benchmark_name in benchmark_list:
        print(benchmark_name)
        if SUBTASK.OBJECT_DETECTION.value in benchmark_name:
             category_tag = SUBTASK.OBJECT_DETECTION
        elif SUBTASK.SEMANTIC_MATCHING.value in benchmark_name:
             category_tag = SUBTASK.SEMANTIC_MATCHING
        elif SUBTASK.QUESTION_GENERATION.value in benchmark_name:
             category_tag = SUBTASK.QUESTION_GENERATION
        else:
            raise ValueError("Unknown Subtask!")

        data = json.load(open(f'benchmark/vqa/{category_tag.value}/{benchmark_name}.json', encoding="utf8"))

        ### loops through each image
        for i, scene in enumerate(data):
            scene_id = scene['scene_id']
            context_json = json.load(open(f'benchmark/context/{scene_id}.json', encoding="utf8"))

            ### loops through each question
            for j, qa_pair in enumerate(scene['qa_pairs']):
                data[i]['qa_pairs'][j]['result'] = {}
                ### loops through each language (English, Mandarin and Cantonese)
                for language in tested_languages:
                    question = qa_pair['question'][language.value]
                    context = process_context(context_json, language)
                    path_to_instruction = f"benchmark/prompt/{get_instruction_prompt_type(benchmark_name)}.json"
                    system_prompt = json.load(open(path_to_instruction, encoding="utf8"))[language.value]
                    # run inferance
                    data[i]['qa_pairs'][j]['result'][language.value] = ai_agent_remote(
                        question=question,
                        context=context,
                        system_prompt=system_prompt,
                        language=language,
                    )   

        model_name = model_id.value.replace(':', '_')
        result_path = f'benchmark/experiment_result/{model_name}/{model_name}-{benchmark_name}-experiment_result.json'
        with open(result_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)   
        calculate_score(result_path, category_tag, tested_languages)              

    log.info("SYSTEM: cmd agent end <<<<<")
    return result_path


if __name__ == '__main__':
    log = logging.getLogger()
    # cmd agent init
    cmd_agent()
    