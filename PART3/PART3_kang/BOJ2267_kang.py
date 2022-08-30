from collections import deque
N = int(input())
map = [[0 for _ in range(N)]for _ in range(N)]
visited = [[False for _ in range(N)]for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for r in range(N):
    row = input()
    for idx, val in enumerate(row):
        val=int(val)
        map[r][idx]=val
        if not val:
            visited[r][idx]=True
answer=[]
def inRange(x,y):
    return 0<=x<N and 0<=y<N

def BFS(x,y):
    visCount=0
    queue = deque()
    queue.append((x,y))
    while queue:
        cx,cy = queue.popleft()
        if visited[cx][cy]:
            continue
        visited[cx][cy]=True
        visCount+=1
        for dir in range(4):
            nx=cx+dx[dir]
            ny=cy+dy[dir]
            if inRange(nx,ny) and not visited[nx][ny]:
                queue.append((nx,ny))
   
    return visCount

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            answer.append(BFS(x,y))
print(len(answer))
answer.sort()
for ans in answer:
    print(ans)