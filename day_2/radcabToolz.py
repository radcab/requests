import time

version = 1.0
author = "github.com/radcab"

#just some functions to make my life a whole lot easier
def readFile(file):
    with open(file) as f:
        lines = f.readlines()
        return lines
    
def typeStr(str, delay):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(delay)
        
        
