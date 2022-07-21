# 빗물
h, w = map(int, input().split())
arr = list(map(int, input().split()))

m = [[1] * w for _ in range(h)]
temp = [] #왼쪽의 벽 가로 좌표와 오른쪽에 존재하는 벽 가로 좌표 저장
count = 0

#벽이 아닌 부분을 0으로
for i in range(len(arr)):
    depth = h - arr[i]
    for j in range(depth):
        m[j][i] = 0

for h1 in range(h-1, -1, -1):
    for w1 in range(w):
        if m[h1][w1] == 1: #벽일 경우 temp에 가로 좌표를 저장
            temp.append(w1)
            if len(temp) == 2: #오른쪽에 벽이 존재할 경우 검사
                if temp[1] - temp[0] == 1: #벽이 붙어있는 경우 왼쪽 벽을 없애고 진행
                    temp = [temp[1]]
                else: #빗물이 고이는 부분을 2로 적고 count 올림
                    for t in range(temp[0] + 1, temp[1]): 
                        m[h1][t] = 2
                        count += 1
                    temp = [temp[1]]
    temp = []
    
print(count)
