import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
board=[0]*101
cnt=[100]*101 # 횟수 리스트
for _ in range(N): # 사다리의 정보
    x,y=map(int,sys.stdin.readline().split()) # x->y 이동
    board[x]=y
for _ in range(M): # 뱀의 정보
    u,v=map(int,sys.stdin.readline().split()) # u->v 이동
    board[u]=v
queue=deque()
v=[False]*101 # 방문 정보 저장
def bfs(start):
    queue.append(start)
    v[start]=True
    cnt[start]=0
    while queue:
        start=queue.popleft()
        for i in range(1,7): # 주사위 돌리기
            nx=start+i
            if 1<=nx<=100:
                if board[nx]!=0: # 만약 사다리 또는 뱀이 있다면 바로 이동 시켜버리기
                    nx=board[nx]
                if not v[nx]: # 아직 방문하지 않은 칸이라면
                    queue.append(nx) # queue에 추가
                    v[nx]=True # 방문 처리
                    cnt[nx]=min(cnt[start]+1,cnt[nx]) # 최소 횟수 저장
bfs(1)
print(cnt[-1]) # 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값

