import sys
input = sys.stdin.readline

def expand_digit(a,b) :
    str_a = str(a)
    str_b = str(b)
    length = max(len(str_a), len(str_b))
    return str_a.zfill(length), str_b.zfill(length)

a,b = map(int,input().split())
str_a, str_b = expand_digit(a,b)
length  = len(str_a)

under_bound_check = True
upper_bound_check = True
cases = 1
for i in range(length) :
    count = 0
    for fs in ['4','7'] :
        if str_a[i] <= fs <= str_b[i] :
            count += 1
            if  under_bound_check and str_a[i] == fs :
                under_bound_check = True
            if  upper_bound_check and str_b[i] == sf :
                upper_bound_check = True


    else :
        str_a = str_a[:i] + '4' + str_a[i+1:]
        break

1 * 2 * 2 * 2 * 2 * 2 * 2

11 32
