def solution(cards1, cards2, goal):
    for v in goal :
        if  cards1 and v == cards1[0] :
            cards1.pop(0)
        elif cards2 and v== cards2[0] :
            cards2.pop(0)
        else :
            return 'No'
    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))