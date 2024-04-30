class InvalidAge(Exception):
    def __init__(self,msg):
        self.msg=msg
    
age =int(input("Enter your age: "))
try:
    if age < 18:
        raise InvalidAge("your age is not eligible")
    else:
        print("You are eligible to vote")    
except InvalidAge as e:
    print(e)
