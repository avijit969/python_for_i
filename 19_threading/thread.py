import time
from threading import *

def square(numbers):
    for num in numbers:
        time.sleep(1)
        print(f"square of {num} is {num*num}")
    

def double(numbers):
    for num in numbers:
        time.sleep(1)
        print(f"double of {num} is {num*2}")


numbers=[1,2,3,4]

staring_time=time.time()
# square(numbers)
# double(numbers)
t1=Thread(target=square,args=(numbers,))
t2=Thread(target=double,args=(numbers,))
t3=Thread(target=double,args=(numbers,))
t1.start()
t2.start()

total_time=time.time()-staring_time
print("total time",total_time)