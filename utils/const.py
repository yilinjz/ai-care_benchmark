from enum import Enum

class LANGUAGE(Enum):
    EN_US = 'en-US'
    ZH_CN = 'zh-CN'
    ZH_HK = 'zh-HK'

### supported languages
language_list = [
    LANGUAGE.EN_US,
    LANGUAGE.ZH_CN,
    LANGUAGE.ZH_HK,
]

### list of benchmarks to run
benchmark_list = [
    'bathroom_existence',
    #'bathroom_identification',
    #'bathroom_location',
    #'bathroom_multi-location',
]
