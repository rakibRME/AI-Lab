queue = []
front = -1
rear = -1
flag = 0
size = int(input("Enter queue size "))

def enque(x):
    global front, rear, size, flag

    if rear < int(size) - 1 :
        queue.append(x)
        rear += 1
    elif size == 0:
        print("Queue is empty") 
        print(f"Current queue is {queue}") 
        flag = 1  
        print(front)
        print(rear)
    else:
        print("Queue is full") 
        print(f"Current queue is {queue}") 
        flag = 1
        print(front)
        print(rear) 
       

def deque():
    global front, rear, size, flag
    front += 1

s = input("Enter string ")
if len(s):
    front = 0
    if size == 0:
        front = -1
else:
    front = -1
    

for i in range(len(s)):
    if flag == 0:
        enque(s[i])
    else:
        pass

print(f"Current queue is {queue}")
print(front)
print(rear)
print("\n")     

while(1):
    x = input("Press 1 for Enque or Press 2 for Deque\n") 
    if x=="1":
        char = input("Enter character\n")
        enque(char)
        print(f"Current queue is {queue}")
        print(front)
        print(rear)

    else:
        deque()
        print(f"Current queue is {queue}")  
        print(f"Current queue is {queue}")
        print(front)
        print(rear)    
 