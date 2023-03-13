from collections import Counter

def solution(participant, completion):
    count = Counter(participant)
    for c in completion:
        count[c] -= 1
        if count[c]==0 :
            del count[c]
    return tuple(count.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))