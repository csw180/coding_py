# 8. String to Integer (atoi)



class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 0
        if s and s[0] in ['+','-'] :
            if s[0] == '+' :
                sign = 1
            else :
                sign = -1
            s = s[1:]
        else :
            sign = 1
        
        nums = '0'
        for c in s :
            if c.isdigit() :
                nums += c
            else :
                break
        nums = nums.lstrip('0')
        int_nums = (sign * int(nums)) if nums != '' else 0
        if int_nums < -1 * (2**31) :
            int_nums = -1 * (2**31)
        elif int_nums > 2**31 - 1  :
            int_nums = 2**31 - 1

        return int_nums    

        

# print(-1 * 2**31)
# print(Solution().myAtoi('-91283472332'))
print(Solution().myAtoi('-9.2'))
# print(Solution().myAtoi('91283472332'))
# print(Solution().myAtoi('042'))
# print(Solution().myAtoi('   -42'))
# print(Solution().myAtoi('4193 with words'))
# print(Solution().myAtoi('words and 987'))

# print(-1 * 2**31)
# a = -1 * 2**31
# print(a)