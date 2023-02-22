import math

def getelap(iin, out) :
    s1,m1 = map(int,iin.split(':'))
    s2,m2 = map(int,out.split(':'))
    elaps = (s2*60+m2) - (s1*60+m1)
    return elaps

def getfee(fees, elap) :
    total  = 0
    base_time, base_fees, per_time, per_fees = fees[0], fees[1], fees[2], fees[3]

    if  elap <= base_time :
        total = base_fees
    else :
        total = base_fees
        elap -= base_time
        total += math.ceil(elap/per_time) * per_fees
    return total

def solution(fees, records):
    cars = {}
    for  record in records :
        splited = record.split(' ')
        if splited[1] not in cars :
            cars[splited[1]] = [splited[0]]
        else :
            tmplist = cars[splited[1]]
            tmplist.append(splited[0])
    # print(f'{cars=}')
    for k, v in cars.items() :
        elaps = sum([ getelap(v[i], v[i+1] if i+1<len(v) else '23:59') for i in range(0,len(v),2) ])
        cars[k] = getfee(fees, elaps)
    # print(f'{cars=}')

    return list(map(lambda x : x[1],sorted(cars.items())))

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]
print(solution(fees,records))