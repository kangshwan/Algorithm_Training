#줄 세우기
from collections import deque

N, M = map(int, input().split())
inDegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

#A, B를 토대로 각 정점에 대해 진입차수 구함. 그래프에 A가 B를 가리키는 것도 추가
for i in range(M):
  A, B = map(int, input().split())
  inDegree[B] += 1
  graph[A].append(B)

q = deque()
ans = []  

# 진입차수가 0인 정점을 큐에 삽입
for j in range(1, N+1):
  if inDegree[j] == 0: q.append(j)

#q가 비기 전까지만(사이클이 x)
while q:
  x = q.popleft() #큐에서 노드 꺼냄
  ans.append(x) 
  
  for k in graph[x]:
    #새롭게 진입차수가 0이 된(inDegree에서 간선 제거) 정점을 큐에 삽입.
    if (inDegree[k] - 1) == 0: 
      q.append(k)
    inDegree[k] -= 1

for elem in ans:
  print(elem, end =' ')




'''
큐를 이용한 위상 정렬

'''