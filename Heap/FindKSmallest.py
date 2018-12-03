class Heap:
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
#--------------------------------------------------------------------

# You find the first k smallest elements
# my_list = [9,4,7,1,-2,6,5]        k = 3
# Output -> [-2,1,4]
def findKSmallest(my_list, k):
    result = []
    arraySize = len(my_list)
    h = Heap()
    
    for _ in range(k):
        h.BuildMinHeap(my_list, arraySize)
        result.append(my_list[0])
        arraySize = arraySize - 1
        #We remove the first and put the last in the first
        # and trickle down or heapify again
        my_list[0] = my_list[arraySize]
    return result


my_list = [9, 4, 7, 1, -2, 6, 5]
result = findKSmallest(my_list, 3)
print(result) # -2, 1, 4
