#BOJ1789_수들의합
import sys

s = int(sys.stdin.readline())
n, maxCount = 0, 0
i = 1

#200이 
while(n < s):
  n += i
  i += 1
  maxCount += 1
  
if n == s: print(maxCount)
else:
  for j in range(maxCount):
    if (n - j) == s: 
      maxCount -= 1
      print(maxCount)
