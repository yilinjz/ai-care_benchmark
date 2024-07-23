##### MODEL ID #####

model_id = 'llama3'
# model_id = 'llama3:70b'
# model_id = 'mistral'
# model_id = 'gemma2'

# model_id = 'qwen2'
# model_id = 'qwen2:72b'
# model_id = 'glm4'

##### MODEL ID #####

from enum import Enum

class LANGUAGE(Enum):
    EN_US = 'en-US'
    ZH_CN = 'zh-CN'
    ZH_HK = 'zh-HK'

### supported languages ###
language_list = [
    LANGUAGE.EN_US,
    LANGUAGE.ZH_CN,
    LANGUAGE.ZH_HK,
]

MODEL_TO_TESTED_LANGUAGES = {
    'llama3': [
        LANGUAGE.EN_US
    ],
    'llama3:70b': [
        LANGUAGE.EN_US
    ],
    'mistral': [
        LANGUAGE.EN_US
    ],
    'gemma2': [
        LANGUAGE.EN_US
    ],
    'qwen2': [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ],
    'qwen2:72b': [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ],
    'glm4': [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ]
}
tested_languages = MODEL_TO_TESTED_LANGUAGES[model_id]

### list of benchmarks to run ###
benchmark_list = [
    'bathroom_existence',
    'bathroom_identification',
    'bathroom_location',
    'bathroom_multi-location',
]
