from typing import *
from math import ceil

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        orders =[i for i in range(numRows)] 
        orders += list(reversed(orders))[1:-1]
        orders = orders * ceil(len(s)/len(orders))
        orders = orders[:len(s)]

        q_list = []
        for i in range(numRows) :
            q_list.append(list())
        
        orders_idx = 0
        for  v in s :
            q_list[orders[orders_idx]].append(v)
            orders_idx +=1
        # print(q_list)

        for v in q_list :
            while(v) : answer.append(v.pop(0))

        return ''.join(answer)

o  = Solution()
print(o.convert("PAYPALISHIRING",4))
# print(o.convert("A",1))

# 1 2 3 2
# k+ k-2 = n

# k = (n + 2) //2

# 1 2 3 4 3 2

# 1 2 3 4 5 4 3 2

        # orders =[i for i in range(((n+2)//2)+1)] 
