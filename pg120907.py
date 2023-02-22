def solution(quiz):
    result=[]
    for q in quiz :
        tokens = q.split("=")
        ops = tokens[0].split(" ")
        if ops[1]== '+' :
            ans = int(ops[0])+int(ops[2])
        else :
            ans = int(ops[0])-int(ops[2])
        if ans == int(tokens[-1]) :
            result.append("O")
        else :
            result.append("X")
    return result

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))