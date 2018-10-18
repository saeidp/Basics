#This techniques uses the chaining with bucket resizing to reduce collision
#Load Factor and Initial size of the bucket is the important parameters (load_factor, self.slots)

#Assume we have a hash table of size m, and that it currently has n entries. Then we call
# lambda = n/m the load factor of the hash table. The load factor can be seen as describing how 
#full the table currently is: A hash table with load factor 0.25 is 25% full, one with load factor
# 0.50 is 50% full, and so forth. If we have a hash table with load factor lambda then the probability
# that for the next key we wish to insert a collision occurs is lambda. Thus assumes that each key from
# the key space is equally likely, and that the hash function h spreads the key space evenly over 
#the set of indices of our array. If these optimistic assumptions fail, then the probability can be higher.
class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.next = None

class HashTable:
    def __init__(self):
        #Size of the HashTable
        self.slots = 10
        #Used while resizing the table when half of the table gets filled
        self.size = 0
        self.bucket = [None] * self.slots
        self.threshold = 0.6
    
    def get_size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def getIndex(self, key):
        hashCode = hash(key)
        index = hashCode % self.slots
        return index
    
    def insert(self, key, value):
        b_index = self.getIndex(key)
        if self.bucket[b_index] == None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size +=1
        else:
            head = self.bucket[b_index]
            while head != None:
                if head.key == key:
                    head.value = value
                    break
                elif head.next == None:
                    head.next = HashEntry(key, value)
                    self.size +=1
                    break
                head = head.next
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()
    
    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] *  new_slots
        # rehash all items into new slots
        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head !=None:
                new_index = self.getIndex(head.key)
                if new_bucket[new_index] == None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node != None:
                        if node.key == head.key:
                            node.value = head.value
                            break
                        elif node.next == None:
                            node.next = HashEntry(head.key, head.value)
                            break
                        node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    def search(self, key):
        b_index = self.getIndex(key)
        head = self.bucket[b_index]
        while head != None:
            if head.key == key:
                return head.value
            head = head.next
        return None    

    def delete(self, key):
        b_index = self.getIndex(key)
        head = self.bucket[b_index]
        if head == None:
            print("key not found")
            return None
        if head.key == key:
            self.bucket[b_index] = head.next
            print("key deleted!")
            self.size -= 1
            return head.key
        prev = None
        while head !=None:
            if head.key == key:
                if prev != None:
                    self.size -= 1
                    prev.next = head.next
                    print("Key Deleted!")
                    return head.key
            prev = head
            head = head.next

        print("key not found")
        return None    


table = HashTable() #Create a HashTable

print(table.isEmpty())
table.insert("This",1) 
table.insert("is",2 )
table.insert("a",3 )
table.insert("Test",4 )   
table.insert("Driver",5 )
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))
                

                