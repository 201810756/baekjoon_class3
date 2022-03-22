# 해결 x -> 구글링
import sys
#import math
T=int(sys.stdin.readline()) # 테스트 케이스
for _ in range(T):
    M,N,x,y=map(int,sys.stdin.readline().split())
    flag=0
    while x<=(M*N):
        if x%N==y%N:
            print(x)
            flag=1
            break
        x+=M
    if flag==0:
        print(-1)
# M,N보다 작거나 같은 두 개의 자연수 x,y를 가지고 각 년도를 <x:y>로 표현
# 첫번째 해 <1:1>
# 두번째 해 <2:2>
# <x,y>의 다음 해 <x',y'>라고 하면, 만약 x<M -> x'=x+1, 아니면 x'=1
# y<N -> y'=y+1, 아니면 y'=1
# <M,N> 마지막 해, 종말
# <M:N>이 마지막 해라면, <x:y>는 몇번째 해를 나타내는지 구하라
# 만약 <x:y>에 해당하는 해가 없다면, -1 출력


# 단순 while문 -> 시간초과 발생
# M,N,x,y의 범위가 1~40,000 이므로 사실상 반복문으로는 불가능
# 규칙을 찾아야함
"""틀린 풀이
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    max_year = math.lcm(M, N)
    flag,result=0,0
    for i in range(x,max_year+1,M):
        if i%N==y:
            result=i
            flag=1
            break
    if flag==1:
        print(result)
    else:
        print(-1)"""
"""시간초과(2)
for _ in range(T):
    M,N,x,y=map(int,sys.stdin.readline().split())
    max_year=math.lcm(M,N)
    flag,result=0,0
    for i in range(1,max_year+1):
        if i%M==x and i%N==y:
            result=i
            flag=1
            break
    if flag==1:
        print(result)
    else:
        print(-1)"""

"""시간초과(1)
for _ in range(T):
    cnt=1 # 결과값 저장 변수
    M,N,x,y=map(int,sys.stdin.readline().split())
    start_x,start_y=1,1
    flag=0
    while start_x!=M or start_y!=N:
        cnt+=1
        if start_x<M:
            start_x+=1
        else:
            start_x=1
        if start_y<N:
            start_y+=1
        else:
            start_y=1
        print(cnt, 'x:',start_x,'y:',start_y)
        if start_x==x and start_y==y:
            flag=1
            break
    if flag==1:
        print(cnt)
    else:
        print(-1)
"""