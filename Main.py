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
    """
    returns: a hash table with all of the words in the given dictionary
    param: dictionary:list
    """
    start = time.time()
    ht = HashTable()
    for word in dictionary:
        key = [*word]
        ht.set(key,word)
    if showExecutionTime:
        print("Execution time : ",(time.time())-start)
    return ht


#############################TestMini############################(SIZEMAX = 107)
# Firstmultiset= ['a', 'd', 'e', 'e', 'i', 'i', 'l', 'n', 'n', 'n', 'o', 'r', 'u', 'x']
# Secondmultiset=['a', 'a', 'a', 'a', 'e', 'i', 'n', 'n', 'o', 'r', 's', 's', 's', 's', 't', 'w', 'z']
# print("Question1")
#dict= Dictionary(UNIVERSEmini,True)
#print(dict)
# print("Question2")
# print(dict.twoSum(Firstmultiset,True))
# print("Question3")
# print(Dictionary(UNIVERSEmini).twoSum(Secondmultiset))
#############################TestFull############################(SIZEMAX=141959)
# dict=Dictionary(UNIVERSE,True)
# TestSet1=['a', 'b', 'e', 'e', 'i', 'i', 'i', 'l', 'l', 'n', 'n', 'o', 'r', 'r', 's', 's', 't', 'y', 'z', 'é']
# TestSet2=['a', 'a', 'a', 'b', 'd', 'e', 'i', 'i', 'i', 'l', 'l', 'n', 'o', 'r', 'r', 'r', 's', 't', 'z', 'z']
# TestSet3=['a', 'a', 'd', 'e', 'h', 'i', 'm', 'n', 'n', 'o', 'o', 'r', 'r', 't', 't', 'x', 'z']
# Camille=sorted(['c','a','m','i','l','l','e','v','e','d','a','n','i'])
# Ayoub=sorted(['a','y','o','u','b','b','a','r','i','c','h'])
# print(dict)
#print(dict.get(['r','a','t']))
# print(dict.twoSum(TestSet1,True))
#print(dict.twoSum(TestSet2))
#print(dict.twoSum(TestSet3))
#print(dict.twoSum(Camille))
#print(dict.twoSum(Ayoub))

