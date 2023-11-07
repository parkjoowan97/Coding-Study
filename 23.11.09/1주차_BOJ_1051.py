#BOJ 1051 숫자정사각형
N,M = map(int,input().split())
A = []
for i in range (0,N):
    a = list(str(input()))
    A.append(a)
ans = []
for i in range (1,N+1):
    for x in range (0,N-i+1):
        for y in range (0,M-i+1):
            B = list(set([A[x][y],A[x][y+i-1],A[x+i-1][y],A[x+i-1][y+i-1]]))
            if len(B) == 1:
                ans.append(i*i)
            else:
                continue
print(max(ans))
