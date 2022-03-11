import sys
from collections import deque
N=int(sys.stdin.readline())
state=[]
for _ in range(N):
    state.append(list(map(int,sys.stdin.readline().split())))
# 0:빈칸 / 1,2,3,4,5,6:물고기 크기 / 9:상어 위치
# 초기 아기 상어 : 2 (1초에 상하좌우 한칸 이동)
# 아기 상어는 자기보다 큰 물고기가 있는 칸은 못 지나감. 자신보다 작은 물고기는 먹을 수 있음(같아도 못 먹음)
x=0
y=0
shark_age=2
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,age):
    visited=[[False]*N for _ in range(N)]
    dist=[[0]*N for _ in range(N)]
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    eatable=[]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if state[nx][ny]<=age:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    dist[nx][ny]=dist[x][y]+1
                    if 1<=state[nx][ny]<age:
                        eatable.append((nx,ny,dist[nx][ny]))
    return eatable
for i in range(N):
    for j in range(N):
        if state[i][j]==9:
            x=i
            y=j
            state[i][j]=0
result=0
eaten=0
while True:
    fish=bfs(x,y,shark_age)
    fish.sort(key=lambda k:(-k[2],-k[0],-k[1]))
    if len(fish)==0:
        break
    else:
        nx,ny,dist=fish.pop()
        state[nx][ny] = 0
        result+=dist
        eaten+=1
        if eaten==shark_age:
            shark_age+=1
            eaten=0
        x=nx
        y=ny
print(result)
