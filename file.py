# file=open("test.txt",'r')
# text1=file.readline()
# text2=file.readline()
# print(text1)

# file=open("isha.txt",'w')
# file.write("hello python \n")
# file.close()

# with open("isha.txt",'a') as file :
#     print(file.writable())
#     file.write("hello isha \n")
#     file.write("hello avi \n")
    # print(file.mode)
    # print(file.name)
# print(file.closed)

# with open("file.txt",'r') as file1:
#     print(file1.read())

# with open("file.txt",'w') as file1:
#     file1.write("new file")

# with open("file.txt",'w+') as file1:
#     file1.write("new file")
#     print(file1.readable())
#     print(file1.writable())
#     print(file1.readline())
    
# with open("file10.txt",'x') as file2:
#     pass

with open('file.txt','r') as p:
    print(p.read(5))
    print(p.tell())
    p.seek(2)
    print(p.tell())
    print(p.read())
    
