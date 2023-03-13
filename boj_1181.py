import sys

n = int(sys.stdin.readline().strip())
words = set()
for i in range(n) :
    words.add(sys.stdin.readline().strip())

sorted_words = sorted(words,key=lambda x : (len(x),x))
for v in sorted_words :
    print(v)