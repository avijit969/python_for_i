class Parent:
    def land(self):
        print("i have land")
    def gold(self):
        print("i have gold")
    def money(self):
        print("i have money")

# class Child:
#     def land(self):
#         print("i have land")
#     def gold(self):
#         print("i have gold")
#     def money(self):
#         print("i have money")
# c1=Child()
# c1.gold()
# c1.land()
# c1.money()

class Child(Parent):
    def house(self):
        print("i have house")

c1=Child()
c1.gold()
c1.land()
c1.money()

