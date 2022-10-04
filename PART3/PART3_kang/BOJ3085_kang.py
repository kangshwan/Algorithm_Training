N = int(input())
board=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for _ in range(N):
    tmp=[]
    for candy in input():
        tmp.append(candy)
    board.append(tmp)
del tmp
def inRange(x,y):
    global N
    return 0<=x<N and 0<=y<N
ans=0
def canEat():
    global board
    r_val = 0
    for x in range(N):
        maxEat = 1
        curCandy = board[x][0]
        for y in range(1,N):
            if board[x][y] == curCandy:
                maxEat+=1
            else:
                r_val = max(r_val, maxEat)
                maxEat=1
                curCandy=board[x][y]
        r_val = max(r_val, maxEat)
    for y in range(N):
        maxEat = 1
        curCandy = board[0][y]
        for x in range(1,N):
            if board[x][y] == curCandy:
                maxEat+=1
            else:
                r_val = max(r_val, maxEat)
                maxEat=1
                curCandy=board[x][y]
        r_val = max(r_val, maxEat)
    return r_val

for x in range(N):
    for y in range(N):
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # nx,ny가 범위 안에 있고, 서로 사탕의 색이 다를 경우
            if inRange(nx,ny) and board[x][y] != board[nx][ny]:
                # swap candy
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                ans = max(ans, canEat())
                # 원위치, 모든 경우를 보기 위함
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
print(ans)
'''
board 최대 크기: 50x50
전수조사할 경우-> 
모든 candy에 대해서 상하좌우 교환,교환 후 모든 행/열 체크
50x50            x   4          x 5000
=50000000 (5천만, 1억도 안됨)
'''