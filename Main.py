#we start by creating our universe which is the dictionnary of acceptable words

#we statrt by reading dicionnaire.txt

import fileinput as file
import math
import HashTable
UNIVERSE=[]
File = file.input("./mini")
for word in File:
    UNIVERSE.append(word.strip('\n'))

N=len(UNIVERSE)

PHI = (math.sqrt(5)-1)/2

TestDict=["art","rat","alice","bob"]

def HachFunction(K,const=2):
    
    return math.floor(const*(K*PHI-math.floor(K*PHI)))

def wordToCharList(word:str):
    return set(word)

def getKey(hachfunction,word):
    K=0
    for charcter in set(word):
        K+=ord(charcter)
    K=math.floor(K*math.pi)
    return hachfunction(K)

#for our hash table we are going to use a string of a set of the alphabet as keys 
# and the values associated with it are going to be the words accepted in dictionnary 
# that contain the same letters in the key

def Hashtable(dictionary=UNIVERSE,const=2):
    hashTable={}
    for i in range(const): 
        hashTable[i]={}
    for word in dictionary:
        
        charSet = wordToCharList(word)
        key= getKey(HachFunction,word)
        if str(charSet) not in hashTable[key]:
            hashTable[key][str(charSet)]=[word]
        if word not in hashTable[key][str(charSet)]:
                hashTable[key][str(charSet)].append(word)

    return hashTable

hashtable =HashTable.hashTableFromList()
print()



#version camille qui marche
# def HashTable():
#     hashTable=[]
#     for i in range (0,89):
#         hashTable.append([])
#     for word in UNIVERSE:
#         key = getKey(HachFunction,word)
#         hashTable[key].append(word)
#     return hashTable
