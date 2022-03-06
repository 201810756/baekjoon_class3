"""
이것이 코딩테스트다 p.152 미로탈출 문제와 유사
"""
import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
# 1:이동가능 / 0:이동불가
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if board[nx][ny]==0:
                continue
            if board[nx][ny]==1:
                board[nx][ny]=board[x][y]+1
                queue.append((nx,ny))
    return board[N-1][M-1]
print(bfs(0,0))
