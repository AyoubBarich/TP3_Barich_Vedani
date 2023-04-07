import math
from itertools import repeat
from itertools import combinations
import time

SIZEMAX=733
PHI = (1+math.sqrt(5))/2


class linkedList():
    """An implementation of a linked list where each element is a list where the first index containts 
    the set charecters of our word and the other indexes contains the string  of the words  """
    def __init__(self,element,next):
        """Intlize our class"""
        self.element=element
        self.next=next
        self.size=0


    def hasNext(self):
        """
        returns: true if self has a linkedlist to the left
        param : self
        """
        return (self.next is not None)
    
    def set(self,element):
        """
        traverses the Linkedlist until the last Linkedlist attaches a linked list wich contains element
        returns: None
        param : self,element:list
        """
        
        newlist = linkedList(element,None)
        current=self
        if current.hasNext():
            current=current.next
            current.set(element)
        current.next = newlist 
        self.size+=1

    def get(self):
       """
       return:elemnt in the current LinkedList
       param:self
       """
       return self.element
    def exists(self,element):
        """
        returns:True if element is in the linked list
        param: element:list
        """
        curr = self
        
        if curr.element!= element:
            if curr.hasNext:
                curr=curr.next
                curr.exists(element)
            else:return False
        

        return True


    
    def isEmpty(self):
        """
        returns:True if self is empty
        param:self
        """
        return ((self.element==[])&(self.next is None))
    
    def __iter__(self):
        """Overides the iteration function"""
        return self
    
    def __next__(self):
        """Overides the next function in iterable"""
        return self.next
    
    def getElementFromMuliset(self,multiset):
        """
        returns:the element in our linkred list associated with the charecter set of "multiSet"
        param:self , multiset:list
        """
        curr=self
        
        if not(curr.isEmpty()):
            if curr.element[0]!=sorted(multiset):
                if curr.hasNext():
                    curr=curr.next
                    curr.getElementFromMuliset(multiset)
                return None
            res=curr.element[1:]
            return res
        return None


    
    def __str__(self)->str:
        """Overides the print function"""
        res=str(self.element)
        if self.hasNext():
            res += self.next.__str__()
        return res 
    

class HashTable:
    """
    HashTable is a class that implements a hash table with its own hach function "getHash".
    HasTable : hash(key) --> Value = [multiSet,words asscociated with the multiSet ...] 
    we initialize the hashtable as empty and we can insert ,find elements from our hashtable.
        
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
        elemnt =item.getElementFromMuliset(key)
        return not(elemnt ==None)
    
    def getAllCombinationsOfaMultiSet(self,multiset):
        """
        returns:a list of all possible commbination of a charecter set
        param: multiset:list
        """
        res=[]
        for i in range(1,len(multiset)):
            for subSet in combinations(multiset, i):
                if subSet not in res:
                    res.append(subSet)
        return res
    
    
    def getComplementaryOfSet(self,multiset,set,allCombinations):
        """
        returns:list of all complements of set that add up to multiset
        param: multiset:list,set:list,allCombinations:list
        
        """
        res=[]
        for comb in allCombinations:
            
            if list(comb) not in res:
                sum= list(comb)
                sum=sum + list(set)
                sum =sorted(sum)
                
                if sum == multiset and self.exists(list(comb)):
                    res.append(list(comb))
        return res
            
    


    def twoSum (self,multiset,showExecutionTime=False):
        """
        returns:the couple of words(U,V) where the sum the set of charecters that make up U and V
        and add up to the multiSet 
        param: multiset:list
        """
        start =time.time()
        res=[]
        allCombinations =self.getAllCombinationsOfaMultiSet(multiset)
        allCombinationsOfAMultiSet=self.getAllCombinationsOfaMultiSet(multiset)
        allCombinationOfmultiSetandComplementary=[]
        max = len(allCombinationsOfAMultiSet)
        print(max)
        progress=0
        for combination in allCombinationsOfAMultiSet:
            progress+=1
            for complementary in self.getComplementaryOfSet(multiset,combination,allCombinations):
                print("combination : ",combination,"complementary :",complementary)
                allCombinationOfmultiSetandComplementary.append((list(combination),list(complementary)))
        
        for couple in allCombinationOfmultiSetandComplementary:
            combination = self.get(list(couple[0])).getElementFromMuliset(list(couple[0]))
            complementary=self.get(list(couple[1])).getElementFromMuliset(list(couple[1]))
            if not(combination is None and complementary is None):
                res.append((combination,complementary))

        if showExecutionTime:
            print("Execution Time : ",time.time()-start)
        return res

      

    