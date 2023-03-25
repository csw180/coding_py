def distince(x1,y1,x2,y2) :
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def solution(m, n, startX, startY, balls):
    result = []

    for ballX, ballY in balls :
        testcase = []
        if not (startY == ballY and startX > ballX) :
            testcase.append(distince(startX, startY, -ballX,ballY)) # 왼쪽
        if not (startY == ballY and startX < ballX) :
            testcase.append(distince(-(m-startX), startY, (m-ballX),ballY)) # 오른쪽
        if not (startX == ballX and startY < ballY) :
            testcase.append(distince(startX, -(n-startY), ballX,(n-ballY))) # 위쪽
        if not (startX == ballX and startY > ballY) :            
            testcase.append(distince(startX, startY, ballX,-ballY)) # 아래쪽
        if startX * ballY == startY * ballX  and startX < ballX :
            testcase.append(distince(startX, startY, -ballX,-ballY)) # 좌측아랫모서리
            testcase.append(distince(startX, -(n-startY), -ballX,(n-ballY))) # 좌측윗모서리
        if startX * ballY == startY * ballX  and startX > ballX :
            testcase.append(distince(-(m-startX), startY, (m-ballX),-ballY)) # 우측아랫모서리
            testcase.append(distince(-(m-startX), -(n-startY), (m-ballX),(n-ballY))) # 우측윗모서리

        result.append(min(testcase))

    return result

print(solution(10,10,3,7,[[7, 7], [2, 7], [7, 3]]))
# print(solution(10,10,3,7,[[2, 7]]))
