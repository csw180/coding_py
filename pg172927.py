def  fatigue(minerals) :
    result = [0,0,0]
    fatgs = {'diamond':(1,5,25),'iron':(1,1,5),'stone':(1,1,1)}
    for mineral in minerals :
        result[0] += fatgs[mineral][0]
        result[1] += fatgs[mineral][1]
        result[2] += fatgs[mineral][2]
    return result

def solution(picks, minerals):
    fatigues = []
    for i in range(0,min([len(minerals),sum(picks)*5]),5) :
        fatigues.append(fatigue(minerals[i:i+5]))
    fatigues_sorted = sorted(fatigues,key=lambda x : (x[2],x[1],x[0]),reverse=True)
    tools  = []
    for i, pick in enumerate(picks) :
        for _ in range(pick) :
            tools.append(i)   
    sum_fatigues = 0
    for tool in tools :
        try :
            sum_fatigues += fatigues_sorted.pop(0)[tool]
        except IndexError :
            break
    return sum_fatigues

print(solution([1, 3, 2],["iron", "diamond", "iron", "stone","diamond", "diamond", "diamond", "iron"]))
print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution([1, 1, 0],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone","iron", "iron", "diamond","diamond"]))
print(solution([0, 1, 0],['stone', 'stone', 'stone', 'stone', 'stone']))

