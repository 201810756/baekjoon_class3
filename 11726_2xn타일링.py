# sol1(IndexError)
"""import sys
N=int(sys.stdin.readline())
# 2xN 크기의 직사각형을 1x2, 2x1 크기의 타일로 채우는 방법의 수
dp=[0]*(N+1)
dp[1]=1
dp[2]=2
for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N]%10007)"""
# sol2
import sys
N=int(sys.stdin.readline())
dp=[0,1,2]
for i in range(3,1001):
    dp.append(dp[i-1]+dp[i-2])
print(dp[N]%10007)