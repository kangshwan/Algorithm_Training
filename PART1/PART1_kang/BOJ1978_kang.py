# 에라토네스의 체 이용
isPrime = [True]*1001
isPrime[0] = isPrime[1] = False
for num in range(2,1001):
    if isPrime[num]:
        for mult in range(num*2, 1001, num):
            isPrime[mult]=False
N=int(input())
ansList = list(map(int, input().split()))
answer=0
for ans in ansList:
    if isPrime[ans]:
        answer += 1
print(answer)