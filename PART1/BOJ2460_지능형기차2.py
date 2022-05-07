countL = []
count = 0
for _ in range(10):
    outN, inN = list(map(int, input().split()))  # 내린 사람, 탄 사람
    count = count - outN + inN
    countL.append(count)

maxN = countL[0]

for i in countL:
    if i > maxN:
        maxN = i

print(maxN)
