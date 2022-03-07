import sys
N=int(sys.stdin.readline())
# N = 2,4,8,16,32,64,128
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
cnt=[0,0]
def check(start_x,start_y,size):
    flag=1
    tmp = board[start_x][start_y]
    for i in range(start_x,start_x+size):
        for j in range(start_y,start_y+size):
            if tmp!=board[i][j]:
                flag=0
                break
    if flag==1:
        if tmp==0:
            cnt[0]+=1
        else:
            cnt[1]+=1
    else:
        check(start_x,start_y,size//2)
        check(start_x,start_y+size//2,size//2)
        check(start_x+size//2,start_y,size//2)
        check(start_x+size//2,start_y+size//2,size//2)
check(0,0,N)
for result in cnt:
    print(result,end='\n')