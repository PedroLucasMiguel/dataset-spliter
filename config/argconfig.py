'''
        short arg, 
        long arg, 
        nargs, 
        const, 
        choices, 
        action, 
        type, 
        required
'''
from enum import Enum

class Config(Enum):
    SHORT_ARG = 0
    LONG_ARG = 1
    NARGS = 2
    CONST = 3
    CHOICES = 4
    ACTION = 5
    TYPE = 6
    REQUIRED = 7

args_config = (
    ("-dtp", "--dataset_path", None, None, None, None, str, True),
    ("-dto", "--dataset_output_path", None, None, None, None, str, False),
    ("-l", "--layout", "?", "all", ["train_val", "train_val_test"], None, str, True),
    ("-ss", "--split_size", "+", None, None, None, float, True),
    ("-inp", "--in_place", None, None, None, "store_true", bool, False),
    ("-ms", "--manual_seed", None, None, None, None, int, False),
    ("-umt", "--use_multi_threading", None, None, None, "store_true", bool, False),
)