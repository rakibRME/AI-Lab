arr = []
curr = -1

def manual_pop():
    global curr
    top_element = arr[curr]
    curr -= 1
    return top_element

def is_palindrome(x):
    global flag,curr,arr
    for i in range(len(x) // 2):
        if curr == -1:
            return False
        else:
            if x[i] != manual_pop():
                return False  
    return True     
       
def push(x, y):
    global curr,arr, flag_count  
    for char in x:
        curr += 1
        arr.append(char)
        # print("PUSH ",char)
        # print("Current ",curr)
    if is_palindrome(x):  
        print(f"{y} is Palindrome")
    else:
        print(f"{y} is not Palindrome")    

with open("input_palindrome.txt","r") as rf:
    #n = int(rf.readline())
    lines = rf.readlines()
    for i in range(int(lines[0])):
        #x = rf.readline()
        #print(f"Line {i+1} is {lines[i+1]}")
        arr.clear()
        curr = -1
        #print(f"Len of {i+1} is",len(lines[i+1].strip()))
        push(lines[i+1].lower().strip(), lines[i+1].strip())
        
        
        
        

                