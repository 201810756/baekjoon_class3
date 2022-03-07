import sys
from collections import deque
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
board=[[]*M for _ in range(N+1)]
for _ in range(M):
    p1,p2=map(int,sys.stdin.readline().split())
    board[p1].append(p2)
    board[p2].append(p1)
queue=deque()
v=[False]*(N+1)
def bfs(start):
    cnt=0
    queue.append(start)
    v[start]=True
    while queue:
        k=queue.popleft()
        for i in board[k]:
            if v[i]==False:
                queue.append(i)
                v[i]=True
                cnt+=1

    return cnt
print(bfs(1))