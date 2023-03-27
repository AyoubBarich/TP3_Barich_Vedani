import math
class HashTable:
    """
    HashTable is a class that implements a hash table with it s own hach function "getHash".
    HasTable : key() --> Value  

    
    
    
    """

    def __init__(self,sizeMax=89) :
        self.sizeMax=sizeMax
        self.size=0
        self.values=[None]*sizeMax

        
            
    
    def getHash(self,key):
        K=0
        for charcter in set(key):
            K+=ord(charcter)
        K=math.floor(K*math.pi)
        return K%self.sizeMax
        
    
    def __getitem__(self,index):
         hash= self.getHash(index)
         return self[hash]

    def __setitem__(self,key,value):
        self.size+=1
        hash = self.getHash(key)
        charSet=self.wordToCharSet(value)
        if str(charSet) not in self[hash]:
            self[key][str(charSet)]=[value]
        if value not in self[key][str(charSet)]:
                self[key][str(charSet)].append(value)

    def wordToCharSet(self,word:str):
         return set(word)
    

    def hashTableFromList(self,list:list):
         i=0
         for item in list:
              key = self.wordToCharSet(item)
              self.__setitem__(key,item)
              i+=1
         return self
