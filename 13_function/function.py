# length=3
# width=7
# area=length*width
# print("Area of rectangle is" ,area)

# length=4
# width=6
# area=length*width
# print("Area of another rectangle is ",area)

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
result=square(10) 
print(result)

