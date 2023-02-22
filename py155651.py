
class Room :
    def __init__(self, book) :
        self.l = book  # ('1500','1700')

    def is_passible(self, book) :
        if  self.l[0] <= book[0] < self.l[1] :
            return False
        else :
            return True

    def update(self, book) :
        self.l = (min(self.l[0],book[0]), max(self.l[1],book[1]))

    def __str__(self) :
        return f'{self.l[0]}:{self.l[1]}'
    
 
def solution(book_time):
    rooms = []
    for book in sorted(book_time,key=lambda x:x[0]):
        s1,b1 = tuple(map(int,book[0].split(':')))
        s2,b2 = tuple(map(int,book[1].split(':')))
        b2+=10
        if b2 >= 60 :
            s2+=1
            b2-=60
        newbook =( str(s1).zfill(2) + str(b1).zfill(2), str(s2).zfill(2) + str(b2).zfill(2))

        need_newroom = True
        for room in rooms:
            if room.is_passible(newbook) :
                room.update(newbook)
                need_newroom = False
                break   
        if need_newroom :
            rooms.append(Room(newbook))

    answer = len(rooms)
    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))

