"""
시간초과 결과가 계속 떠서 결국 구글링
방문리스트에 방문 표시를 하고 덱에서 꺼내느냐 vs 덱에서 꺼낸 후에 방문리스트에 방문 표시를 하느냐
이 두 코드의 차이점 때문에 계속 시간초과가 발생하였고
그것도 모르고 이것 저것 시도하다가 짜증만 이빠이
덱에서 꺼낸 후에 방문리스트에 방문 표시를 하게 되면
덱에 중복적으로 노드가 들어갈 수 있음
따라서 방문표시를 해놓고 덱에 넣어주어야 중복을 방지
"""
import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
board=[[]*M for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    board[u].append(v)
    board[v].append(u)
V=[False]*(N+1)  # 방문 노드 저장
queue=deque()
cnt=0
def bfs(x):
    queue.append(x)
    V[x]=True
    while queue:
        x=queue.popleft()
        for node in board[x]:
            if not V[node]:
                queue.append(node)
                V[node]=True

for i in range(1,len(V)):
    if not V[i]:
        bfs(i)
        cnt+=1
print(cnt)