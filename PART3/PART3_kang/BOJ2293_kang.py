n,k = map(int, input().split())
dp = [0]*100001
coins=[]
for _ in range(n):
    coins.append(int(input()))
dp[0]=1
for coin in coins:
    for price in range(coin, k+1):
        dp[price]+=dp[price-coin]
print(dp[k])