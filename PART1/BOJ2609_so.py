#2609 최대공약수와 최소공배수
a, b = map(int, input().split())

def gcd(a, b):
  if a == 0: return b
  elif b == 0 : return a

  return gcd(b, a%b)

  
def lcm(a, b):
  if a == 0: return b
  elif b == 0 : return a
  
  return a*b/gcd(a,b)


print(gcd(a,b))
print(int(lcm(a,b)))