class Arith:
    def sum(num1,num2):
        return num1+num2

    def sum(num1,num2,num3):
        return num1+num2+num3
result=Arith.sum(10,20,50)
print(result)

# In python method and constructor overload is not possible

class Student:
    def __init__(self,name):
        self.name=name
    def __init__(self,name,age):
        self.name=name
        self.age=age

# s1=Student("ram")
s2=Student("ram",20)
print(s2.name,s2.age)
    