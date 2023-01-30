import time
import os
from os import system

version = 1.0
author = "github.com/radcab"

#just some functions to make my life a whole lot easier
def coolTitle(title):
    system("title " + title)

def readFile(file):
    with open(file) as f:
        lines = f.readlines()
        new_lst = [x[:-1] for x in lines]
        return new_lst

def typeStr(str, delay):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(delay)
        
        
