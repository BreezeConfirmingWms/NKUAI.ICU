"""
@Project ：ICUdevWebBackend
@File    ：parseJsonSort.py
@Author  ：BreezeConfirming
@Date    ：2024/1/26 下午12:22

=====================
Edited On PyCharm
Developing Time Stamp <- 2024
=====================

@CopyRight YanMing all right reserved

"""

import os
from pathlib import Path,PosixPath
from argparse import ArgumentParser


import re
from regex import  compile,template,findall

from xml.etree import  ElementTree as etree
import json

import yaml
import markdown



from easydict import EasyDict as edict
from collections import deque,OrderedDict
from queue import PriorityQueue






import multiprocessing
import subprocess




def  worker(num):
    print("Worker:",num)

if __name__=="__main__":
   my_jobs=[]
   for i in range(5):
       p=multiprocessing.Process(target=worker,args=(i,))
       my_jobs.append(p)
       p.start()





