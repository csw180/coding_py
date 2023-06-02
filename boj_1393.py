# 백준 음하철도구구팔:1393  https://www.acmicpc.net/problem/1393

import sys
import math

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def distance(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

xs, ys = map(int,sys.stdin.readline().split())
x,y,dx,dy  = map(int,sys.stdin.readline().split())
gcd_ = gcd(dx,dy)   
dx //= gcd_
dy //= gcd_

while ( distance(x,y,xs,ys) >= distance(x+dx,y+dy,xs,ys) ) :
    x += dx
    y += dy

print(x,y)
