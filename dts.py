import argparse

from split.dtsplit import Splitter
from config.argconfig import args_config, Config
from tools.checks import check_args, check_dataset_structure

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Dataset Splitter",
                                     "python dts.py <args>",
                                     "Creates a splited dataset")

    for config in args_config:
        if config[Config.ACTION.value] is None:
            parser.add_argument(config[Config.SHORT_ARG.value], config[Config.LONG_ARG.value], 
                                nargs=config[Config.NARGS.value],
                                const=config[Config.CONST.value],
                                choices=config[Config.CHOICES.value],
                                type=config[Config.TYPE.value], 
                                required=config[Config.REQUIRED.value])
        else:
            parser.add_argument(config[Config.SHORT_ARG.value], config[Config.LONG_ARG.value], 
                                action=config[Config.ACTION.value], 
                                required=config[Config.REQUIRED.value])

    args = parser.parse_args()

    check_args(args)
    check_dataset_structure(args.dataset_path)

    Splitter(args.dataset_path, 
             args.dataset_output_path if args.dataset_output_path != None else ".",
             args.layout,
             args.split_size, 
             args.use_multi_threading).start()