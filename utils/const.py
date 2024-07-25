##### MODEL ID #####

# model_id = 'llama3'
model_id = 'llama3:70b'
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
    test_location
    # # bathroom
    # 'bathroom_existence',
    # 'bathroom_identification',
    # 'bathroom_location',
    # 'bathroom_multi-location',
    # # bedroom
    # 'bedroom_existence',
    # 'bedroom_identification',
    # 'bedroom_location',
    # 'bedroom_multi-location',
    # # dining_room
    # 'dining_room_existence',
    # 'dining_room_identification',
    # 'dining_room_location',
    # 'dining_room_multi-location',
    # # doorway
    # 'doorway_existence',
    # 'doorway_identification',
    # 'doorway_location',
    # 'doorway_multi-location',
    # # kitchen
    # 'kitchen_existence',
    # 'kitchen_identification',
    # 'kitchen_location',
    # 'kitchen_multi-location',
    # # living_room
    # 'living_room_existence',
    # 'living_room_identification',
    # 'living_room_location',
    # 'living_room_multi-location',
    # # playroom
    # 'playroom_existence',
    # 'playroom_identification',
    # 'playroom_location',
    # 'playroom_multi-location',
    # # lobby
    # 'lobby_existence',
    # 'lobby_identification',
    # 'lobby_location',
    # 'lobby_multi-location',
    # # meeting_room
    # 'meeting_room_existence',
    # 'meeting_room_identification',
    # 'meeting_room_location',
    # 'meeting_room_multi-location',
    # # pantry
    # 'pantry_existence',
    # 'pantry_identification',
    # 'pantry_location',
    # 'pantry_multi-location',
    # # workstation
    # 'workstation_existence',
    # 'workstation_identification',
    # 'workstation_location',
    # 'workstation_multi-location',
    # # bookstore
    # 'bookstore_existence',
    # 'bookstore_identification',
    # 'bookstore_location',
    # 'bookstore_multi-location',
    # # classroom
    # 'classroom_existence',
    # 'classroom_identification',
    # 'classroom_location',
    # 'classroom_multi-location',
    # # coffee_shop
    # 'coffee_shop_existence',
    # 'coffee_shop_identification',
    # 'coffee_shop_location',
    # 'coffee_shop_multi-location',
    # # computer_lab
    # 'computer_lab_existence',
    # 'computer_lab_identification',
    # 'computer_lab_location',
    # 'computer_lab_multi-location',
    # # dorm
    # 'dorm_existence',
    # 'dorm_identification',
    # 'dorm_location',
    # 'dorm_multi-location'
]
