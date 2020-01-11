from dicts.chiquitoDict import chiquitoDict
from dicts import chiquitoExtendedDict
from random import randint

def simple_chiquito(type):
    chiquitoWords = chiquitoDict.array
    if type == 'extended':
        chiquitoWords = chiquitoExtendedDict.chiquitoExtended
    arrayLen = len(chiquitoWords)-1
    number = randint(0,arrayLen)
    return(chiquitoWords[number])