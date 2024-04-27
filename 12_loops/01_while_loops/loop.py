# i=0
# while i<=3:
#     print("hello python !")
#     a=10
#     b=20
#     print(a+b)
#     i+=1

# print("end of while loop")
    
# flag=True
# while flag:
#     try:
#         num=int(input("Enter only number:"))
#     except Exception as e:
#         print("game over")
#         flag=False

num=int(input("Enter number: ")) 
isPrime=True
j=2
while j<num:
    if num%j==0:
        isPrime=False
        break
    j+=1
if isPrime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

    
        
    
    