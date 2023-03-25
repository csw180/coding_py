import sys
c1 = sys.stdin.readline().strip()
c2 = sys.stdin.readline().strip()
c3 = sys.stdin.readline().strip()

ary = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
idx = str(ary.index(c1)) + str(ary.index(c2))
nidx = int(idx) * (10 ** ary.index(c3))
print(nidx)

