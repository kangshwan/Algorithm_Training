# 최소비용 구하기

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start_city, end_city = map(int, sys.stdin.readline().split())

INF = 100000000
dist = [INF] * (N+1)

def dikstra(start):
    # global INF, dist, graph
    Q = []
    
    heapq.heappush(Q, (0, start))
    dist[start] = 0  # 처음 시작하는 도시 0으로

    while Q:
        d, now = heapq.heappop(Q)

        if dist[now] < d:  # 이미 최솟값이 존재하면 넘어감
            continue
          
        for v1, w1 in graph[now]:
            cost = d + w1 #  (현재 dist 값 + 간선 가중치 값)
            if cost < dist[v1]:
                dist[v1] = cost
                heapq.heappush(Q, (cost, v1))  # 큐에 넣어줌

dikstra(start_city)
print(dist[end_city])

'''
1. 다익스트라 이용해서 푸는데, 입력을 고려 안 해서 틀림
2. graph 내에 u,v,w를 모두 넣어서 했더니 꼬여서 못품
3. graph를 이중 배열로 만들 때, 노드에 따라 나누어줬지만 출력이 잘못되어 틀림(cost를 출력했는데 end_city의 최솟값이 필요했음)
4. 34줄에 cost 부분에서 d + w1인데 (현재!!!! dist 값 + 간선 가중치 값) dist[v1]으로 해서 틀림 현재 dist 유의하기

'''
