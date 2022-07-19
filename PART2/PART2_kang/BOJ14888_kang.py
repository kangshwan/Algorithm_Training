n = int(input())
nums = list(map(int,input().split()))
op = list(map(int, input().split()))
largest  = -1000000000
smallest = 1000000000

def solution(numIdx, calcResult):
    global largest, smallest
    if numIdx == n:
        if largest < calcResult:
            largest = calcResult
        if smallest > calcResult:
            smallest = calcResult
        return
        
    for opIdx in range(4):
        # op[opIdx]가 0이상이면
        if op[opIdx]:
            if opIdx == 0:
                nextNum = calcResult + nums[numIdx]
            elif opIdx == 1:
                nextNum = calcResult - nums[numIdx]
            elif opIdx == 2:
                nextNum = calcResult * nums[numIdx]
            else:
                nextNum = int(calcResult / nums[numIdx])
            op[opIdx] -= 1
            solution(numIdx+1, nextNum)
            op[opIdx] += 1

solution(1, nums[0])
print(f'{largest}\n{smallest}')