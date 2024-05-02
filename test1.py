string=input()
output=""
for char in string:
    if char.isalpha():
        output+=char
        previous=char
    else:
        output+=chr(ord(previous)+int(char))
print(output)
