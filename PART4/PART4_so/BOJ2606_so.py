#BOJ2606_바이러스
from collections import deque

com = int(input())
path_num = int(input())

graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for _ in range(path_num):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def bfs(start):
  cnt = 0
  q = deque()
  q.append(start)
  visited[start] = True

  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        cnt += 1
        q.append(i)
        visited[i] = True
  return cnt  
    
print(bfs(1))
'''
같은 네크워크 상에서 바이러스 걸림

컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
'''