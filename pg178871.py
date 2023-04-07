# 달라기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    d2key = {v:i for i,v in enumerate(players)}

    for call in callings :
        key = d2key[call]
        d2key[players[key-1]] = key
        d2key[call] = key - 1
        players[key-1] , players[key] = players[key], players[key-1]

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],	["kai", "kai", "mine", "mine"]	))