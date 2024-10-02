class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapup(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapdown(self, index):
        size = len(self.heap)
        while (2 * index + 1) < size:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            larger_child_index = left_child_index

            if right_child_index < size and self.heap[right_child_index] > self.heap[left_child_index]:
                larger_child_index = right_child_index

            if self.heap[larger_child_index] > self.heap[index]:
                self.heap[index], self.heap[larger_child_index] = self.heap[larger_child_index], self.heap[index]
                index = larger_child_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapup(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        largest = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.heapdown(0)
        return largest

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

max_heap = MaxHeap()

# x = int(input("How many nodes "))
# for i in range(x):
#     max_heap.insert(int(input("Enter node value ")))

# while max_heap.peek() is not None:
#     print("Max Heap:", max_heap)
#     print(f"Max value {max_heap.extract_max()}")
#     print("\n")


while(1):
    x = int(input("1/2 "))
    if x == "1":
        max_heap.insert(int(input("Enter node value ")))
        print("Max Heap:", max_heap.peek())
        print(f"Max value {max_heap.peek().extract_max()}")
        print("\n")
    else: 
        print("Max Heap:", max_heap.peek())
        print(f"Max value {max_heap.peek().extract_max()}")
        print("\n")