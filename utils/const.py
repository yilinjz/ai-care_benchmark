from enum import Enum


### MODEL ID ###
class MODEL(Enum):
    LLAMA_3 = 'llama3'
    LLAMA_3_70B = 'llama3:70b'
    MISTRAL = 'mistral'
    GEMMA_2 = 'gemma2'
    QWEN_2 = 'qwen2'
    QWEN_2_72B = 'qwen2:72b'
    GLM_4 = 'glm4'

model_id = MODEL.LLAMA_3


### subtasks ###
class SUBTASK(Enum):
    OBJECT_DETECTION = 'object_detection'
    SEMANTIC_MATCHING = 'semantic_matching'
    QUESTION_GENERATION = 'question_generation'

subtask_list = [
    SUBTASK.OBJECT_DETECTION,
    SUBTASK.SEMANTIC_MATCHING,
    SUBTASK.QUESTION_GENERATION,
]


### supported languages ###
class LANGUAGE(Enum):
    EN_US = 'en-US'
    ZH_CN = 'zh-CN'
    ZH_HK = 'zh-HK'

language_list = [
    LANGUAGE.EN_US,
    LANGUAGE.ZH_CN,
    LANGUAGE.ZH_HK,
]

TESTED_LANGUAGES_BY_MODEL = {
    MODEL.LLAMA_3: [
        LANGUAGE.EN_US
    ],
    MODEL.LLAMA_3_70B: [
        LANGUAGE.EN_US
    ],
    MODEL.MISTRAL: [
        LANGUAGE.EN_US
    ],
    MODEL.GEMMA_2: [
        LANGUAGE.EN_US
    ],
    MODEL.QWEN_2: [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ],
    MODEL.QWEN_2_72B: [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ],
    MODEL.GLM_4: [
        LANGUAGE.ZH_CN,
        LANGUAGE.ZH_HK,
    ]
}

tested_languages = TESTED_LANGUAGES_BY_MODEL[model_id]


### list of benchmarks to run ###
benchmark_list = [
    # bathroom #
    'bathroom_object_detection',
    'bathroom_semantic_matching',
    # bedroom #
    'bedroom_object_detection',
    'bedroom_semantic_matching',
    # dining_room #
    'dining_room_object_detection',
    'dining_room_semantic_matching',
    # doorway #
    'doorway_object_detection',
    'doorway_semantic_matching',
    # kitchen #
    'kitchen_object_detection',
    'kitchen_semantic_matching',
    # living_room #
    'living_room_object_detection',
    'living_room_semantic_matching',
    # playroom #
    'playroom_object_detection',
    'playroom_semantic_matching',
    # lobby #
    'lobby_object_detection',
    'lobby_semantic_matching',
    # meeting_room #
    'meeting_room_object_detection',
    'meeting_room_semantic_matching',
    # pantry #
    'pantry_object_detection',
    'pantry_semantic_matching',
    # workstation #
    'workstation_object_detection',
    'workstation_semantic_matching',
    # bookstore #
    'bookstore_object_detection',
    'bookstore_semantic_matching',
    # classroom #
    'classroom_object_detection',
    'classroom_semantic_matching',
    # coffee_shop #
    'coffee_shop_object_detection',
    'coffee_shop_semantic_matching',
    # computer_lab #
    'computer_lab_object_detection',
    'computer_lab_semantic_matching',
    # dorm #
    'dorm_object_detection',
    'dorm_semantic_matching',
]
