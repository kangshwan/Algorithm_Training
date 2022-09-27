#BOJ2178_미로탐색
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
  line = input()
  line = list(line)
  for j in range(M):
    line[j] = int(line[j])
  graph.append(line)

visited = [[False for _ in range(M)] for _ in range(N)]
step = [[0 for _ in range(M)] for _ in range(N)] #최소의 칸 수를 적어준다

def in_range(x,y):
  return 0 <= x < N and 0 <= y < M

def can_go(x, y):
  global visited, graph
  if not in_range(x, y): return False
  if visited[x][y] or graph[x][y] == 0: return False
  return True

def bfs(n, m):
  dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
  q = deque([(n,m)])
  visited[n][m] = True
  
  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = dx + x, dy + y
      if can_go(nx, ny):
        step[nx][ny] = step[x][y] + 1 
        q.append((nx, ny))
        visited[nx][ny] = True
        
bfs(0, 0)
print(step[N-1][M-1]+1)

'''
    1
  0   2
    3

1 - 이동 가능
0 - 이동 불가능


(1,1)에서 출발 -> (N, M) 이동 최소 칸 수
서로 인접칸만 가능

N - 세로, M - 가로
'''