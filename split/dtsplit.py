import os
import random

from math import floor
from typing import List
from shutil import copy
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor

class Splitter:

    def __init__(self, 
                 dtpath:str,
                 outpath:str,
                 layout:str,
                 split_sizes:List[float], 
                 multithreading:bool = False) -> None:
        
        self.__dtpath = dtpath
        self.__outpath = outpath
        self.__layout = layout
        self.__split_sizes = split_sizes
        self.__nclasses = len(os.listdir(dtpath))
        self.__outdt = None
        self.__nworkers = None

        if multithreading:
            cpu_cores = cpu_count()
            self.__nworkers = self.__nclasses if cpu_cores >= self.__nclasses else cpu_cores

        pass

    def __create_structure(self) -> bool:

        self.__outdt = os.path.join(self.__outpath, "output")

        try:
            os.mkdir(self.__outdt)
        except OSError as _:
            print(f"The {self.__outdt} directory already exists!")
            return False

        # Assuming that at least the layout will be train_val, we can create those two folders
        # without any checking!
        os.mkdir(os.path.join(self.__outdt, "train"))
        os.mkdir(os.path.join(self.__outdt, "val"))
            
        if self.__layout == "train_val_test":
            os.mkdir(os.path.join(self.__outdt, "test")) 

        dt_c = os.listdir(self.__dtpath)

        for s in os.listdir(self.__outdt):
            for c in dt_c:
                os.mkdir(os.path.join(self.__outdt, s, c))
        
        return True
    
    def __class_split(self, class_name:str) -> None:

        files = os.listdir(os.path.join(self.__dtpath, class_name))
        n_files = len(files)

        paths = [os.path.join(self.__outdt, "train"), os.path.join(self.__outdt, "val")]

        max_tvt = []
        max_tvt.append(floor(n_files * self.__split_sizes[0]))
        max_tvt.append(floor(n_files * self.__split_sizes[1]))

        if self.__layout == "train_val_test":
            paths.append(os.path.join(self.__outdt, "test"))
            max_tvt.append(floor(n_files * self.__split_sizes[2]))
            files_counter = [0, 0, 0]
            random_options = [0, 1, 2]
            
        else:
            files_counter = [0, 0]
            random_options = [0, 1]

        finished_splitting = False

        for f in files:
            # In case of the splitting process has ended and we still have files
            # we will throw the files at the train set
            if finished_splitting:
                copy(os.path.join(self.__dtpath, class_name, f), 
                     os.path.join(paths[0], class_name, f))
                continue

            i = random.choice(random_options)

            copy(os.path.join(self.__dtpath, class_name, f), 
                 os.path.join(paths[i], class_name, f))
            
            files_counter[i] += 1

            if files_counter[i] == max_tvt[i]:
                random_options.remove(i)

                if len(random_options) == 0:
                    finished_splitting = True


    def start(self) -> None:

        classes = os.listdir(self.__dtpath)

        if self.__create_structure():
            if self.__nworkers == None:
                for c in classes:
                    self.__class_split(c)

            else:
                with ThreadPoolExecutor(self.__nworkers) as executor:
                    for i in range(0, self.__nclasses, self.__nworkers+1):
                        executor.map(self.__class_split, classes[i:i+self.__nworkers])
                        






    