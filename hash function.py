def disp(hashTable):
    for i in range (len(hashTable)):
        print(i,end=" ")
        for j in hashTable[i]:
            print(">",end=" ")
            print(j,end=" ")
        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(HashTable,keyvalue,value):
    hashkey = Hashing(keyvalue)
    HashTable[hashkey].append(value)
insert(HashTable,10,"bihar")
insert(HashTable,10,"delhi")
insert(HashTable,27,"mumbai")
disp(HashTable)