
#초기 2차원 리스트 설정
N = int(input())
A = []
for i in range (0,N):
    a = list(map(int,input().split()))
    A.append(a)

boundary = []
for d in range (2,N+1): #d1 + d2 = d
    for d1 in range (1,d):
        d2 = d - d1
        boundary.append([d1,d2])
print(boundary)
ans = []
for c in boundary:
    d1,d2 = c[0],c[1]
    d = d1 + d2
    for x in range (0,N - d):
        for y in range (d1,N - d2):  
            for a in range (0,N):
                for b in range (0,N):
                    sum1,sum2,sum3,sum4,sum5 = 0,0,0,0,0               
                    if 0 <= a < x + d1 -1 and 0 <= b < y:
                        sum1 += A[a][b]
                    elif 0 <= a < x + d2 and y <= b < N:
                        sum2 += A[a][b]
                    elif x + d1 -1 <= a < N and 0 <= b < y-d-1:
                        sum3 += A[a][b]
                    elif x + d2 <= a < N and y-d <= b < N:
                        sum4 += A[a][b]
                    else:
                        sum5 += A[a][b]
                    m = max(sum1,sum2,sum3,sum4,sum5)
                    n = min(sum1,sum2,sum3,sum4,sum5)
                    print(m,n)
                    ans.append(m-n)
