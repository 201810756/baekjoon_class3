import sys
N=int(sys.stdin.readline()) # N : 계단의 수
stairs=[]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))
# 규칙
# 계단은 한 번에 한 계단 혹은 두 계단 +1 or +2
# 연속된 세 개의 계단 x (시작점은 미포함)
# 마지막 도착 계단은 반드시 포함
dp=[0]*(N+1)
if N==1:
    print(stairs[0])
else:
    dp[1]=stairs[0]
    dp[2]=dp[1]+stairs[1]
    for i in range(3,N+1):
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i-2],dp[i-2]+stairs[i-1])
    print(dp[N])
""" 
DP는 결국 점화식 
계단은 최대 2칸까지 연속으로 오를 수 있음 idea
현재칸+(-1칸)+(-3칸까지) or 현재칸+(-2칸까지) 
(oxoo) or (ooxo)
"""