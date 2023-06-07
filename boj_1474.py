# 백준 밑줄:1474 https://www.acmicpc.net/problem/1474

import sys

input = sys.stdin.readline

N, M  = map(int, input().split())
words = []
words_length = 0
for i in range(N) :
    word  = input().rstrip()
    words_length += len(word)
    words.append((word,i))

_common, _optional = divmod(M - words_length,N-1)
# _common 공통적으로 각 단어앞에 붙여야 하는 '_' 의 갯수
# 공통적으로 단어 앞에 '_' 를 붙여 길이 M 을 만들수 없을때 추가로 '_'를 더 붙어야 하는 단어의 갯수

onemore = [ x[1] for x in sorted(words[1:],key=lambda x: x[1] - N if x[0][0].islower() else N- x[1])[:_optional]]
# 소문자로 시작하는 단어는 먼저나오는 단어부터 '_' 를 추가시켜나가고 
# 대문자로 시작하는 단어는 맨나중에 나오는 단어부터 '_' 를 추가시켜나가야 한다.

optional_count = 0
result = words[0][0]
for i in range(1,N) :
    result += ('_' * _common) + ('_' if i in onemore else '') + words[i][0]
    optional_count += 1

print(f'{result}')