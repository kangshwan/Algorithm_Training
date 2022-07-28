# Prim 알고리즘을 이용한 MST(Minimum Spanning Tree) 찾기
V,E=map(int,input().split())
# union-find를 사용하기 위한 root 변수 설정
root = [i for i in range(V)]
edges=[]
for _ in range(E):
    a, b, c = map(int,input().split())
    edges.append((a-1,b-1,c))
# edge들을 weight 순서대로 오름차순 정렬
edges = sorted(edges, key = lambda x:x[2])

# union-find를 통해서 cycle 생성하는지 판단
def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])
def union(x, y):
    x,y = find(x), find(y)
    root[y]=x

answer = 0
for edge in edges:
    a,b,c = edge
    # union-find에서 find의 결과가 같다면->부모가 같다->cycle생성됨
    # union-find에서 find의 결과가 같지 않다면->부모가 다르다->cycle생성X
    if find(a) != find(b):
        answer += c
        union(a,b)
print(answer)