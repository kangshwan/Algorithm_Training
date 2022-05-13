# sumList = [0 for _ in range(46)]
# sumList[1] = 1
# for idx in range(2,46):
#     sumList[idx] = sumList[idx-1]+idx
# numList=[0 for _ in range(1001)]
# for num in range(1,46):
#     for i in range(sumList[num]-num+1, sumList[num]+1):
#         if(i > 1000):
#             break
#         numList[i]=num
# a,b = list(map(int,input().split()))
# answer=0
# for i in range(a,b+1):
#     answer += numList[i]
# print(answer)

numList=[0 for _ in range(1001)]
idx = 1
for num in range(1,46):
    for i in range(idx, idx+num):
        if(i > 1000):
            break
        numList[i]=num
    idx += num
a,b = list(map(int,input().split()))
answer=0
for i in range(a,b+1):
    answer += numList[i]
print(answer)
