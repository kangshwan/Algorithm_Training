count = 0
n = int(input())
k = list(map(int, input().split()))


def prime(k):
    global count
    temp = 0
    for i in range(2, k+1):
        if (k % i) == 0:
            temp += 1
    if temp == 1:
        count += 1


for elem in k:
    prime(elem)

print(count)
