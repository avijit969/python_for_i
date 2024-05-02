
# from threading import *
# import time
# def table(num):
#     for i in range(1,11):
#         time.sleep(.5)
#         print(f"{num}*{i}={num*i}")
        
# t1=Thread(target=table,args=(5,))
# t2=Thread(target=table,args=(7,))
# t1.start()
# t1.join()
# t2.start()
# t2.join()
#  Creating a Thread without extending Thread class:
from threading import *
import time
class Table:
    def table(self,num):
        for i in range(1,11):
            time.sleep(.5)
            print(f"{num}*{i}={num*i}")
tb=Table()   
t1=Thread(target=tb.table,args=(5,))
t2=Thread(target=tb.table,args=(7,))

t1.setName("Table of 5") # to set the name of the thread
thread_name=t1.getName() # to get the name of the thread
print(thread_name)
t1.start()
print(t1.is_alive())
print(t1.ident)
t1.join() 
t2.start()
print(current_thread().is_alive()) # to check if the thread is alive or not
print(current_thread().ident) # to get the id of the thread
# print(t2.ident)
print("the number activate threads are",active_count()) # to get the number of active threads
print(current_thread().getName()) # to get the name of the current thread
current_thread() # to get the current thread
print(enumerate()) # to get the list of all the active threads


#  Creating a Thread by extending Thread class

# from threading import Thread
# import time

# class MyThread(Thread):
#     def __init__(self, num):
#         super().__init__()
#         self.num = num

#     def run(self):
#         for i in range(1, 11):
#             time.sleep(0.5)
#             print(f"{self.num} * {i} = {self.num * i}")

# t1 = MyThread(5)
# t2 = MyThread(7)
# t1.start()
# t2.start()
