"""
김진영이 듣도 못한 사람의 명단과,
보도 못한 사람의 명단이 주어질 때,
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""
# sol1(시간초과)
"""import sys
N,M=map(int,sys.stdin.readline().split())
listen=[]
see=[]
both=[]
cnt=0
for _ in range(N):
    listen.append(sys.stdin.readline().rstrip())
for _ in range(M):
    see.append(sys.stdin.readline().rstrip())
for name in listen:
    if name in see:
        cnt+=1
        both.append(name)
print(cnt)
both.sort()
for both_name in both:
    print(both_name,end='\n')"""
# sol2(딕셔너리 사용)
"""import sys
N,M=map(int,sys.stdin.readline().split())
name=dict()
results=[]
for _ in range(N):
    a=sys.stdin.readline().rstrip()
    name[a]=1
for _ in range(M):
    b=sys.stdin.readline().rstrip()
    if b in name:
        results.append(b)
results.sort()
print(len(results))
for result in results:
    print(result,end='\n')"""
# sol3(set사용)
import sys
N,M=map(int,sys.stdin.readline().split())
listen=set()
see=set()
for _ in range(N):
    listen.add(sys.stdin.readline().rstrip())
for _ in range(M):
    see.add(sys.stdin.readline().rstrip())
results=list(listen&see)
results.sort()
print(len(results))
for result in results:
    print(result,end='\n')