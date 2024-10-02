class Maxheap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [0]*self.capacity

    def getLeftChildIndex(self, index):
        return 2*(index)+1
    
    def getRightChildIndex(self, index):
        return 2*(index)+2
    
    def getParentIndex(self , index):
        return (index - 1)//2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def LeftChild(self, index):
        return self.array[self.getLeftChildIndex(index)]
    
    def RightChild(self, index):
        return self.array[self.getRightChildIndex(index)]
    
    def Parent(self, index):
        return self.array[self.getParentIndex(index)]
    
    def isFull(self):
        return self.capacity == self.size
    
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
            
        data = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.reheapdown()

        return data

    def reheapdown(self):

        index = 0
        while(self.hasLeftChild(index)):
            largerChild = self.getLeftChildIndex(index)
            
            if(self.hasRightChild(index) and self.RightChild(index)>self.LeftChild(index)):
                largerChild = self.getRightChildIndex(index)
            
            if self.array[index] < self.array[largerChild]:
                self.array[index], self.array[largerChild] = self.array[largerChild], self.array[index]
            
            index = largerChild
        
    def enqueue(self, data):
        if self.isFull():
            return "Full"

        self.array[self.size] = data
        self.size += 1
        self.reheapup()

    def reheapup(self):
        index = self.size - 1
        while(self.hasParent(index) and self.Parent(index) < self.array[index]):
            self.array[self.getParentIndex(index)], self.array[index] = self.array[index], self.array[self.getParentIndex(index)]
        
            index = self.getParentIndex(index)

h = Maxheap(10)            
h.enqueue(9)
h.enqueue(77)
h.enqueue(61)
h.enqueue(12)
h.enqueue(43)
h.enqueue(88)
h.enqueue(25)
h.enqueue(43)
print(h.array)