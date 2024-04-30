numbers=[1,2,3,4,5,6,7,8,9,10]

# def greater(num):
#     return num>5

# num=filter(greater,numbers)
num=filter(lambda num:num>5,numbers)
print(list(num))

# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# even_num=filter(even,numbers)
even_num=filter(lambda num:num%2==0,numbers)
odd_num=filter(lambda num:num%2!=0,numbers)

print(list(even_num))
print(list(odd_num))
        
