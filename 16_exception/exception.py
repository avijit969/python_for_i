# name = "isha"
# if name == "isha":
#     print("hello isha")
# try:
#     num1=int(input("Enter a number :"))
#     result=20/num1
#     print(result)
# except ZeroDivisionError:
#     print("you can not divide any number with zero")
# except ValueError:#if user enter string instead of number
#     print("please enter a number")
# print("__________________________")
# print("hello isha ")
# print("exception handling")

list1=(10,20,30)
try:
    print(list1[10])
except IndexError as i:
    print("error",i)
else:
    print("no error")
finally:
    print("end")


# try:
#     print(avi)
# except NameError:
#     print("name is not defined")
