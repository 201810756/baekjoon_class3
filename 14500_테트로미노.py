"""
나중에 다시 한번 풀어봐야될듯
* 조건 구현
* 예외 처리
* 생각을 코드로 옮기기
* 시간초과 해결 아이디어
* 너무어렵ㄷ
* 시간초과 3 틀렸습니다 3 지ㅏㄴ짜 왜 틀렸는지를 모르겠네
"""
"""import sys
N,M=map(int,sys.stdin.readline().split()) # N : 세로  M : 가로
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
# 테트로미노가 놓인 칸에 쓰인 수들의 합 ?
max_sum=0
max_cnt=4
max_board=max(max(board))
visited = [[False] * M for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def normal_block(x,y,cnt,tmp_sum):
    global max_sum,max_board
    visited[x][y]=True
    if tmp_sum + max_board*(4-cnt)<=max_sum:
        return
    if cnt==max_cnt:
        max_sum=max(max_sum,tmp_sum)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            normal_block(nx,ny,cnt+1,tmp_sum+board[nx][ny])
            visited[nx][ny]=False
def strange_block(x,y):
    global max_sum
    tmp=[]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M :
            tmp.append(board[nx][ny])
    if len(tmp)>=3:
        tmp.sort()
        tmp_sum=board[x][y]+sum(tmp[1:4])
        max_sum=max(max_sum,tmp_sum)

result=0
for i in range(N):
    for j in range(M):
        normal_block(i,j,1,board[i][j])
        visited[i][j]=False
        strange_block(i,j)
print(max_sum)"""
# 구글링 갖다빼낌 https://velog.io/@jajubal/파이썬백준-14500-테트로미노
import sys;
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)