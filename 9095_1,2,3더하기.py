import sys
T=int(sys.stdin.readline())
# 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수
def plus(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return plus(n-1)+plus(n-2)+plus(n-3)

for _ in range(T):
    n=int(sys.stdin.readline())
    print(plus(n))