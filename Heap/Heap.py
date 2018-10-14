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
    def maxHeapify(self, heaplist, index, heapSize):
        largest = index
        while(largest < heapSize // 2):
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heapSize and heaplist[left] > heaplist[index]:
                largest = left
            if right < heapSize and heapList[right] > heaplist[largest]:
                largest = right
            if largest != index:
                temp=heaplist[index]
                heaplist[index] = heaplist[largest]
                heaplist[largest] = temp
                index = largest
            else:
                break
    
    def BuildMaxHeap(self, heaplist, heapSize):
        for i in range((heapSize - 1)//2, -1, -1):
            self.maxHeapify(heaplist, i, heapSize)
    
heapList = [1, 4, 7, 12, 15, 14, 9, 2, 3, 16]
print("Before Heapyfy: ", str(heapList))
h = Heap()
h.BuildMaxHeap(heapList, len(heapList))
print("After heapyfy: ", str(heapList))



                
