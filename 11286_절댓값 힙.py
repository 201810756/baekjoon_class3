"""
절댓값 힙
1. 배열에 정수 x를 넣는다 (x!=0)
2. 배열에서 절댓값이 가장 작은 값 출력, 그 값을 배열에서 제거.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수 출력, 배열에서 제거

연산 종류 :
x!=0 : x를 넣어라
x==0 : 연산 2 실행
"""
import sys
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    command=int(sys.stdin.readline())
    if command!=0:
        heapq.heappush(heap,(abs(command),command))
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
