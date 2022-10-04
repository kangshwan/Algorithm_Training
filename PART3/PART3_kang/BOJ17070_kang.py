N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
answer = 0
def inRange(x,y):
    return 0<=x<N and 0<=y<N

def canGo(nx,ny,dir):
    if dir != 2:
        return not board[nx][ny]
    return not board[nx-1][ny] and not board[nx-1][ny-1] and not board[nx][ny-1] and not board[nx][ny]
    
def DFS(x, y, dir):
    global answer
    if x == N-1 and y == N-1:
        answer+=1
    if dir == 0:
        # →
        nx,ny = x,y+1
        if inRange(nx,ny) and canGo(nx,ny,0):
            DFS(nx,ny,0)
        # ↘
        nx, ny = x+1, y+1
        if inRange(nx,ny) and canGo(nx,ny,2):
            DFS(nx,ny,2)
    elif dir == 1:
        # ↓
        nx,ny = x+1,y
        if inRange(nx,ny) and canGo(nx,ny,1):
            DFS(nx,ny,1)
        # ↘
        nx, ny = x+1, y+1
        if inRange(nx,ny) and canGo(nx,ny,2):
            DFS(nx,ny,2)
    else:
        # →
        nx,ny = x,y+1
        if inRange(nx,ny) and canGo(nx,ny,0):
            DFS(nx,ny,0)
        # ↓
        nx,ny = x+1,y
        if inRange(nx,ny) and canGo(nx,ny,1):
            DFS(nx,ny,1)
        # ↘
        nx, ny = x+1, y+1
        if inRange(nx,ny) and canGo(nx,ny,2):
            DFS(nx,ny,2)
DFS(0,1,0)
print(answer)

# def checkEmpty(x,y):
#     for dir in range(3):
#         nx,ny = x+dx[dir], y+dy[dir]
#         if not inRange(nx,ny) or isWall[nx][ny]:
#             return False
#     return True
# for i in range(N):
#     for j in range(N):
#         if dp[i][j] == 0:
#             continue
#         # 현재 파이프가 가로인 경우
#         if pdir[i][j]==0:
#             for dir in (0,2):
#                 nx, ny = i+dx[dir], j+dy[dir]
#                 # 대각으로 둘 경우에는 빈공간이 모두 확보되었는지 확인해야함.
#                 if dir == 2:
#                     if not checkEmpty(i,j):
#                         break
#                 if inRange(nx,ny) and not isWall[nx][ny]:
#                     dp[nx][ny]+=dp[i][j]
#                     # 대각선을 가장 큰 dir값을 갖도록 설정했기 때문에 max 사용해서 처리.
#                     pdir[nx][ny] = max(dir, pdir[nx][ny])                
#         # 현재 파이프가 세로인 경우
#         elif pdir[i][j]==1:
#             for dir in (1,2):
#                 nx, ny = i+dx[dir], j+dy[dir]
#                 if dir == 2:
#                     if not checkEmpty(i,j):
#                         break
#                 if inRange(nx,ny) and not isWall[nx][ny]:
#                     dp[nx][ny]+=dp[i][j]
#                     # 대각선을 가장 큰 dir값을 갖도록 설정했기 때문에 max 사용해서 처리.
#                     pdir[nx][ny] = max(dir, pdir[nx][ny])                
#         # 현재 파이프가 대각인 경우
#         else:
#             for dir in range(3):
#                 nx, ny = i+dx[dir], j+dy[dir]
#                 if dir == 2:
#                     if not checkEmpty(i,j):
#                         break
#                 if inRange(nx,ny) and not isWall[nx][ny]:
#                     dp[nx][ny]+=dp[i][j]
#                     # 대각선을 가장 큰 dir값을 갖도록 설정했기 때문에 max 사용해서 처리.
#                     pdir[nx][ny] = max(dir, pdir[nx][ny])                