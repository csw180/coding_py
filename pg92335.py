import re

def isprime(n:int)-> bool :
    sqrt_value = n**(1/2) #n 까지 다 나눠볼필요없이 루트n 까지만 나눠보면된다. 루트n보다 큰수에는 소수가 발생하지 않는다.
    if n==1 : return False
    for i  in range(2,int(sqrt_value)+1) :
        if n%i == 0 : return False
    return True

def baseN(base10: int, n: int) -> str:
    result = ''
    while base10 :
        result += str(base10 % n)
        base10 //= n
    return result[::-1]

def solution(n, k):
    answer = 0
    n_basek = baseN(n,k)
    p = re.compile(r'(^[1-9]+0)|(0[1-9]+$)|(0[1-9]+0)|(^[1-9]+$)')

    position = 0 
    founds = []
    while True : 
        matched =  p.search(n_basek, position)
        if matched is None : break
        position = matched.span()[0] + 1
        founds.append(int(matched.group().strip('0')))

    for found  in founds :
        if  isprime(found) :
            answer += 1

    return answer



# print(solution(437674,3))
print(solution(110011,10))
# print(solution(1,3))



# n 보다 작은 소수 구하기 (에라토스테네스의 체)
# 소수를 모두 구할때는 이거 쓰면되지만 n 의 소수여부만 필요한거면 isprime 쓰는걸로
# def prime_list(n) :
#     primes = [True]*n
#     for i  in range(2,int(n**0.5)+1) :
#         if  primes[i] == True :
#             for j in range(i*2,n,i) :
#                 primes[j] = False
#     return  [i for i,v in enumerate(primes) if v and i > 1 ]

