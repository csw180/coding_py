# 프로그래머스 2018 KAKAO BLIND RECRUITMENT [3차] 압축 
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

import string

class WordDict :
    def __init__(self):
        self._word_dict = {x:i for i,x in enumerate(string.ascii_uppercase,start=1)}
        self.last_value = 26
        self._temp_word = ''
        self.index_list = []

    def __str__(self) -> str:
        return f'temp_word={self._temp_word} index_list={self.index_list}'

    def append_char(self, char):
        if  self._temp_word+char in self._word_dict :
            self._temp_word += char
        else :
            self.append(self._temp_word+char)
            self.index_list.append(self._word_dict.get(self._temp_word))
            self._temp_word = char

    def flush(self):
        self.index_list.append(self._word_dict.get(self._temp_word))
        self._temp_word = ''

    def append(self, word):
        self.last_value += 1
        self._word_dict[word] = self.last_value

def solution(msg):
    answer = []
    word_dict = WordDict()
    for c in msg :
        word_dict.append_char(c)
        # print(f'{c} after append : {word_dict}')
    word_dict.flush()
    # print(f'after flush : {word_dict}')
    answer = word_dict.index_list
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))
print(solution('A'))
