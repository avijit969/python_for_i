# from threading import *   
# import time
# l=Lock()
   
# def wish(name):
#     l.acquire()
#     for i in range(10):   
#         print("Good Evening:",end='')   
#         time.sleep(2)   
#         print(name)
#     l.release()  
    
 
# t1=Thread(target=wish,args=("isha",))   
# t2=Thread(target=wish,args=("avi",))   
# t1.start()   
# t2.start()

from threading import *   
l=RLock()   
# print("Main Thread trying to acquire Lock")   
# l.acquire()   
# print("Main Thread trying to acquire Lock Again")   
# l.acquire()

# from threading import *   
# import time   
# l=RLock()   
# def factorial(n):   
#     l.acquire()   
#     if n==0:   
#         result=1   
#     else:   
#         result=n*factorial(n-1)   
#     l.release()
#     return result

# def results(n):
#     time.sleep(2)  
#     print("The Factorial of",n,"is:",factorial(n))   
   
# t1=Thread(target=results,args=(5,))   
# t2=Thread(target=results,args=(9,))   
# t1.start()   
# t2.start()  

# using semaphore
from threading import *   
import time   
s=Semaphore(3)   

def wish(name):
    s.acquire()
    for i in range(3):   
        print("Good Evening:",end='')   
        time.sleep(1)   
        print(name)
    s.release()  
    
 
t1=Thread(target=wish,args=("isha",))   
t2=Thread(target=wish,args=("avi",))   
t3=Thread(target=wish,args=("sugyani",))   
t4=Thread(target=wish,args=("jit",))   
t5=Thread(target=wish,args=("ram",))   
t6=Thread(target=wish,args=("sita",))   
t1.start()   
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
