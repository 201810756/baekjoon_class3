import sys
from collections import deque
M,N,H=map(int,sys.stdin.readline().split())
# M : 가로 / N : 세로 / H : 상자의 수
# 1 : 익은 토마토 / 0 : 익지 않은 토마토 / -1 : 토마토가 들어있지 않음
floor=[]
box=[]
queue=deque()
for i in range(H):
    for j in range(N):
        box.append(list(map(int,sys.stdin.readline().split())))
    floor.append(list(box))
    box.clear()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if floor[i][j][k]==1:
                queue.append((i,j,k))
df=[-1,1,0,0,0,0]
dx=[0,0,-1,1,0,0]
dy=[0,0,0,0,-1,1]
def bfs():
    while queue:
        f,x,y=queue.popleft()
        for i in range(6):
            nf=f+df[i]
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nf<H and 0<=nx<N and 0<=ny<M:
                if floor[nf][nx][ny]==0:
                    floor[nf][nx][ny] = floor[f][x][y] + 1
                    queue.append((nf,nx,ny))
    return floor
result=bfs()
cnt=0
for i in result:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
        cnt=max(cnt,max(j))
print(cnt-1)
