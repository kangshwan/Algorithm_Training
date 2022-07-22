N, S = map(int, input().split())
nums = list(map(int,input().split()))
pt1,pt2=0,0
sum=0
answer=100000001
while(pt1 < N):
    if sum >= S :
        wc = pt2-pt1
        answer = min(answer, wc)
        sum-=nums[pt1]
        pt1+=1
    else:
        if pt2==N:
            break
        sum+=nums[pt2]
        pt2+=1
    # print(f'pt1: {pt1}, pt2: {pt2}')
    # print('sum: ',sum)
if answer==100000001:
    print(0)
    exit(0)
print(answer)
'''
문제가 두 포인터 문제기 때문에,
조건인 S를 만족했을경우 pt1을 하나 증가시켰을 때도
조건 S를 만족하는지 확인하고, 그렇지 않다면 pt2를 증가시켜
총 200000번 만에 최소를 구하도록 작성.

'''
'''
아이디어 1
전수조사를 진행하는것.
--> how? 0 idx부터 연속찾고, 1 idx부터 연속 찾고...
N-1 idx부터 연속찾고...
--> N의 최장길이가 100000 (십만) 이고, 대략 계산해봐도 최악은 100000x100000 = 10000000000 (100억) 보다는 적게 나오겠지만..
--> 그래도 0.5초를 만족하려먼 적어도 5천만번 정도 계산을 해야 가능한것.
시간제한이 0.5초라 안될것같았는데
역시 시간초과가 났다.
'''