# coding: utf-8
import logging
import json

import ollama

from utils.const import model_id, tested_languages, benchmark_list
from utils.helper import process_context, get_instruction_type, translate_word


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
    response = client.chat(model=model_id, messages=messages)
    # print(response)
    print(response['message']['content'])
    return response['message']['content']

def calculate_score(result_path):
     data = json.load(open(result_path, encoding="utf8"))
     for language in tested_languages:
        total_count = 0
        correct_count = 0
        for scene in data:
            for qa_pair in scene['qa_pairs']:
                total_count += 1
                answers = json.loads(qa_pair['answer'][language.value])
                for i, answer in enumerate(answers):
                    answers[i] = answer.replace(" ", "")
                result = qa_pair['result'][language.value].replace(" ", "")
                if result in answers:
                    correct_count += 1
        print(f"LANGUAGE: {language.value} | CORRECT: {correct_count} | TOTAL: {total_count} | SCORE: {correct_count/total_count}")    

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
                for language in tested_languages:
                    question = qa_pair['question'][language.value]
                    context = process_context(context_json, language)
                    path_to_instruction = f"benchmark/prompt/{get_instruction_type(benchmark_name)}.json"
                    system_prompt = json.load(open(path_to_instruction, encoding="utf8"))[language.value]
                    # run inferance
                    print(benchmark_name)
                    data[i]['qa_pairs'][j]['result'][language.value] = ai_agent_remote(
                        question=question,
                        context=context,
                        system_prompt=system_prompt,
                        language=language,
                    )   

        # print(benchmark_name)
        # print(path_to_instruction)

        model_name = model_id.replace(':', '_')
        result_path = f'benchmark/experiment_result/{model_name}/{model_name}-{benchmark_name}-experiment_result.json'
        with open(result_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)   
        calculate_score(result_path)              

    log.info("SYSTEM: cmd agent end <<<<<")
    return result_path


if __name__ == '__main__':
    log = logging.getLogger()
    # cmd agent init
    cmd_agent()
    