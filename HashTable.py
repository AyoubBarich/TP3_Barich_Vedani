import math
from itertools import repeat
import time
SIZEMAX=89

class HashTable:
    """
    HashTable is a class that implements a hash table with it s own hach function "getHash".
    HasTable : key() --> Value  
    we intilize the hashtable as empty and we can insert ,find , remove element from our self.keys
        
    """


    def __init__(self) :
        """intiates our hash table"""
        self.sizeMax=SIZEMAX
        self.size=0
        self.keys=dict(zip(range(SIZEMAX), repeat([])))
        

    
    def getHash(self,key:list):
        """
        returns: the hash value 

        param : key=type:list of charecters
        """
        K=0
        key.sort()
        for charcter in key:
            K+=ord(charcter)
        K=math.floor(K*math.pi)
        return K%self.sizeMax
        
    
    def get(self,key):
         """
         returns : the linked list associated with our index 
         param : key=type:list of charecters
         """
         hash= self.getHash(key)
         return self.keys[hash]
         
         
    def set(self,key,value):
        """
        returns: None

        param : key=type:list of charecters and Value 
        """
        self.size+=1
        hash = self.getHash(key)
        
        element = self.keys[hash]
        
        if element == []:
            self.keys.__setitem__(hash,[key,value])
        else:
            self.keys[hash].append(value)
    def remove(self,key):
        """
        removes the the value associated with our key in the hash table to equal an empty list

        returns: None

        param : key=type:list of charecters and Value 
        """
        hash = self.getHash(key)
        self.keys[hash]=[]
        
    
    def __str__(self):
        """Overides the print function"""
        res = "Hash Table:\n"
        for key in self.keys.keys():
            res+= 'Key: '+str(key)+' , Value : '
            for value in self.keys[key] :
                res+=str(value)+','
            res+='\n'
        return res
        
    def exists(self,key):
        """ 
        returns :True if the given key has stored values in the hash table
        param : key=type:list of charecters and Value
        """
        item = self.get(key)
        return (item !=[])

    def searchComplementary(self,multiset,showExecutionTime=False):
        """
        returns :the list containing the words that add uop to the 2 sum of the given multiset
        param : key=type:list of charecters and Value
        
        
        """
        start =time.time()
        for i in range(len(multiset)+1):
            Usubset=multiset[0:i]
             
            if self.exists(Usubset):
                Vsubset=multiset[i:len(multiset)]
                
                if self.exists(Vsubset):
                    if showExecutionTime:
                        print("Execution Time : ",(time.time())-start)
                    return "the words : "+str(self.keys[self.getHash(Usubset)])+"and"+str(self.keys[self.getHash(Vsubset)])+" are the 2-sum of the set "+str(multiset)
        

    