def MinHeap(value,heap):
    heap.append(value)
    index = len(heap) - 1

    while index > 0 and heap[(index - 1)//2] > heap[index]:
        heap[(index - 1)//2] , heap[index] = heap[index] , heap[(index - 1)//2]
        index = (index - 1)//2

heap = []
list = [1,5,25,8,56,4,25,3]
for value in list:
    MinHeap(value,heap)
    print(f"{value} added and heap is {heap}")
