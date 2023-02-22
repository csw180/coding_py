def solution(id_pw, db):
    pw_dict = {}
    for d in db :
        pw_dict[d[0]] = d[1]
    if id_pw[0] not in pw_dict :
        return 'fail'
    elif id_pw[0] in pw_dict  and pw_dict[id_pw[0]]!= id_pw[1] :
        return "wrong pw"
    else :
        return 'login'        
    

print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))