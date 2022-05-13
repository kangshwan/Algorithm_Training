# 에라토네스의 체 이용
isPrime = [True]*10001
isPrime[0] = isPrime[1] = False
for num in range(2,10001):
    if isPrime[num]:
        for mult in range(num*2, 10001, num):
            isPrime[mult]=False
a = int(input())
b = int(input())
answer=0
count=0
minVal=10001
for i in range(a, b+1):
    if isPrime[i]:
        answer += i
        count  += 1
        minVal = min(minVal,i)

if count:
    print(answer)
    print(minVal)
else:
    print(-1)