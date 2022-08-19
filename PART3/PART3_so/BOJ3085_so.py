#BOJ3085_사탕 게임
n = int(input())
m = []
for _ in range(n):
  string = input()
  m.append(list(string))
  
def maxCandy(arr): #candy의 최대 개수를 구함
  max_val = 1
  
  for i in range(len(arr)): 
    cnt = 1
    for j in range(1, len(arr)):
      if arr[i][j] == arr[i][j-1]: cnt += 1
      else: cnt = 1
      
      if cnt> max_val: max_val = cnt

    cnt = 1
    
    for j in range(1, len(arr)):
      if arr[j][i] == arr[j-1][i]:
        cnt += 1
      else: cnt = 1
      if cnt > max_val: max_val = cnt  
      
  return max_val

def changeCandy(m):
  ans = 0
  
  for i in range(len(m)):
    for j in range(len(m)):
      
      if j+1 < n:
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
        temp = maxCandy(m)
        if temp > ans: ans = temp
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
      
      if i+1 < n:  
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
        temp = maxCandy(m)
        if temp > ans: ans = temp
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]        
  
  print(ans)

changeCandy(m)  
'''
0 처음 NxN 에서의 최대 개수 구하기

0 temp 에 NxN 복사

0이후 인접 두 칸 같은지 아닌지 확인
같음? pass, 다름? temp 바꿈

바뀌면 바뀐 상태에서 temp에서 최대 개수 검사
최대 개수가 이전꺼보다 크면 바꿈.


이후 temp 다시 NxN으로 초기화
'''