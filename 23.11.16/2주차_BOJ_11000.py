import sys
import heapq
input = sys.stdin.readline
N = int(input())
A = []
for i in range (0,N):
    a = list(map(int,input().split()))
    A.append(a)
A.sort(key = lambda x: x[0])

que = []
heapq.heappush(que,A[0][1])
for i in range (1,N):
    if A[i][0] < que[0]:
        heapq.heappush(que,A[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que,A[i][1])
print(len(que))