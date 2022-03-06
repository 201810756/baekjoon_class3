"""
흰점 : 0
검은점:1

"""
import sys
def quad(x,y,size):
    flag=1
    tmp=board[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[i][j]!=tmp:
                flag=0
                break
    if flag==1:
        print(int(tmp),end='')
    elif flag==0:
            print('(', end='')
            quad(x,y,size//2)
            quad(x,y+size//2,size//2)
            quad(x+size//2,y,size//2)
            quad(x+size//2,y+size//2,size//2)
            print(')',end='')
N=int(sys.stdin.readline())
board=[]
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
quad(0,0,N)