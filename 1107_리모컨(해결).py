import sys
N=int(sys.stdin.readline()) # 가고 싶은 채널
M=int(sys.stdin.readline()) # 고장난 채널의 수
if M!=0:
    error_list=list(map(int,sys.stdin.readline().split())) # 고장난 채널 번호
# 현재 채널 = 100
    result=abs(N-100) # 단순히 +,- 버튼으로만 조정
    for i in range(1000001): # 채널 => 500000까지 따라서 위,아래 모두 고려
        tmp=str(i)
        for j in range(len(tmp)):
            if int(tmp[j]) in error_list:
                break
            elif j==(len(tmp)-1):
                result=min(result,abs(i-N)+len(tmp))
    print(result)
else:
    print(min(abs(N-100),len(str(N))))

"""
무작정 구현하기에는 너무 많은 조건들이 있어서 상당히 까다롭다.
실제로 모든 조건들을 고려하여 구현하려 하였지만 계속 실패해서 포기했다. 
브루트포스 알고리즘에 해당하는데 
전체 채널의 0~1000001까지 중에서 지금 현재 누를 수 있는 리모컨의 버튼으로 갈 수 있는 
채널에 가서 목표하는 채널까지의 차이(즉 +,- 버튼의 횟수)와 그 버튼을 누른 횟수(len)의 합과 
현재까지의 최소값과의 비교를 통해서 결국 최종적인 최소 버튼 횟수를 구할 수 있다. 
사실 숫자가 너무 커서 무작정 모든 경우를 체크한다는 생각을 하지는 못하고 
좀 더 효율적인 방법을 찾기 위해서 여러 생각들을 해봤지만 실패하고 결국 구글링을 통해 아이디어를 얻었다.
"""