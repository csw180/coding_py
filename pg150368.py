from itertools import product

def solution(users, emoticons):
    answer = []
    case_matric =  list(product([10,20,30,40],repeat=len(emoticons)))
    for tp in case_matric :

        users_sum_list = []
        users_plus_list = []
        for user in users :
            rate_limit, buy_limit = user[0], user[1]
            user_sum = 0
            user_plus = False
            for v in zip(tp,emoticons) :
                if  rate_limit <= v[0] :
                    user_sum += (100-v[0])*v[1] / 100
            if  user_sum >= buy_limit :
                user_plus = True
                user_sum = 0
            
            users_sum_list.append(user_sum)
            users_plus_list.append(user_plus)
        
        # print(f'{tp=} : {users_sum_list=} {users_plus_list=}')
        answer.append((len(list(filter(lambda x:x,users_plus_list))),int(sum(users_sum_list))))

    # print(f'{answer=}')
    answer.sort(key=lambda x : (x[0],x[1]), reverse=True)
    return list(answer[0])

# print(solution([[40, 10000], [25, 10000]],	[7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))