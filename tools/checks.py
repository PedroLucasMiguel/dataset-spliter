from os import path, listdir
from argparse import Namespace

class DatasetStructureNotValidException(Exception):
    pass

class InvalidPathException(Exception):
    pass

class InvalidSplitSizeException(Exception):
    pass

class InvalidManualSeedException(Exception):
    pass

def check_args(args:Namespace) -> None:

    if not path.isdir(args.dataset_path):
        raise InvalidPathException
    
    if args.dataset_output_path != None:
        if not path.exists(args.dataset_output_path):
            raise InvalidPathException
    
    sz = len(args.split_size)

    if (args.layout == "train_val" and sz != 2) or (args.layout == "train_val_test" and sz != 3):
        raise InvalidSplitSizeException
    
    s = sum(args.split_size)

    assert s <= 1.0 and s >= 0.0, "The size of splits must sum up to 1.0"

    if args.manual_seed != None and args.manual_seed < 0:
        raise InvalidManualSeedException

def check_dataset_structure(dataset_path:str) -> None:

    for item in listdir():
        if path.isfile(path.join(dataset_path, item)):
            raise DatasetStructureNotValidException