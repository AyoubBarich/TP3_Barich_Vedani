#we start by creating our universe which is the dictionnary of acceptable words

#we statrt by reading dicionnaire.txt

import fileinput as file
import math
import time
import sys
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
dict= Dictionary(UNIVERSEmini,True)
# print(Dictionary(UNIVERSEmini))

print(dict.twoSum(Firstmultiset))
#print(Dictionary(UNIVERSEmini).twoSum(Secondmultiset))
#############################TestFull############################
R=['a','o','u','u']
ht = HashTable()
ht.set(['t','r','a'],"art")
ht.set(['t','r','a'],"rat")
ht.set(['c', 'e', 'h', 'r', 't', 'é'],"rta")
ht.set(['c', 'e', 'h', 'r', 't', 'é'],"cet")
ht.set(['e', 'i', 'l', 't', 'u'],'mm')
ht.set(['e', 'i', 'l', 't', 'u'],'hello')
ht.set(['u','s','a'],"usa")
ht.set(['a','u'],"au")
ht.set(['o','u'],"ou")
ht.set(['d', 'e', 'i', 'i', 'n', 'o', 'x'],"dioxine")

# print(ht)
# print(ht.twoSum(R))

# print(ht.getComplementaryOfSet(['a','o','u','u'],['a','u']))




#version camille qui marche
# def HashTable():
#     hashTable=[]
#     for i in range (0,89):
#         hashTable.append([])
#     for word in UNIVERSE:
#         key = getKey(HachFunction,word)
#         hashTable[key].append(word)
#     return hashTable
