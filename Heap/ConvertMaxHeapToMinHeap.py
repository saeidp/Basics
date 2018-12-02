class Heap:
    def maxHeapify(self, heaplist, index, heapSize):
        largest = index
        while(largest < heapSize // 2):
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heapSize and heaplist[left] > heaplist[index]:
                largest = left
            if right < heapSize and heaplist[right] > heaplist[largest]:
                largest = right
            if largest != index:
                heaplist[index],heaplist[largest] = heaplist[largest], heaplist[index]
                index = largest
            else:
                break
   
    def BuildMaxHeap(self, heaplist, heapSize):
        for i in range((heapSize - 1)//2, -1, -1):
            self.maxHeapify(heaplist, i, heapSize)
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
    def BuildMinHeap(self, heaplist, heapSize):
        for i in range((heapSize - 1)//2, -1, -1):
            self.minHeapify(heaplist, i, heapSize)
    
#--------------------------------------------------------------
# Convert Max Heap to Min Heap
# maxHeap = [9,4,7,1,-2,6,5]
# result = [-2,1,5,9,4,6,7]
# In a binary Min-Heap, the parent node has minimum value
# than its children. In the result list, -2 is the root
# of Min-Heap and its left child 1, calculated as, index*2
# and right child 5, calculated as, (index * 2) +1, both have
# greater values.
def convertMax(maxHeap):
    result ="["
    h = Heap()
    h.BuildMinHeap(maxHeap, len(maxHeap))
    for i in range(len(maxHeap)):
        if i == len(maxHeap) - 1:
            result += str(maxHeap[i])
        else:
            result += str(maxHeap[i]) + ","
    result += "]"
    return result

# suppose we already have a max heap then 
maxHeap = [9, 4, 7, 1, -2, 6, 5]
print(convertMax(maxHeap)) # a string of [-2, 1, 5, 9, 4, 6, 7]
