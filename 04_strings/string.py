name ='isha'
name="isha"
name='''isha 
das
avi
'''
# print(name)

# indexing
str1="avijit"
print(str1[5])

str1="isha"
print(str1[:2])
print(str1[2:])
name=str1[:]

# negative slicing 
name="isha das isha"
print(name[-4:])
print(name[::-2])

capital=name.capitalize()
print(capital)
print(name.lower())
print(name.upper())
print(name.title())

print(name.count('isha'))
print(name.index('x')) # if not present then error ValueError: substring not found 
print(name.find("d")) # if not present then -1

# Check Methods:
print(name.startswith("x")) # false
print(name.endswith("isha")) # true
alp='12aa' # alpha numeric value contains only characters and numbers not space 
print(alp.isalnum())
alp="abcd"
print(alp.isalpha())
name=' '
print(name.isspace())

name = 'isha das'
replaced_name=name.replace('isha',"avi")
print(id(name),id(replaced_name))
print(replaced_name)

name='  isha  '
print(name.strip())
print(name.lstrip())
print(name.rstrip())
str1=""
print(str1.join(("avi"," isha")))

str2='isha_avi'
name1,name2=str2.split('_')
print(name1,name2)
name1,name2=['isha','avi']

print(str2.partition(' '))