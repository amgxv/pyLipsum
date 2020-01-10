from dicts.chiquitoDict import chiquitoDict
from random import randint

def simple_chiquito():
    chiquitoWords = chiquitoDict.array
    number = randint(0,len(chiquitoWords))
    return(chiquitoWords[number])
