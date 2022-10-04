#BOJ13549_숨바꼭질3
from collections import defaultdict, deque

N, K = map(int,input().split())
max_size = 100001
visited = [False] * max_size
counted = defaultdict(int)

def bfs(start):
  q = deque()
  q.append([start,0])
  
  while q:
    cur, cnt = q.popleft()
    visited[cur] = True
    
    if cur == K: counted[cnt] += 1
    else: 
      if 0 <= cur + 1 < max_size and not visited[cur + 1]:
        q.append([cur + 1, cnt + 1])
      if 0 <= cur - 1 < max_size and not visited[cur - 1]:
        q.append([cur - 1, cnt + 1])
      if 0 <= cur * 2 < max_size and not visited[cur * 2]:
        q.append([cur * 2, cnt])
        
  ans = max_size
  for key in counted.keys():
    ans = min(ans, key)
  print(ans)
    
bfs(N)

'''
defaultdict()는 딕셔너리를 만드는 dict 클래스의 서브클래스
작동하는 방식은 거의 동일하지만, defaultdict()는 인자로 주어진 객체의 기본값을 딕셔너리 값의 초기값으로 지정할 수 있다.

defalutdict(int) - 디폴트 값이 int인 딕셔너리
값을 지정하지 않은 키는 그 값이 0으로 지정된다.


수빈이 - 1초뒤
  X-1
  X+1
  
  0초
  2*X

5-10-9-18-17 2초

수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후?

이전에 풀었던 것과 비슷하지만 2*X에서 0초이며 찾을 수 있는 가장 빠른 시간만 출력함 -> 가장 작은 key 값을 print
'''