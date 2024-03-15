# dataset-splitter
A utily to help split datasets

## Args

```bash
-dtp or --dataset_path -> Receives the dataset path
# Example: python dts.py -dtp ../dataset

-dto or --dataset_output_path -> Set the output dataset directory
# Example: python dts.py -dtp ../dataset -dto splitted_dataset

-l or --layout -> Defines the layout of the final dataset #["train_val", "train_val_test"]
# Example: python dts.py -dtp ../dataset -dto splitted_dataset -l train_val_test

-ss or --split_size -> Defines the size of each split
# Example: python dts.py -dtp ../dataset -dto splitted_dataset -l train_val_test -ss 0.8,0.2

-ms or --manual_seed -> Defines a manual seed for the split
# Example: python dts.py -dtp ../dataset -dto splitted_dataset -l train_val_test -ss 0.8,0.2 -ms 1212

-umt or --use_multi_threading -> Defines if the split process will or not be multithreaded
# Example: python dts.py -dtp ../dataset -dto splitted_dataset -l train_val_test -ss 0.8,0.2 -umt
```