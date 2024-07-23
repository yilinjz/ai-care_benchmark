# coding: utf-8
import logging
import json

import ollama

from utils.const import language_list, model_id, benchmark_list
from utils.helper import process_context, get_instruction_type, translate_word


def ai_agent_remote(question, context, system_prompt, language):
    '''
    Client call to ollama
    '''
    question_prompt = f"{translate_word('Question', language)}:\n{question}\n\n"
    context_prompt = f"{translate_word('Context', language)}:\n{context}\n\n"
    messages = [
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": f"{question_prompt}{context_prompt}"}
    ]

    client = ollama.Client(host = "http://127.0.0.1:11434")
    response = client.chat(model=model_id, messages=messages)
    print(response)
    return response['message']['content']


def cmd_agent():
    '''
    Runs experiment
    '''
    log.info("SYSTEM: cmd agent start >>>>>")

    ### loops through list of benchmark files
    for benchmark_name in benchmark_list:
        data = json.load(open(f'benchmark/vqa/{benchmark_name}.json', encoding="utf8"))

        ### loops through each image
        for i, scene in enumerate(data):
            scene_id = scene['scene_id']
            context_json = json.load(open(f'benchmark/context/{scene_id}.json', encoding="utf8"))

            ### loops through each question
            for j, qa_pair in enumerate(scene['qa_pairs']):
                data[i]['qa_pairs'][j]['result'] = {}
                ### loops through each language (English, Mandarin and Cantonese)
                for language in language_list:
                    question = qa_pair['question'][language.value]
                    context = process_context(context_json, language)
                    path_to_instruction = f"benchmark/prompt/{get_instruction_type(benchmark_name)}.json"
                    system_prompt = json.load(open(path_to_instruction, encoding="utf8"))[language.value]
                    # run inferance
                    data[i]['qa_pairs'][j]['result'][language.value] = ai_agent_remote(
                        question=question,
                        context=context,
                        system_prompt=system_prompt,
                        language=language,
                    )   

        # print(benchmark_name)
        # print(path_to_instruction)

        model_name = model_id.replace(':', '_')
        with open(f'benchmark/experiment_result/{model_name}/{model_name}-{benchmark_name}-experiment_result.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)                 

    log.info("SYSTEM: cmd agent end <<<<<")


if __name__ == '__main__':
    log = logging.getLogger()
    # cmd agent init
    cmd_agent()
    