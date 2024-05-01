# class Student:
#     def set_attribute(self,name,age,rollNo):
#         self.name=name
#         self.age=age
#         self.rollNo=rollNo
#     def read(self):
#         print(f'{self.name} is reading')

# s1=Student()
# s1.set_attribute("sugyani",19,389)
# print(s1.name)
# print(s1.age)
# print(s1.rollNo)
# s1.read()

# s2=Student()
# s2.set_attribute("avi",20,969)
# print(s2.age)
# print(s2.name)
# print(s2.rollNo)
# s2.read()

# using constructor
class Student:
    college_name="GIETU" #class variable
    def __init__(self,name,age,rollNo):
        self.name=name
        self.age=age
        self.rollNo=rollNo
    def read(self):
        print(f'{self.name} is reading')
    def sum(self,num1,num2):
        result=num1+num2
        return result

s1=Student("sugyani",19,389)
print(s1.name)
print(s1.age)
print(s1.rollNo)
s1.read()
print(s1.sum(1,2))

s2=Student("avi",20,969)
print(s2.age)
print(s2.name)
print(s2.rollNo)
s2.read()

print(f"class or common variable is {Student.college_name}")
# print(s1.college_name) #not recommended