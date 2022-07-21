# 연산자 끼워넣기
import sys

n = int(input())
an = list(map(int, input().split()))
ns = list(map(int, input().split()))

# 최대값 최소값 초기화
minN, maxN = sys.maxsize, -sys.maxsize


def dfs(depth, an, plus, minus, multi, div, result):
    global minN, maxN

    if depth == len(an) - 1:
        maxN = max(maxN, result)
        minN = min(minN, result)
        return

    if plus > 0:
        dfs(depth + 1, an, plus - 1, minus, multi, div, result + an[depth+1])
    if minus > 0:
        dfs(depth + 1, an, plus, minus - 1, multi, div, result - an[depth+1])
    if multi > 0:
        dfs(depth + 1, an, plus, minus, multi - 1, div, result * an[depth+1])
    if div > 0:
        dfs(depth + 1, an, plus, minus, multi, div - 1, int(result / an[depth+1]))


dfs(0, an,  ns[0], ns[1], ns[2], ns[3], an[0])
print(maxN)
print(minN)