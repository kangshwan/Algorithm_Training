#BOJ12851_숨바꼭질2
from collections import defaultdict, deque

N, K = map(int,input().split())
max_size = 100001
visited = [False] * max_size

#가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 구하기 위해 딕셔너리 선언
counted = defaultdict(int)

def bfs(start):
    q = deque()
    q.append([start, 0])
    
    while q:
      cur, cnt = q.popleft() #수빈이의 위치와 현재 시간
      visited[cur] = True
      
      #동생 위치에 도달했을 때 key 값으로 value에 += 1
      if cur == K: counted[cnt] += 1
      else:
        if 0 <= cur + 1 < max_size and not visited[cur + 1]:
          q.append([cur + 1, cnt + 1])
        if 0 <= cur - 1 < max_size and not visited[cur - 1]:
          q.append([cur - 1, cnt + 1])
        if 0 <= cur * 2 < max_size and not visited[cur * 2]:
          q.append([cur * 2, cnt + 1])
          
    #counted에 저장된 값들 중 첫번째 값이 가장 빠른 시가느로 수빈이가 동생을 찾는 방법의 수      
    for key in counted.keys():
      print(key)
      print(counted[key])
      exit(0)
      
bfs(N)
      
'''
수빈이 위치 - N,
동생 위치 - K

수빈이의 위치 X,  
  걷는 경우 1초 뒤 X-1 or ㅌ+1
  순간이동의 경우 1초 후 2*X
  
BFS 최단 거리
수빈이가 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후?
가장 빠른 시간으로 찾는 방법 몇 가지?
'''