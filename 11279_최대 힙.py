import sys
import heapq
N=int(sys.stdin.readline())
# X:자연수->추가 / X:0->가장 큰 값 출력 및 제거
heap=[]
for _ in range(N):
    X=int(sys.stdin.readline())
    if X!=0:
        heapq.heappush(heap,(-X))
    elif X==0:
        if len(heap)==0:
            print(0)
        else:
            print((heapq.heappop(heap))*(-1))
