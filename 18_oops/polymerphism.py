# operator overloading

print(10+20)
print("isha"+" das")

# print(2*5)
# print("isha "*5)

class Page:
    def __init__(self,page):
        self.page=page
    def __add__(self,other):
        return self.page+other.page
    
p1=Page(10)
p2=Page(20)

print(p1+p2)


class Test:
    def __init__(self,num):
        self.num=num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __lt__(self,other):
        return self.num<other.num
t1=Test(10)
t2=Test(20)
result=t1<t2
print(result)

