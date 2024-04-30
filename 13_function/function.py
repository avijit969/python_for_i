# length=3
# width=7
# area=length*width
# print("Area of rectangle is" ,area)

# length=4
# width=6
# area=length*width
# print("Area of another rectangle is ",area)
name="isha"
def area_of_rectangle(length,width):
    """this function is use for finding the area of rectangle
    length:rec length
    width :rec width"""
    area=length*width
    print("Area of rectangle is {}".format(area))

# call
# area_of_rectangle(3,7)
# area_of_rectangle(4,6)
# area_of_rectangle(3,6)
# area_of_rectangle(7,0)

# print("hello")
# print(id(area_of_rectangle))
# print(area_of_rectangle.__doc__)
# help(area_of_rectangle)

def wish(name): # function definition argument
    print(f"hello {name}")
    
# wish("isha") # function call parameter
# wish("avi")

def square(num):
    sq=num*num
    print(f"square is {sq}")
    return sq
    print("isha")
# result=square(10) 
# print(result)


# multiple value return in function 

def sum_sub(num1,num2):
    """this function is use for both addition and subtraction"""
    sum=num1+num2
    sub=num1-num2
    return sum,sub,"isha"

# call function sum_sub()
print(type(sum_sub(20,30))) #<class 'tuple'>
add,diff,name=sum_sub(20,30) #(50 ,-10,"isha")
print(add,diff,name)

def cal(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return add,sub,mul,div

values=cal(9,7) #(16,2,63,1.25)
for value in values:
    print(value)

# positional arguments
def sub(num1,num3):
    return num1-num3

print(sub(20,10))

# keyword arguments
def sub(num1,num2):
    return num1-num2

print(sub(num2=20,num1=10))

# default arguments
def add(num1,num2=20):
    return num1+num2

print(add(10))
print(add(10,40))

def wish(name="student"):
    print(f"good morning {name}")
    
wish()
wish("isha")

# variable length argument
def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

print(add(10,20,17,27,23))

def mark_display(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

mark_display(isha=100,avi=20,sugyani=102,jit=25)

# global variable v/s local variable

name="isha" # global variable
def display():
    global name1
    name1="avi" # local variable
    # print(name1)

def wish():
    print(name)
    print(name1)
    
def modify_global_variable(): # to change global variable i.e.name from isha to avi we have to use global keyword
    global name
    name="avi"

modify_global_variable()
# display()
# wish()
print(name)
