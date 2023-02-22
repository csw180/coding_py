
ss=  [-1,1,3,-2,2]
plus_a = []
minus_a = []
for s in ss:
    if  s>0 :
        plus_a.append(s)
    else :
        minus_a.append(s)
result = minus_a + plus_a
print(result)
