with open("test_2.txt", "w") as f:
    # text_size = 2
    # f_content = f.read(text_size)
    
    #print(f.tell())
   
    # while len(f_content) > 0:
    #     print(f_content,end='#')
    #     f_content = f.read(text_size)
    f.write("BaBU")
    f.seek(4)
    f.write("HASAN")

with open("test_2.txt", "r") as f_r:
    print(f_r.read())