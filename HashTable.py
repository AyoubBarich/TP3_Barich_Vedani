import math
import LinkedList
class HashTable:
    """
    HashTable is a class that implements a hash table with it s own hach function "getHash".
    HasTable : key() --> Value  using Chain class to define the pair(key,value)
    we intilize thee hashtable as empty and we can insert ,find , remove element from our hashTable



    
    
    
    """


    def __init__(self,sizeMax=89) :
        self.sizeMax=sizeMax
        self.size=0
        self.keys=[None]*sizeMax

        
            
    
    def getHash(self,key):
        """
        returns: the index of the key in the hashTable

        param : key:"set of charecters" 
        """
        K=0
        for charcter in set(key):
            K+=ord(charcter)
        K=math.floor(K*math.pi)
        return K%self.sizeMax
        
    
    def __getitem__(self,key):
         """
         returns : the linked list associated with our index 
         param : key:"set of charecters" 
         """
         hash= self.getHash(key)
         linkedList = self.keys[hash]
         #we go throug our lonked list until we find the value associated with the hash
         while linkedList is not None and linkedList.key != hash:
            linkedList = linkedList.next
                
            if linkedList is None:
                    #not found 
                    return None
            else:
                    #found
                    return linkedList.value
            


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
