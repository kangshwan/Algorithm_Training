# BOJ1303_전쟁-전투
n, m = map(int, input().split())  # 전쟁터의 가로, 세로 크기

graph = []
for _ in range(m):
    color = input()
    graph.append(list(color))

visited = [[False for _ in range(n)] for _ in range(m)]

def in_range(x, y):
    global n, m
    return 0 <= x and x < m and 0 <= y and y < n

def white_can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or graph[x][y] == 'B':
        return False
    return True
def blue_can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or graph[x][y] == 'W':
        return False
    return True

def w_dfs(x, y):
    global graph, white
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if white_can_go(new_x, new_y):
            white += 1
            visited[new_x][new_y] = True
            w_dfs(new_x, new_y)
def b_dfs(x, y):
    global graph, blue
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if blue_can_go(new_x, new_y):
            blue += 1
            visited[new_x][new_y] = True
            b_dfs(new_x, new_y)

white_team = []
blue_team = []

for i in range(m):
    for j in range(n):
        if white_can_go(i, j):
            visited[i][j] = True
            white = 1

            w_dfs(i, j)

            white_team.append(white)
        if blue_can_go(i, j):
            visited[i][j] = True
            blue = 1

            b_dfs(i, j)

            blue_team.append(blue)

my_team, your_team = 0, 0
for i in white_team:
    my_team += i**2

for i in blue_team:
    your_team += i**2

print(my_team, your_team, end=' ')










'''
  3
0   2
  1
  
내 병사 - 흰색 옷
적국 병사 = 파란 옷

병사들은 모일수록 강해짐 N명이 뭉쳐있으면 N^2만큼의 힘을 냄

누가 승리하는가?
단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.


내 병사의 위력의 합, 적국 병사의 위력의 합


* dx, dy 테크닉 bfs로 하는 법도 찾아보기 *
'''
