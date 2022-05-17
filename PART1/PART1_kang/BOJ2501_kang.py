n, k = list(map(int,input().split()))
count=0
for div in range(1, n+1):
    if n % div == 0:
        count+=1
        if count==k:
            print(div)
            exit()
print(0)