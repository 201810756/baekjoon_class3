import sys
from collections import deque
N=int(sys.stdin.readline())
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
# 1 : 집이 있음 / 0 : 집이 없음
# 단지에 번호를 붙이고, 단지수 출력 & 단지에 속하는 집의 수 오름차순
house_queue=deque()
town_num=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def house_check():
    flag=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                house_queue.append((i,j))
                flag=1
                break
        if flag==1:
            break
def bfs():
    global town_num
    cnt_list=[]
    cnt=0
    house_check()
    while house_queue:
        x,y=house_queue.popleft()
        board[x][y]=-1
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==1:
                board[nx][ny]=-1
                house_queue.append((nx,ny))
        if len(house_queue)==0:
            cnt_list.append(cnt)
            cnt=0
            house_check()
            town_num+=1
    return cnt_list
result_list=bfs()
result_list.sort()
print(town_num)
for result in result_list:
    print(result)
