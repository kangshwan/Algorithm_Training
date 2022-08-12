# 1916 최소비용 구하기
# 다익스트라

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 도시 번호는 1 ~ N
dict_graph = dict()
for _ in range(N) :
    dict_graph[_ + 1] = dict()

# 도시 별 버스 정보 저장
for _ in range(M):
    tmp_start, tmp_end, fee = map(int, sys.stdin.readline().split())
    if (tmp_end in dict_graph[tmp_start] and dict_graph[tmp_start][tmp_end] < fee) :
        continue
    dict_graph[tmp_start][tmp_end] = fee 

start, end = map(int, input().split())

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances

print(dijkstra(dict_graph, start)[end])