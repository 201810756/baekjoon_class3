"""
널리 잘 알려진 자료구조 중 최소 힙이 있다.
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
"""
import sys
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    # x=0 : 가장 작은 값 출력 후 제거
    # x=자연수 : 배열에 x 추가
    x=int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap,x)
    elif x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
"""
python 힙큐(heapq)
* 최댓값, 최솟값을 찾는 연산을 빠르게 할 수 있는 완전이진트리 
import heapq 

heap=[] 선언 
heapq.heappush(heap,value) value 삽입

이미 생성된 리스트에 대해서 
list=[1,2,10,4]
heapq.heapify(list)
>> [1,2,4,10]

heapq.heappop(heap) 연산은 가장 작은 원소를 heap에서
제거함과 동시에 그 결과값을 리턴해줌
삭제하고 싶진 않고 그저 값에만 접근하고 싶다면 [0] 인덱스에 바로 접근
 
"""