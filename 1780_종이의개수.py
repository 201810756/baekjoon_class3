"""
N×N크기의 행렬로 표현되는 종이가 있다.
종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고,
각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때,
-1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수,
1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
"""
# sol1
import sys
N=int(sys.stdin.readline())
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
result=[0,0,0]

def check(start_col,start_row,n):
    global result
    check_num=board[start_col][start_row]
    for i in range(start_col,start_col+n):
        for j in range(start_row,start_row+n):
            if check_num!=board[i][j]:
                for k in range(3):
                    for l in range(3):
                        check(start_col+k*n//3,start_row+l*n//3,n//3)
                return
    if check_num==-1:
        result[0]+=1
    elif check_num==0:
        result[1]+=1
    elif check_num==1:
        result[2]+=1
check(0,0,N)
for r in result:
    print(r,end='\n')


