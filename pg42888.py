# 프로그래머스 오픈채팅방 2019 kakao blind recruitment
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def make_message(commands, user) :
    result = []
    for command in commands :
        if command[0]=='Enter' :
            result.append(user[command[1]]+"님이 들어왔습니다.")
        elif command[0]=='Leave' :
            result.append(user[command[1]]+"님이 나갔습니다.")
    return result

def solution(records):
    user = dict()
    commands = []
    for record in records :
        command, *userinfo = record.split()
        if  command=='Change' :
            user[userinfo[0]] = userinfo[1]
        else :
            commands.append((command,userinfo[0]))
            if  command=='Enter' :
                user[userinfo[0]] = userinfo[1]
    return make_message(commands, user)

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))