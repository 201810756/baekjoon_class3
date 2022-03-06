import sys
from collections import deque
N=int(sys.stdin.readline())
board=[]
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=[[0]*N for _ in range(N)]
queue=deque()
cnt=0
def bfs(x,y):
    queue.append((x,y))
    count[x][y]=cnt
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue

            if board[nx][ny]==board[x][y] and count[nx][ny]==0:
                queue.append((nx,ny))
                count[nx][ny]=1
for i in range(N):
    for j in range(N):
        if count[i][j]==0:
            bfs(i,j)
            cnt+=1
print(cnt,end=' ')
for i in range(N):
    for j in range(N):
        if board[i][j]=='G':
            board[i][j]='R'
count=[[0]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if count[i][j]==0:
            bfs(i,j)
            cnt+=1
print(cnt)