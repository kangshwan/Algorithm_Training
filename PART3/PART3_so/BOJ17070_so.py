# BOJ17070_파이프옮기기


n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def dfs(x, y, z):
    global ans

    if x == n - 1 and y == n - 1:
        ans += 1
        return

    # 대각선 이동
    if x + 1 < n and y + 1 < n:
        if home[x+1][y+1] == 0 and home[x][y+1] == 0 and home[x+1][y] == 0:
            dfs(x+1, y+1, 2)

    # 대각선이 가로일 때 대각선 가로 이동
    if z == 0 or z == 2:
        if y + 1 < n:
            if home[x][y+1] == 0:
                dfs(x, y + 1, 0)

    # 대각선 세로일 때 세로 이동
    if z == 1 or z == 2:
        if x+1 < n:
            if home[x+1][y] == 0:
                dfs(x+1, y, 1)


dfs(0, 1, 0)

print(ans)

# n = int(input())
# home = [list(map(int, input().split())) for _ in range(n)]
# ans = 0


# def can_go():

# def dfs(x,y,z):
#   global ans

#   if x == n - 1 and y == n - 1:
#     ans += 1
#     return

#   dxs, dys = [1,0,1] , [1,1,0]
#   for dx, dy in zip(dxs, dys):
#     new_x, new_y = x + dx, y + dy

#     if can_go(new_x, new_y)
'''

이 자리에 파이프가 놓여질 수 있는가? 판단하는 함수
놓여질 수 없는 경우
1. 가로로 놓았는데 세로로 놓으려는 경우
 파이프 두 칸의 x가 같을 때 y가 달라지는 경우
 
2. 세로로 놓았는데 다음에 가로로 놓으려는 경우
  파이프 두 칸의 y가 같을 때 x가 달라지는 경우

- 백트래킹
고쳐야 할 것
1. 무조건 0, 1부터 시작해서 n, n 에 도착하면 ans += 1.
2. 세로로 갔는데 n-1이면 백, 가로로 갔는데 n-1이면 백
'''
