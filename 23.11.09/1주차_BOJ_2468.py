from collections import deque
N = int(input())
A = []
max_height = 0
for i in range (0,N):
    a = list(map(int,input().split()))
    max_height = max(max(a),max_height)
    A.append(a)

def move(x,y,h):
    dxdy = [[1,0],[-1,0],[0,1],[0,-1]]
    z = []
    for i in range (0,4):
        a = x + dxdy[i][0]
        b = y + dxdy[i][1]
        if 0 <= a < N and 0 <= b < N and A[a][b] > h:
            z.append([a,b])
    return z
ans = []

for height in range (0,max_height):
    cnt = 0
    visited = [[False for _ in range (0,N)] for _ in range (0,N)]
    for i in range (0,N):
        for j in range (0,N): 
            if A[i][j] > height and visited[i][j] == False:
                visited[i][j] = True
                a = deque([])
                a.appendleft([i,j])
                while a:
                    c = a.popleft()
                    visited[c[0]][c[1]] = True
                    b = move(c[0],c[1],height)
                    for area in b:
                        if visited[area[0]][area[1]] == False:
                            visited[area[0]][area[1]] = True
                            a.appendleft([area[0],area[1]])
                cnt += 1
    ans.append(cnt)      
print(max(ans))



