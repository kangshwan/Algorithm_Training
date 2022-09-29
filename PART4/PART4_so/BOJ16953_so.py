#BOJ16953_A→B
from collections import deque

def bfs(start, end):
  q = deque([(start)])
  level, cnt = start, 1
  
  while q:
    x = q.popleft()
    
    if (x/2 == level):  #가장 왼쪽 것과 같으면 트리의 깊이가 바뀌었다는 것이므로 cnt + 1
      cnt += 1
      level = x
      
    if x == end: return cnt
    
    left = x * 2
    right = int(str(x) + '1')
    if left > end and right > end: continue #둘 다 조건이 아닐 때
    if left > end and right <= end: q.append(right) #left가 조건이 아닐 때
    elif left <= end and right > end: q.append(left) #right가 조건이 아닐 때
    else: #둘 다 조건일 때
      q.append(left)
      q.append(right)
      
  return -1

a,b = map(int, input().split())
print(bfs(a, b))  
  
'''
정수 A를 B로 바꾸는 법
1. 2를 곱한다
2. 1을 수의 가장 오른쪽에 추가한다.

연산의 최솟값은?

최소 값이니까 bfs 이용
'''