# name="ram"
# print(id(name))
# name="rama"
# print(id(name))

# name=["ram"]
# print(id(name))
# name[0]="rama"
# print(id(name))

# list1=["rama",0,True,2.5,True,["avi"]]
# list1.append("sita")
# # list1.remove(True)
# print(list1)
# print(list1[7])

# list2=[1,2,3,4]
# list3=[5,6,7,9]
# list4=list2+list3
# print(list2*2)
# print(list2)

# # len()
# print(len(list3))
list1=[]
print(type(list1))
list1.append("rama")
# list1.append("avi")
# list1.append(1)

list1.extend([1,True,"avi"])
# for element in (1,True,"avi"):
#     list1.append(element)

list1.insert(4,[False])

list1.pop(3)

# list1.clear()
list1.append("rama")
# print(list1.index("rama"))
# print(list1)
# print(list1.count("rama"))

numbers=[2,5,8,1,10]
# numbers.sort() # as list is mutable so it will change the original list i.e. numbers . so after sorting we print or access the original string because sort() does not return anything it changes the original list
# numbers.sort(reverse=True)
numbers.reverse()
numbers2=numbers2.copy()
print(numbers2)
print(len(numbers2))
print(max(numbers2))
print(min(numbers2))
