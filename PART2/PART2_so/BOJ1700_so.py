# # 멀티탭 스케줄링
# # 1. 콘센트가 비어있을 때
# # 콘센트에 이미 있을 떄
# # 2. 콘센트가 꽉 차있을 때
# # 3. 콘센트가 꽉 찼지만 이미 꽂혀져 있는 거일 때

n, k = map(int, input().split())
orderArr = list(map(int, input().split()))


plug = []
count = 0


for i in range(k):
    if orderArr[i] in plug: # 멀티탭에 이미 꽂혀있음
        continue 
      
    if len(plug) < n:  # 멀티탭에 구멍이 남아있을 때
        plug.append(orderArr[i])
        continue

    
    idx = 0 # 멀티탭에서 뺄 전기용품의 위치
    farN = 0 # 써야하는 전기 용품 중 가장 먼 것의 위치
    
    for j in range(n): #멀티탭에 전기용품 플러그를 바꿔줘야할 때
        if plug[j] not in orderArr[i:]: #남은 순서 중에 계속 써야하는 전기용품이 없을 때
            idx = j
            break
        else:
            if farN < orderArr[i:].index(plug[j]): #계속 써야하는 전기용품이 있을 때 
              farN = orderArr[i:].index(plug[j])
              idx = j
    plug[idx] = orderArr[i]
    count += 1
print(count)

