import Main

def Test_Multiensemble():
    TestDict=["art","rat","alice","bob"]
    assert(({"{'t', 'r', 'a'}": ['art', 'rat']}) in Main.HashTable(TestDict,2).values())