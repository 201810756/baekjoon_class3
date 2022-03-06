"""
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
#sol1
"""N,K=map(int,sys.stdin.readline().split()) # N:수빈위치, K:동생위치
d=[1000001]*200002
d[N]=0
result=0
if N>K:
    result=N-K
else:
    for i in range(N,K):
        d[i*2]=d[i]+1
        if (i+1)%2==0:
            continue
        else:
            d[i + 1] = min(d[i],d[i+1],d[i + 2]) + 1
    result=d[K]
print(result)"""
#sol2
"""N,K=map(int,sys.stdin.readline().split()) # N:수빈위치, K:동생위치
d=[1000001]*200002
d[N]=0
d[N+1]=1
d[N-1]=1
result=0
if N>K:
    result=N-K
else:
    for i in range(N-1,K+1):
        if i*2==K:
            result=d[i]+1
            break
        else:
            d[i*2]=d[i]+1
            d[(i*2)-1]=d[i*2]+1
            d[(i*2)+1]=d[i*2]+1
            if (i+1)%2==0:
                if (i+1)//2 < N:
                    d[i+1]=min(d[i],d[i+2])+1
                else:
                    if d[i+1]<min(d[i],d[i+2]):
                        continue
                    else:
                        d[i+1]=min(d[i],d[i+2])+1
            else:
                if d[i+1]<min(d[i],d[i+2]):
                    continue
                else:
                    d[i+1]=min(d[i],d[i+2])+1
        result=d[K]
print(result)"""
# sol3(bfs 개념 활용)
import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split()) # N:수빈위치, K:동생위치
MAX=100000
d=deque()
visited=[0 for _ in range(MAX+1)]
def check(v):
    d.append(v)
    while d:
        v=d.popleft()
        if v==K:
            return visited[v]
        for i in (v-1,v+1,v*2):
            if 0<=i<=MAX and visited[i]==0:
                visited[i]=visited[v]+1
                d.append(i)
print(check(N))