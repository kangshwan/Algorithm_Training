N, K = map(int, input().split())
items = list(map(int, input().split()))

# 전기용품 이름은 자연수 이므로.. 0으로 pluged초기화
pluged=[]
# 플러그에 꽂힌 전자기기를 뺄 때, 가장 멀리 있는 용품을 빼기 위함.
dist=[100 for _ in range(N)]
answer = 0
for idx, item in enumerate(items):
    # 초기 플러그 채우기
    if len(pluged) < N:
        if item not in pluged:
            pluged.append(item)
    # 플러그가 다 찼다면 이제 뽑기
    else:
        # item이 플러그에 꽂혀있다면
        if item in pluged:
            continue
        # item이 꽂혀 있지 않다면, 현재 시점부터 가장 나중에 다시사용되는 전자기기 제거
        else:
            for pIdx, pItem in enumerate(pluged):
                for i in range(idx+1, K):
                    if items[i] == pItem:
                        dist[pIdx]=i-idx
                        break
            print("pluged:\t",pluged)
            print("dist: \t",dist)
            plugOutIdx=0
            maxDist=-1
            for pIdx, pDist in enumerate(dist):
                if pDist>maxDist:
                    plugOutIdx = pIdx
                    maxDist=pDist
                # 체크 후에 dist초기화
                dist[pIdx]=100
            
            pluged[plugOutIdx]=item
            print("after:\t",pluged)
            print()
            answer += 1
print(answer)


    

'''
세번째 아이디어
새로 꽂을것이 들어왔을 경우, 다시 사용하기까지 가장 오래걸리는 전자기기 제외.
'''
'''
두번째 아이디어 폐기-단순 사용횟수로 뽑는 경우 최소시간이 나오지 않는다.
모든 사용 기기의 사용 횟수를 기록하고, 사용횟수가 적게 남은것부터 제외.
'''
'''
초기 아이디어 - 폐기. 2 3 1 7 4 2 로 주어지고, N=2인경우 아래 처럼 진행하면 횟수가 4가나옴.
최소 횟수는 3이다.

처음 N 개의 item은 일단 플러그에 꽂혀있다.
greedy하게 접근하여, N+1개째가 들어 왔을 경우에, N+N개까지 확인하여 포함되지 않는 플러그를 제거한다.
ex) N = 3, items = 1, 2, 3, 4, 1, 2
pluged = 1, 2, 3
next = 4
next에서 + 3 번째 이내에 다시 사용을 하고 있다면 제외하지 않는다.
next+1 = 1, next+2 = 2, next+3 = outOfRange
따라서 3이 제거가 되고, 4가 채워진다.
pluged = 1, 2, 4
그 다음 순서인 1, 2 는 이미 존재하므로, 플러그에서 뽑은 횟수는 1.
ex2) N=2, items = 2, 3, 2, 3, 1, 2, 7
pluged = 2, 3
idx=3까지는 이미 존재하므로 그냥 진행됨.
next = 1에서, next+1 = 2, next+2 = 7
pluged에서 2는 존재하므로, 3이 제외됨
pluged = 2, 1
이후 next = 2, pluged에 있으므로 진행.
next = 7에서, 2, 1 둘다 next+N안에 없으므로 앞에 있는것을 제외
pluged = 7, 1
따라서 빼는 횟수 : 2
'''

'''
test case
3 6
1 2 3 4 1 2
ans: 1

test case
4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
ans: 4
'''