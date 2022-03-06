import sys
from collections import deque
M,N=map(int,sys.stdin.readline().split())
# 0:익지 않은 토마토 1:익은 토마토 -1:토마토가 들어있지 않은 칸
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            queue.append((i,j))
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==0:
                    board[nx][ny]=board[x][y]+1
                    queue.append((nx,ny))
    return board
result=bfs()
for i in result:
    if 0 in i:
        print(-1)
        exit()
print(max(map(max,result))-1)