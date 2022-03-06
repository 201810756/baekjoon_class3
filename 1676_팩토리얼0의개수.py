"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""
import sys
N=int(sys.stdin.readline())
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
result_str=str(factorial(N))
cnt=0
for k in range(len(result_str)-1,-1,-1):
    if result_str[k]!='0':
        break
    cnt+=1
print(cnt)