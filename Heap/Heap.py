#nLog(n)
#Heaps can be implemented using lists. Initially, elements are
# placed in nodes in the same order as they appear in the list.
# Then a function is called over the whole heap in a bottom-up
# manner that “Max Heapifies” this heap so that the heap 
# property is satisfied on all nodes.
# When we say bottom up, we mean the function starts from the
# last parent node present at n/2th position of list and 
# performs a check if the values at child nodes are smaller
# than parent node.
class Heap:
    #MaxHeapify(): This functions takes the node value and
    # compares it with the key at parent node. It swaps if 
    # childNode >= parentNode. The while loop makes sure that 
    # the nodes keep swapping until heap property is satisfied.
    def maxHeapify(self, heapList, index, heapSize):
        largest = index
        while(largest < heapSize // 2):
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heapSize and heapList[left] > heapList[index]:
                largest = left
            if right < heapSize and heapList[right] > heapList[largest]:
                largest = right
            if largest != index:
                heapList[index],heapList[largest] = heapList[largest], heapList[index]
                index = largest
            else:
                break
    
    def BuildMaxHeap(self, heapList, heapSize):
        for i in range((heapSize - 1)//2, -1, -1):
            self.maxHeapify(heapList, i, heapSize)
    
    # Min Heap follows Min Heap property which means the key at the
    # parent node is always smaller than keys at both child nodes
    # he function starts from the last parent node present
    # n/2th position of the list and checks if the values at
    # child nodes are greater than parent node, if yes then
    # swap the values. If no, then move to the next parent node
    def minHeapify(self, heapList, index, heapSize):
        smallest = index
        while smallest < heapSize // 2:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heapSize and heapList[left] < heapList[index]:
                smallest = left
            if right < heapSize and heapList[right] < heapList[smallest]:
                smallest = right
            if smallest != index:
                heapList[index], heapList[smallest] = heapList[smallest], heapList[index]
                index = smallest
            else:
                break
    def BuildMinHeap(self, heapList, heapSize):
        for i in range((heapSize - 1)//2, -1, -1):
            self.minHeapify(heapList, i, heapSize)
    

heapList = [1, 4, 7, 12, 15, 14, 9, 2, 3, 16]
print("Before Heapyfy: ", str(heapList))

h = Heap()
h.BuildMaxHeap(heapList, len(heapList))
print("After max heapify: ", str(heapList)) #[16, 15, 14, 12, 4, 7, 9, 2, 3, 1]
h.BuildMinHeap(heapList, len(heapList))
print("After min heapify: ", str(heapList)) #[1, 2, 7, 3, 4, 14, 9, 12, 16, 15]

#---------------------------------------------------------------
# Custom min heap
class MinHeap:
    def __init__(self):
        self.heap = []
        self.last_index = -1
    def push(self, value):
        self.last_index += 1
        if self.last_index < len(self.heap):
            self.heap[self.last_index] = value
        else:
            self.heap.append(value)
        self.siftup(self.last_index)

    def pop(self):
        if self.last_index == -1:
            raise IndexError('pop from empty heap')

        min_value = self.heap[0]

        self.heap[0] = self.heap[self.last_index]
        self.last_index -= 1
        self.siftdown(0)

        return min_value
    
    def siftup(self, index):
        while index > 0:
            parent_index, parent_value = self.get_parent(index)

            if parent_value <= self.heap[index]:
                break

            self.heap[parent_index], self.heap[index] =\
                self.heap[index], self.heap[parent_index]

            index = parent_index

    def siftdown(self, index):
        while True:
            index_value = self.heap[index]

            left_child_index, left_child_value = self.get_left_child(index, index_value)
            right_child_index, right_child_value = self.get_right_child(index, index_value)

            if index_value <= left_child_value and index_value <= right_child_value:
                break

            if left_child_value < right_child_value:
                new_index = left_child_index
            else:
                new_index = right_child_index

            self.heap[new_index], self.heap[index] =\
                self.heap[index], self.heap[new_index]

            index = new_index
    
    def get_parent(self, index):
        if index == 0:
            return None, None

        parent_index = (index - 1) // 2

        return parent_index, self.heap[parent_index]

    def get_left_child(self, index, default_value):
        left_child_index = 2 * index + 1

        if left_child_index > self.last_index:
            return None, default_value

        return left_child_index, self.heap[left_child_index]

    def get_right_child(self, index, default_value):
        right_child_index = 2 * index + 2

        if right_child_index > self.last_index:
            return None, default_value

        return right_child_index, self.heap[right_child_index]

    def __len__(self):
        return self.last_index + 1

mh = MinHeap()
mh.push(31)
mh.push(11)
mh.push(7)
mh.push(12)
mh.push(15)
mh.push(14)
mh.push(9)
mh.push(2)
mh.push(3)
mh.push(16)
#print("After min heapify: ", str(mh.heap))
for i in range(len(mh.heap)):
    print(mh.pop(), end=" " ) # 2 3 7 9 11 12 14 15 16 31 

# values = random.sample(range(10000), 10)
# print(values)

# h = Heap()
# for v in values:
#     h.push(v)

# while len(h) > 0:
#     print(h.pop(), end=' ')


