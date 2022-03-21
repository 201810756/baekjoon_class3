import sys
N,M=map(int,sys.stdin.readline().split()) # N : 저장된 사이트의 수, M : 비밀번호 찾으려는 사이트 수
info=dict()
for _ in range(N):
    site,password=sys.stdin.readline().split()
    info[site]=password
for _ in range(M):
    findsites=sys.stdin.readline().rstrip()
    print(info[findsites])
