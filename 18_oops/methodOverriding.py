class Parent:
    def __init__(self,name):
        self.name=name
    def izzat(self):
        print("i have more izzat")
    
class Child(Parent):
    def izzat(self):
        super().izzat()
        print("izzat pani me gei chhapak")

p=Parent("ram")
c1=Child("isha")
# print(c1.name)
c1.izzat()
