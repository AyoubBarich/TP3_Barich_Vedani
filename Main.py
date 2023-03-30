#we start by creating our universe which is the dictionnary of acceptable words

#we statrt by reading dicionnaire.txt

import fileinput as file
import math
import time
from HashTable import HashTable



def readFileToList(filepath):
    UNIVERSE=[]
    File = file.input(filepath)
    for word in File:
        UNIVERSE.append(word.strip('\n'))
    return UNIVERSE

UNIVERSEmini=readFileToList("./mini")
UNIVERSE=readFileToList("./dictionnaire")




def Dictionary(dictionary,showExecutionTime=False):
    start = time.time()
    ht = HashTable()
    for word in dictionary:
        key = [*word]
        ht.set(key,word)
    if showExecutionTime:
        print("Execution time : ",(time.time())-start)
    return ht


#############################TestMini############################
Firstmultiset= ['a', 'd', 'e', 'e', 'i', 'i', 'l', 'n', 'n', 'n', 'o', 'r', 'u', 'x']
Secondmultiset=['a', 'a', 'a', 'a', 'e', 'i', 'n', 'n', 'o', 'r', 's', 's', 's', 's', 't', 'w', 'z']
Dictionary(UNIVERSEmini,True)
print(Dictionary(UNIVERSEmini))
print(Dictionary(UNIVERSEmini).twosum(Firstmultiset,True))
print(Dictionary(UNIVERSEmini).twosum(Secondmultiset,True))
#############################TestFull############################





#version camille qui marche
# def HashTable():
#     hashTable=[]
#     for i in range (0,89):
#         hashTable.append([])
#     for word in UNIVERSE:
#         key = getKey(HachFunction,word)
#         hashTable[key].append(word)
#     return hashTable
