from itertools import combinations
N = int(input())
# 9876543210 이 최대 9876543210

# [0,1,2,3,4,5,6,7,8,9]에서 1개 뽑았을때, 2개뽑았을때, ... , 10개 뽑았을때 값들을 구하면 전체 감소하는 수를 구할수 있지.
# 2^10-1=1023개 (전체 감소하는 수 개수) --> 1023개만 구하면 해결됨
num = [0,1,2,3,4,5,6,7,8,9]
numlist = []
for i in range(1,11):
    for sub in list(combinations(num,i)):
        sub=list(sub)
        sub.sort(reverse=True)
        numlist.append(int(''.join(str(e)for e in sub)))
        # numlist.append(sub)
numlist.sort()
if N >= 1023:
    print(-1)
else:
    print(numlist[N])