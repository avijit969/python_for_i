from threading import *   
print(current_thread().isDaemon()) #False   
print(current_thread().daemon) #False   


def wish():
    print("i am demon thread")
    
t1=Thread(target=wish)
t1.setDaemon(True)
t1.start()
print(t1.isDaemon())

