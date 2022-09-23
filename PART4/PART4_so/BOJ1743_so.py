#BOJ1743_음식물 피하기
from collections import deque

n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1

visited=[[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
  return 0 <= x < n and 0 <= y < m

def can_go(x, y):
  if not in_range(x,y): return False
  elif visited[x][y] or graph[x][y] == 0: return False
  return True

def bfs(x, y):
  global visited
  dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
  new_waste = 1
  q = deque()
  q.append((x, y))
  
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if can_go(nx,ny):
        q.append((nx, ny))
        visited[nx][ny] = True
        new_waste += 1
  
  return new_waste

waste = 0
for i in range(n):
  for j in range(m):
    if can_go(i, j):
      waste = max(waste, bfs(i,j))
      
print(waste)
        
  
  
  

'''
  4
1   3
  2

n = 세로 길이
m = 가로 길이
k = 음식물 쓰레기의 개수
밑의 줄은 좌표(r,c) -> 음식물이 떨어진 곳 (r은 위에서부터, c는 왼쪽에서부터가 기준)

음식물이 있는 곳은 1로 표시하기
'''