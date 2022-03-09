"""
출력결과의 형식을 잘 살펴보자.
deque의 reverse()를 사용하면 시간초과가 발생한다.
처음에는 error에 대해서만 flag를 사용하였지만
reverse() 함수를 쓰면 안되므로 방향성에 대해서도 flag사용
"""

import sys
T=int(sys.stdin.readline()) # Test Case
from collections import deque
for _ in range(T):
    er_flag=0
    di_flag=0 # 순방향
    p=sys.stdin.readline().rstrip() # 수행할 함수 R:뒤집기 / D:첫번째 수 버리기
    n=int(sys.stdin.readline()) # 배열의 원소의 개수
    test_list = deque()
    if n==0:
        origin_list=sys.stdin.readline().rstrip()
    else:
        origin_list=sys.stdin.readline().rstrip() # 배열 [x1,x2,...,xn]형태로 주어짐
        st=''
        for i in range(len(origin_list)):
            if origin_list[i]=='[':
                continue
            elif origin_list[i]==']':
                test_list.append(int(st))
            elif origin_list[i]==',':
                test_list.append(int(st))
                st=''
            else:
                st+=origin_list[i]
    for command in p:
        if command=='R':
            #test_list.reverse()
            if di_flag==0:
                di_flag=1
            else:
                di_flag=0
        elif command=='D':
            if len(test_list)==0:
                er_flag=1
            else:
                if di_flag==0:
                    test_list.popleft()
                else:
                    test_list.pop()
    if er_flag==1:
        print("error")
    else:
        if di_flag==0:
            print('[',end='')
            for i in range(len(test_list)):
                print(test_list[i],end='')
                if i!=len(test_list)-1:
                    print(',',end='')
            print(']')
        else:
            print('[', end='')
            for i in range(len(test_list)-1,-1,-1):
                print(test_list[i], end='')
                if i!=0:
                    print(',',end='')
            print(']')
