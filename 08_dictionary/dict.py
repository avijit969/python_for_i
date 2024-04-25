# dict1={}
# print(type(dict1))

student={
    "name":"isha",
    "age":19,
    "roll_no":389,
    "exam_marks":[90,80,95],
    "percentage":95.55,
    1:"avi", # key most be only number and string but values are any datatype (objects)
    2:"avi"
}
# print(f"student name is {student["name"]} and her age is {student['age']}")
# adding or update
# student["name"]="sita"
# # student.update({"mob":82491257})
# student.setdefault("mob",8657467)
# print(student)
# # remove
# # student.pop("age")
# print(student.popitem())
# print(student)

# print(student["name1"]) # key error
# print(student.get("name1")) # none

# print(list(student.keys()))
# print(student.values())
# print(tuple(student.items()))

user={
    "name":"isha",
    "age":19,
}
# user.clear()
user1=user.copy()
size=len(user1)
print(size)
print(user)
print(user1)