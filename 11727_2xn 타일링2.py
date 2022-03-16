import sys
n=int(sys.stdin.readline())
# 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지 출력
dp=[0]*1001
dp[1]=1
dp[2]=3
dp[3]=5
# index=2까지만 구하고 했었어도 됐네
for i in range(4,n+1):
    dp[i]=dp[i-1]+(dp[i-2]*2)
print(dp[n]%10007)