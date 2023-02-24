def solution(keymap, targets):
    answer = []
    for target in targets :
        indx_list = []
        for c in target :
            indx_list.append(min([key.find(c)+1 if key.find(c) >= 0  else 999 for key in keymap]))
    
        answer.append(sum(indx_list) if max(indx_list) < 999 else -1)
    return answer


# print(solution(["ABACD", "BCEFD"],	["ABCD","AABB"]))
# print(solution(["AA"],		["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]	))
