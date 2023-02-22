
# https://school.programmers.co.kr/learn/courses/30/lessons/60060?language=python3
# Trie 문자열 검색 알고리즘..

class Node :
    def __init__(self,value) :
        self.value = value
        self.child = {}
        self.remain = {}
        self.terminal = False

class Trie :
    def __init__(self) :
        self.head = Node(None)
    
    def update(self, string) :
        current = self.head

        for i, s  in enumerate(string) :
            if current.remain.get(len(string)-i) is None :
                current.remain[len(string)-i] = 1
            else : 
                current.remain[len(string)-i] +=1          
            if  current.child.get(s) is None :
                current.child[s] = Node(s)
            current = current.child[s]
          
        current.terminal = True
    
    def search(self, string) :
        current = self.head

        result = ''
        for s in string :
            if  current.child.get(s) is None :
                return result, current.remain
            else :
                current = current.child[s]            
            result += current.value
        return result, current.remain
    
def solution(words, queries) :
    answer = []
    t = Trie()       
    rev_t = Trie()
    for word in words :
        t.update(word)         
        rev_t.update(word[::-1])         

    for v in queries :
        if  v[-1]=='?' :
            result, remain = t.search(v)
        else :
            v = v[::-1]
            result, remain = rev_t.search(v)

        wild_cnt = v.count('?')
        alpha = v.replace('?','')
        # print(f'{v=} {alpha=},{wild_cnt=}')
        # print(f'{v=} {result=},{remain=}')
        # if  alpha == result and remain.get(wild_cnt) is not None:
        if  alpha == result and wild_cnt in remain:
            answer.append(remain[wild_cnt])
        else : 
            answer.append(0)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao",'kaka']
queries = ["fro??", "????o", "fr???", "fro???", "pro?","kaka?","????","?????????"]
print(solution(words, queries))

