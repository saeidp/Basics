class Heap:
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
#-------------------------------------------------------------
# write a code to find first "k" largest elements using Max-Heap
# my_list = [9,4,7,1,-2,6,5]           k = 3
# Output-> [9,7,6]
def findKLargest(my_list, k):
    result = []
    for i in range(k):
        result.append(0)
    arraySize = len(my_list)
    h = Heap()
    for i in range(k):
        h.BuildMaxHeap(my_list, arraySize)
        result[i] = my_list[0]
        arraySize = arraySize - 1
        my_list[0] = my_list[arraySize]
    return result

my_list = [9, 4, 7, 1, -2, 6, 5]
result = findKLargest(my_list, 3)
print(result) # [9, 7, 6]


