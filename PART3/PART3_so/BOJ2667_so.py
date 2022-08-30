#BOJ2667_단지번호붙이기

n = int(input())
grid = []

for _ in range(n):
  string = input()
  grid.append(list(map(int,string)))

visited = [[False for _ in range(n)] for _ in range(n)]

town = 0
towns = []

#주어진 위치가 격자를 벗어나는지 여부를 반환
def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

#주어진 위치로 이동할 수 있는지 여부를 확인
def can_go(x,y):
  if not in_range(x,y): #격자 안인지
    return False
  if visited[x][y] or grid[x][y] == 0: #이미 방문했는지
    return False
  
  return True 
 
def dfs(x,y):
  global town
  dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
  
  for dx, dy in zip(dxs, dys):
    new_x, new_y = x + dx, y + dy
    
    if can_go(new_x, new_y):
      visited[new_x][new_y] = True
      town += 1
      dfs(new_x, new_y) #깊이 탐색


#격자의 각 위치에서 탐색을 시작할 수 있는 경우
#한 마을에 대한 DFS 탐색 수행
for i in range(n):
  for j in range(n):
    if can_go(i, j):
      # 해당 위치 방문할 수 있으면 visited 배열 갱신
      # 새로운 마을을 탐색한다는 의미로 town 1로 갱신
      visited[i][j] = True
      town = 1
      
      dfs(i, j)
      
      towns.append(town) #오름차순 시킬 단지 수

towns.sort()

print(len(towns))

for elem in range(len(towns)):
  print(towns[elem])
      
        
        
'''
  4
1   3
  2
'''
    