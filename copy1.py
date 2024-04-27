with open("file.txt",'r') as file1:
    content=file1.read()
    
with open("file1.txt",'w') as file2:
    file2.write(content)