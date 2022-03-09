"""
동기화 측면에서 어려움 겪음
리스트 remove()는 시간초과를 유발
시간초과 해결 못하고 결국 구글링
"""
import sys
import heapq
T=int(sys.stdin.readline()) # Test Case
def sol(k):
    min_queue=[]
    max_queue=[]
    dic={}
    for i in range(k):
        command, num=sys.stdin.readline().split()
        if command=='I':
            heapq.heappush(min_queue,int(num))
            heapq.heappush(max_queue,-int(num))
            if dic.get(int(num)):
                dic[int(num)]+=1
            else:
                dic[int(num)]=1
        else:
            if num=='1':
                while max_queue:
                    tmp=-heapq.heappop(max_queue)
                    if dic[tmp]>0:
                        dic[tmp]-=1
                        break
            else:
                while min_queue:
                    tmp=heapq.heappop(min_queue)
                    if dic[tmp]>0:
                        dic[tmp]-=1
                        break
    remain=[]
    for key,value in dic.items():
        if value>0:
            remain.append(key)
    if len(remain)==0:
        print("EMPTY")
    else:
        remain.sort()
        print(remain[-1],remain[0])

for _ in range(T):
    k=int(sys.stdin.readline()) # 연산 개수
    sol(k)




