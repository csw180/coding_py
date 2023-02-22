
jail = [0 for i in range(120)]
for n in range(1,120+1) :
    for i in range(n-1,120,n) :
        jail[i] = 1 if jail[i] == 0 else 0

print(jail.count(1))

