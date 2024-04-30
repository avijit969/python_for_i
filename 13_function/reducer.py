from functools import reduce
list1=[10,20,30,40]
all_sum=reduce(lambda x,y:x*y,list1)
print(all_sum)
