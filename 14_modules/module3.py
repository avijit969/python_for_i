# import module1
# import module2
import module1,module2

import module2 as m2
# result=module1.sum(10,20)
# subs=module1.sub(20,10)
# multi=module2.mul(10,20)
# from module1 import sum,sub
# from module1 import *
from module2 import mul as multiplication , div as division

# result=sum(10,20)
# result2=sub(10,20)
# result3=multiplication(10,20)
# result4=division(10,2)
# print(result,result2)
# print(result3)
# print(result4)

from module1 import sum

# print(__name__)
print(sum(10,20))