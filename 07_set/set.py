# set1={1,2,"ram","sita",2.45,"ram","ram","sita"}
# print(set1)

# # empty set
# set1=set() #{,}
# print(type(set1))

# # set
# set1.add("sita")
# set1.update(("sita","ram",True,1,10.4))

# # remove
# set1.remove("sita")
# set1.discard("ram")
# removed_value=set1.pop()
# print(removed_value)
# print(set1)


# # set operation
# set1={1,2,3,4,5,6,7,8,9,10}
# set2={8,9,10,11,13}

# #union
# set3=set1.union(set2)
# print(set3)

# # intersection
# newSet=set1.intersection(set2)
# print(newSet)

# # difference
# newSet=set1.difference(set2)
# print(newSet)
# newSet=set2.difference(set1)
# print(newSet)

# # symmetric difference
# newSet=set1.symmetric_difference(set2)
# print(newSet)

set1={1,2,3,4,5,6,7,8}
set2={1,2}
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

set2.clear()
set4=set1.copy()
print(set4)
print(set2)

