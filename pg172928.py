def movable(park,r,c,op,n) :
    movable = True
    mr, mc  = r, c
    if  op == 'E' :
        if c+n >= len(park[r]) : 
            movable  = False
        else :
            for i in range(1,n+1) :
                if  park[r][c+i] == 'X' :
                    movable = False
        if movable :  mc += n

    if  op == 'W' :
        if c-n < 0 :
            movable = False
        else :
            for i in range(1,n+1) :
                if park[r][c-i] =='X' :
                    movable = False
        if movable :   mc -= n

    if  op == 'N' :
        if r-n < 0 :
            movable = False
        else : 
            for i in range(1,n+1) :
                if park[r-i][c] == 'X' :
                    movable = False
        if movable :    mr -= n

    if  op == 'S' :
        if  r+n >= len(park) :
            movable  = False
        else : 
            for i in range(1,n+1) :
                if park[r+i][c] == 'X' :
                    movable = False
        if movable : mr += n

    return movable, mr, mc
    
def solution(park, routes):
    r, c = 0, 0
    for i, p in enumerate(park) :
        if p.find('S') != -1 :
            r, c = i, p.find('S')
            break
    
    for route in routes :
        op, n = route.split()
        able, mr, mc = movable(park,r,c,op,int(n))
        if able :
            r, c = mr, mc

    return [r,c]


print(solution(["SOO","OOO","OOO"],	["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],	["E 2","S 2","W 1"]	))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))