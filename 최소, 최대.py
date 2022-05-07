def Qsort(A):
    if len(A) <= 1: return A
    p = A[0]
    S, M, L = [], [], []

    for i in A:
        if i < p: S.append(i)
        elif i > p: L.append(i)
        elif i == p: M.append(i)

    return Qsort(S) + M + Qsort(L)
    
N = int(input())
L = list(map(int, input().split()))

L= Qsort(L)
print(L[0], L[-1])