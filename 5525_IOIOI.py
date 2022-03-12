import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline()) # S의 길이
S=sys.stdin.readline().rstrip()
i=0
cnt=0
result=0
# Pn이란, n+1개의 I와 n개의 0이 서로 교대로 나오는 문자열
# S에 Pn이 몇 군데 포함되어 있는지 출력
while i<=(M-2):
    if S[i:i+3]=="IOI": # 규칙성을 갖는 모양 IOIOIOIOIOIOIOIOIOIOI...
        i+=2 # IOIOI => IO+I+OI (I는 중복)
        cnt+=1
        if cnt==N: # IOIOI라면 cnt=2 즉 N의 값과 같다 => result+=1
            result+=1
            cnt-=1
    else:
        i+=1
        cnt=0 # 규칙성이 깨졌으므로 cnt=0
print(result)

"""sol2(50)
P=[]
for i in range((2*N)+1):
    if i%2==0:
        P.append("I")
    else:
        P.append("O")
result=0
for i in range(0,M-(2*N)):
    if S[i:i+((2*N)+1)]==P:
        result+=1
print(result)
"""


"""sol1(50)
check_queue=deque()
result=0
cnt=0
for letter in S:
    check_queue.append(letter)
    cnt += 1
    if cnt==((2*N)+1):
        if check_queue==P:
            result+=1
            check_queue.popleft()
            cnt=(2*N)
        else:
            check_queue.popleft()
            cnt=(2*N)
print(result)
"""