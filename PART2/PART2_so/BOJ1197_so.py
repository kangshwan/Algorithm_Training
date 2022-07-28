#최소 스패닝 트리
import sys

V, E = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
arr.sort(key=lambda x: x[2]) #가장 뒤에 있는 가중치의 값으로 오름차순 정렬

uf = [i for i in range(V+1)] #union-find. 부모루트를 담음

def kruskal():
  global V, E, arr, uf
  mst = 0 #최소 스패닝 트리의 가중치를 담음
  
  for u, v, w in arr:
    A = find(u)
    B = find(v)
    if A != B: #사이클이 돌면 안 됨
      if A > B: uf[A] = B #union함수의 역할
      else: uf[B] = A
      mst += w
  return mst
      
def find(x): # x 노드가 포함된 집단의 루트 노드를 찾음. 그 집단의 대표 번호
  global uf
  if uf[x] == x: 
    return x
  return find(uf[x])

print(kruskal())
  
    
  
  
'''
최소 스패닝 트리 = 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

1 크루스칼 알고리즘 이용


- 시간초과 코드 (union함수의 역할을 크루스칼 for문에서 직접 해결. 재귀 x)

#최소 스패닝 트리
import sys

V, E = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
arr.sort(key=lambda x: x[2])

uf = [i for i in range(V+1)] #union-find

def kruskal():
  global V, E, arr, uf
  mst = 0 #최소 스패닝 트리의 가중치를 담음
  
  for u, v, w in arr:
    if find(u) != find(v):
      mst += w
      union(u, v)
  return mst
      
      
def union(x, y):
  global uf
  X, Y = find(x), find(y)
  uf[X] = Y
  
def find(x):
  global uf
  if uf[x] == x: 
    return x
  return find(uf[x])

print(kruskal())
'''