def div(n, k):
    temp = []
    for i in range(1, n+1):
        if(n%i==0):
            temp.append(i)
    if len(temp) >= k:
        return temp[k-1]
    else: return 0


n, k = map(int, input().split())
print(div(n, k))