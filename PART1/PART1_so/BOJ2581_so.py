#소수 10000이상
m = int(input())
n = int(input())

def prime(k):
  cnt = 0
  for i in range(2, k+1):
    if (k%i ==0):
      cnt += 1
  if cnt ==1:
    return k
  else: return 0
  
prime_arr = []  
for elem in range(m, n+1):
  if prime(elem) != 0:
    prime_arr.append(prime(elem))

sum = 0
if len(prime_arr) == 0:
  print(-1)
else:
  for elem in prime_arr:
    sum += elem 
  print(sum)
  print(min(prime_arr))