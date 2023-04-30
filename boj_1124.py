import sys
from math import sqrt

# 에라토스테네스의 체 (소수리스트 작성)
# 소수리트를 리턴하는 대신 소수를 dict 형식으로 반환토록 수정
# 리스트롤 반환했을경우
#     if number in sieve :count += 1
# 보다 dict 형식으로 반환한 경우
#     if sieve.get(number) :count += 1
# 가 처리속도가 빠름

def sieve_of_eratos(n):
    sieve = [True] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    # return [i for i in range(2, n + 1) if sieve[i] == True]
    return {i:True for i in range(2, n + 1) if sieve[i] == True}

# 소인수분해(factorization) 결과 항의 갯수 리턴
def factorization(n,primt_list):
    count = 0
    for i in primt_list:
        if i > n : break
        while n % i == 0:
            n //= i
            count += 1
    return count

a, b = map(int,sys.stdin.readline().rstrip().split());
sieve = sieve_of_eratos(b)
count = 0
for s in range(a,b+1):
    number = factorization(s,sieve.keys())
    if sieve.get(number) :count += 1
print(count)