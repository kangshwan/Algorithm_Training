# N = int(input())
# nums = list(map(int, input().split()))
# print(f"{min(nums)} {max(nums)}")

N = int(input())
nums = list(map(int, input().split()))
min = 1000001
max = -1000001
for num in nums:
    if max < num:
        max = num
    if min > num:
        min = num
print(f'{min} {max}')

'''
comment
혹시나 해서 내장 함수 사용이 아닌 정석 풀이를 해봤는데
더 오래걸리고 메모리도 많이쓰는 결과를 얻었다..
'''