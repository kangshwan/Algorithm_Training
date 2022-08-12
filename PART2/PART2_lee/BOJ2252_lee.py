# 2252 줄세우기
# 위상정렬

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)] # 내 뒤에 있어야 하는 사람들
front = [0 for _ in range(n + 1)] # 앞에 있어야 하는 사람 수
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    front[b] += 1

q = deque()
for i in range(1, n + 1):
    if front[i] == 0: # 내 앞에 있어야 하는 사람이 없으면
        q.append(i) # 큐에 삽입

while q:
    now = q.popleft() # 현재 줄서는 사람
    answer.append(str(now))
    for i in graph[now]: # 현재 줄서는 사람 뒤에 서야 하는 사람들
        front[i] -= 1 
        if front[i] == 0:
            q.append(i)

print(" ".join(answer))