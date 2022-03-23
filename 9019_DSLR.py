# A->B 변환하기 위한 최소한의 명령어 나열 출력
"""
사실 문제는 대놓고 전형적인 BFS문제라 크게 어렵지 않게 구현했는데
시간초과를 해결을 하지 못해서 찾아보니
1.A를 문자형으로써 생각하여 L,R 명령어를 수행할 때 인덱싱 기법을 사용한다거나 하면 시간초과가 발생
=> 정수형으로 L,R 구현해야함
2.명령어 S를 수행할 때 실수 했던 부분 :
n==0 일때 9999를 반환해주어야 하는데
잘못생각하고 n-1==0일때 9999를 반환하고 있었음
제일 늦게 알아차림
3.탐색 시 queue에서 꺼내올 때 바로 B값과의 비교를 통해서 탈출할 수 있는 구문을 추가해줌
시간초과에 도움이 될까 싶어서
"""
import sys
from collections import deque
T=int(sys.stdin.readline()) # Test Case
limit=10000
commands=['D','S','L','R']
def com_D(n):
    return (2*n)%limit
def com_S(n):
    if n==0:
        return 9999
    else:
        return n-1
def com_L(n):
    return ((n%1000)*10)+(n//1000)
def com_R(n):
    return ((n%10)*1000)+n//10
def bfs(start,target):
    queue=deque()
    queue.append(start)
    v[start]=True
    while queue:
        start=queue.popleft()
        if start==target:
            print(board[target])
            break
        for command in commands:
            if command=='D':
                next=com_D(start)
                if not v[next]:
                    queue.append(next)
                    board[next]=board[start]+command
                    v[next]=True
            elif command=='S':
                next = com_S(start)
                if not v[next]:
                    queue.append(next)
                    board[next] = board[start] + command
                    v[next] = True
            elif command=='L':
                next = com_L(start)
                if not v[next]:
                    queue.append(next)
                    board[next] = board[start] + command
                    v[next] = True
            elif command=='R':
                next = com_R(start)
                if not v[next]:
                    queue.append(next)
                    board[next] = board[start] + command
                    v[next] = True
for _ in range(T):
    A,B=map(int,sys.stdin.readline().split())
    board=['']*limit
    v=[False]*limit
    bfs(A,B)
# 시간초과 풀이(1)
"""import sys
from collections import deque
T=int(sys.stdin.readline()) # 테스트 케이스
limit=10000
commands=['D','S','L','R']
def command_D(n):
    tmp=n*2
    if tmp>9999:
        return tmp%limit
    else:
        return tmp
def command_S(n):
    tmp=n-1
    if tmp<1:
        return 9999
    else:
        return tmp
def command_L(n):
    tmp=str(n)
    if len(tmp)==4:
        return int(tmp[1:] + tmp[0])
    else:
        return int(tmp+('0'*(4-len(tmp))))
def command_R(n):
    tmp=str(n)
    if len(tmp)==4:
        return int(tmp[-1]+tmp[:3])
    else:
        tmp=('0'*(4-len(tmp)))+tmp
        return int(tmp[-1]+tmp[:3])
def sol(start):
    queue=deque()
    v=[False]*limit
    queue.append(start)
    v[start]=True
    while queue:
        start=queue.popleft()
        for command in commands:
            if command == 'D':
                next=command_D(start)
                if not v[next]:
                    queue.append(next)
                    board[next]=board[start]+command
                    v[next]=True
            elif command == 'S':
                next=command_S(start)
                if not v[next]:
                    queue.append(next)
                    board[next]=board[start]+command
                    v[next]=True
            elif command == 'L':
                next = command_L(start)
                if not v[next]:
                    queue.append(next)
                    board[next] = board[start] + command
                    v[next] = True
            else:
                next = command_R(start)
                if not v[next]:
                    queue.append(next)
                    board[next] = board[start] + command
                    v[next] = True

for _ in range(T):
    A,B=map(int,sys.stdin.readline().split()) # A : 레지스터 초기 값, B : 최종 값
    board = [''] * limit
    sol(A)
    print(board[B])
"""