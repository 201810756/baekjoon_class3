import sys
N,M=map(int,sys.stdin.readline().split()) # 수의 개수 N, 합을 구해야 하는 횟수 M
num=list(map(int,sys.stdin.readline().split())) # N개의 수
sum_list=[0]
for i in range(N):
    sum_list.append(sum_list[-1]+num[i])
for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print((sum_list[j]-sum_list[i-1]))

# 처음에 두 가지 방법 모두  시간초과 발생
# 인덱스 슬라이싱 , 무작정 for문 모두 시간초과 발생
# 그럴만도 한게 N의 범위가 10만까지 , 반복문으로 M 횟수만큼 돌기에는 복잡도 너무 큼
# 미리 누적합을 구해놓고 (어짜피 처음 수를 입력받는건 단 한번, 리셋되지 않음)
# 인덱스를 입력받았을때 누적합을 구해놓은 리스트에 단순 접근만 하여 풀자
# dp 리스트같이
