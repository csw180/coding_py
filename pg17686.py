import re

def comparator_func() :
    count = 0
    def wrapper(filename) :
        nonlocal count
        m = re.match('(^.*?)([0-9]+)(.*$)', filename)
        count += 1
        return m.group(1).lower(), int(m.group(2)), count
    return wrapper

def solution(files):
    comparator = comparator_func()
    answer =sorted(files, key=lambda x: comparator(x))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

