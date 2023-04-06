def solution(name, yearning, photo):
    answer = []
    d = dict.fromkeys(name,0)
    for i in range(len(name)) :
        d[name[i]] = yearning[i]
    for ps in photo :
        score = 0
        for p in ps :
            if  d.get(p) is not None :
                score += d[p]
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))