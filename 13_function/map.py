numbers=(1,2,3,4,5)
# numbers_with_5Added=[]
# for num in numbers:
#     numbers_with_5Added.append(num+5)

# print(numbers_with_5Added)

# def add_five(num):
#     return num+5

# numbers_with_5Added=map(add_five,numbers)
numbers_with_5Added=map(lambda num:num+5,numbers)

print(list(numbers_with_5Added))


