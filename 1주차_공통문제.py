#풀이 1 (Yellow 활용)
import math
def solution1(brown, yellow):
    a = brown + yellow #전체 타일 갯수 a
    for i in range (1,int(math.sqrt(a))+1): #a = i * (a//i) = i * b (i <= b)
        if a % i == 0:
            b = a // i 
            if (i - 2) * (b - 2) == yellow: #yellow = (i-2) * (b-2)
                answer = [b,i]
                return answer

#풀이 2 (Brown 활용)
def solution2(brown,yellow):
    for i in range (1,int(math.sqrt(yellow))+1): #yellow = i * (yellow//i) = i * b (i <= b)
        if yellow % i == 0:
            b = yellow // i 
            if (i + 2) * (b + 2) == brown + yellow: #brown + yellow = (i+2) * (b+2)
                answer = [b+2,i+2]
                return answer
brown,yellow = map(int,input().split())
print(solution1(brown,yellow))
print(solution2(brown,yellow))