# 못풀어서 결국 구글링
import sys
import math
INF=1e9
n=int(sys.stdin.readline())
# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현될 수 있다
# 26은 5^2+1^2 또는 4^2+3^2+1^2
# 자연수 n이 주어질 때, n을 최소 개수의 제곱수의 합으로 표현하라
# 합이 n과 같게 되는 제곱수들의 최소 개수 출력

# dynamic programming
dp=[0]*(n+1) # dp리스트 사용
dp[0],dp[1]=0,1 # 초기값
for i in range(2,n+1): # dp 배열 돌기, 2 ~ n까지
    min_value=INF # 초기 최소값은 최대로 설정(INF)
    for j in range(1,int(math.sqrt(i))+1): # j = 1~i의 제곱근까지 반복
        min_value=min(min_value,dp[i-(j**2)])
    dp[i]=min_value+1
print(dp[n])
# PyPy3로 통과함
# 구하는 규칙 자체가 좀 어려움
# 풀기 싫은 스탕ㄹ;
