import sys
N=int(sys.stdin.readline()) # 정점의 개수 N
board=[]
for _ in range(N): # 인접 행렬
    board.append(list(map(int,sys.stdin.readline().split())))

# i -> j 경로 있으면 [i,j]=1
# 거쳐간다 ? 플로이드와샬

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1 or (board[i][k]==1 and board[k][j]==1):
                board[i][j]=1
for line in board:
    for result in line:
        print(result,end=' ')
    print()
