def enQueue(stack1, stack2, x):
    # Move all elements from stack1 to stack2
    while stack1:
        stack2.append(stack1.pop())
    
    # Push the new element onto stack1
    stack1.append(x)
    
    # Move all elements back from stack2 to stack1
    while stack2:
        stack1.append(stack2.pop())

def deQueue(stack1):
    # If stack1 is empty, raise an error
    if not stack1:
        raise IndexError("Queue is empty")
    
    # Pop and return the top element of stack1
    return stack1.pop()

def bfs_traversal(n, adjacency_list):
    # Initialize an empty list to store the BFS traversal
    bfs_result = []
    
    # Initialize two stacks to implement the queue
    stack1 = []
    stack2 = []
    
    # Start BFS from node 0
    enQueue(stack1, stack2, 0)
    
    # Mark node 0 as visited
    visited = set([0])
    
    # Continue BFS until the queue is empty
    while stack1:
        node = deQueue(stack1)
        bfs_result.append(node)
        
        # Visit all neighbors of the current node
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                enQueue(stack1, stack2, neighbor)
                visited.add(neighbor)
    
    return bfs_result

def main():
    # Read input from a file
    with open('input.txt', 'r') as file:
        data = file.read().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        adjacency_list = []
        
        for i in range(n):
            m = int(data[index])
            index += 1
            if m > 0:
                adjacency_list.append(list(map(int, data[index:index + m])))
                index += m
            else:
                adjacency_list.append([])
        
        result = bfs_traversal(n, adjacency_list)
        results.append(result)
    
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
