import sys
N,M=map(int,sys.stdin.readline().split())
pok_name={}
pok_num={}
for i in range(N):
    name=sys.stdin.readline().rstrip()
    pok_name[i]=name
    pok_num[name]=i
for _ in range(M):
    question=sys.stdin.readline().rstrip()
    if ord('A')<=ord(question[0])<=ord('Z') or ord('a')<=ord(question[0])<=ord('z'):
        print(pok_num[question]+1)
    else:
        print(pok_name[int(question)-1])

"""
문제를 입력받을 때, 문제가 숫자인지 포켓몬 이름인지 구분할때
.isdigit()메소드를 사용했어도 됨
"""