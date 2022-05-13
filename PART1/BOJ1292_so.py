n, k = map(int, input().split())

def easy(n, k):
  temp = []
  sum = 0
  for i in range(1, k+1):
    for j in range(1, i+1):
      temp.append(i)
  for w in temp[n-1:k]:
    sum += w
    
  return sum
  
print(easy(n, k))