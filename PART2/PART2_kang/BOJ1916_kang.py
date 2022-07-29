import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())

# dijkstra 수행을 위한 heap 생성
heap = []

graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int,input().split())
    # 입력이 1~N이므로 -1하여 인덱스 맞춰줌
    graph[u-1].append([v-1, w])
    # uni-direction이다!! two-way 아님.
    
source, dest = map(int,input().split())
dist = [INF for _ in range(N)]

def Dijkstra(x):
    dist[x] = 0
    heapq.heappush(heap,(0, x))
    while heap:
        cost, current = heapq.heappop(heap)
        # heap에는 아래 코드에서 동일한 위치에 다른 cost로 여러개가 들어가있을 수 있음.
        # 물론 heap에 따라서 가장 짧은것이 먼저 나오겠지만, 나중에는 찌꺼기들이 들어있음.
        # 바로 아래 코드는 찌꺼기들을 걸러내기 위한 코드다.
        if dist[current] < cost:
            print(f'({cost}, {current})')
            continue

        for next, weight in graph[current]:
            if cost+weight < dist[next]:
                dist[next] = cost+weight
                heapq.heappush(heap,(dist[next], next))
Dijkstra(source-1)
print(dist[dest-1])
"""
ex)
4
5
1 2 3
1 3 2
1 4 10000
2 4 1
3 4 6
1 4
의 경우에는 heap에 (4,4) (8,4) (10000,4) 등 4가 여러번 들어가는데
heap에 따라서 가장 짧은것이 나오고 (방문되고) dist[4]가 가장 작아졌을것이기 때문에
나머지는 최소인 dist[4]보다 크게 나올것.
방문의 역할을
if dist[current] < cost:
    continue
가 대신 해주고 있음.
노드가 많을수록 heap에 찌꺼기가 많이 쌓임(위처럼 코드 작성할 경우)
"""
