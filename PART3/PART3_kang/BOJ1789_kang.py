S = int(input())
n,sumN=1,0
while True:
    sumN+=n
    if sumN>S:
        print(n-1)
        break
    n+=1