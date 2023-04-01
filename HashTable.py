import math
from itertools import repeat
from itertools import combinations
import time
SIZEMAX=89
PHI = (1+math.sqrt(5))/2


class linkedList():
    def __init__(self,element,next):
        self.element=element
        self.next=next
        self.size=0


    def hasNext(self):
            return (self.next is not None)
    
    def set(self,element):
        
        newlist = linkedList(element,None)
        current=self
        if current.hasNext():
            current=current.next
            current.set(element)
        current.next = newlist 
        self.size+=1

    def get(self):
       return self.element
    
    def isEmpty(self):
        return ((self.element==[])&(self.next is None))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next
    
    def __str__(self)->str:
        res=str(self.element)
        if self.hasNext():
            res += self.next.__str__()
        return res 
    
    # def getElements(self):
    #     currentElement=self
    #     currentElementlist = [self.element[0]]
    #     if currentElement.hasNext():
    #         currentElement=currentElement.next
    #         currentElementlist.append(currentElement.getElements())
    #     return currentElementlist
  

    # def getElementFromIndex(self,index):
        
    #     currentnode=self
    #     if currentnode.size!=index:
    #         if currentnode.hasNext():
    #             currentnode=self.next
          
    #     return currentnode.element
        
            


        

        
    
   



        

        

class HashTable:
    """
    HashTable is a class that implements a hash table with its own hach function "getHash".
    HasTable : hash(key) --> Value = [multiSet,words asscociated with the multiSet] 
    we initialize the hashtable as empty and we can insert ,find , remove element from our hashtable.
        
    """


    def __init__(self) :
        """initiates our hash table"""
        self.sizeMax=SIZEMAX
        self.size=0
        self.keys=dict(zip(range(SIZEMAX), repeat(linkedList([],None))))
        

    
    def getHash(self,key:list):
        """
        returns: the hash value 

        param : key=type:list of charecters
        """
        K=0
        key.sort()
        for charcter in key:
            K+=ord(charcter)
        K=math.floor(K*PHI)
        return K%self.sizeMax
        
    
    def get(self,key):
         """
         returns : the list associated with our index 
         param : key=type:list of characters
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
        linkedlist = self.keys[hash]
        
        if linkedlist.isEmpty():
            self.keys.__setitem__(hash,linkedList([key,value],None))
            return True
        # print(self.keys[hash].getElements())
        # print('key',key)
        # if key in self.keys[hash].getElements():
            
        #     index=self.keys[hash].getElements().index(key)
        #     target = self.keys[hash]
        #     for i in range(0,index):
        #         if target.next is not None:
        #             target=target.next
        #         break;
        #     if value not in target.element:
        #         self.keys[hash].element.append(value)
        # elements=self.keys[hash].getElements()
    
    
        # if key in elements:
        #     elementIndex=elements.index(key)
        #     node=self.keys[hash]
        #     if value not in node.getElementFromIndex(elementIndex) :
        #         node.getElementFromIndex(elementIndex).append(value)
        while linkedlist is not None:
            if key in linkedlist.element:
                if value not in linkedlist.element:
                    linkedlist.element.append(value)
                    return True
            linkedlist=linkedlist.next

        self.keys[hash].set([key,value])
        return True
        



    def __str__(self):
        """Overides the print function"""
        res = "Hash Table:\n"
        for key in self.keys.keys():
            res+= 'Key: '+str(key)+' , Value : '
            res+=str(self.keys[key])+','
            res+='\n'
        return res
        
    def exists(self,key):
        """ 
        returns :True if the given key has stored values in the hash table
        param : key=type:list of charecters and Value
        """
        item = self.get(key)
        return not(item.isEmpty())
    
    def getAllCombinationsOfaMultiSet(self,multiset):
        res=[]
        for i in range(1,len(multiset)):
            for subSet in combinations(multiset, i):
                if subSet not in res:
                    res.append(subSet)
        return res
    def getComplementaryOfSet(self,multiset,set):
        allCombinations=self.getAllCombinationsOfaMultiSet(multiset)
        for comb in allCombinations: 
            sum= list(comb)
            sum=sum +set
            sum =sorted(sum)
            if sum == multiset:
                return list(comb)
    



    # def twosum(self,multiset,showExecutionTime=False):
    #     """
    #     returns :the list containing the words that add up to the 2 sum of the given multiset
    #     param : key=type:list of charecters and Value
        
        
    #     """

      

    