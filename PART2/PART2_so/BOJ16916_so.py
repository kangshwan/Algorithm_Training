#부분 문자열

#접두사와 접미사의 최대 길이를 포함하고 있는 테이블을 만듬
def lps(pattern):
  pattern_size = len(pattern)
  table = [0] * pattern_size
  j = 0
  
  for i in range(1, pattern_size):
    #j는 0 이상일 때 i번째 문자와 j번째 문자가 일치하지 않을 때 j의 위치를 idx - 1 값으로 변경
    while j > 0 and pattern[i] != pattern[j]:
      j = table[j-1]
    #일치하면 현재 j 위치에 1을 더한 값이 i번째 idx 값으로 들어감. 그리고 i++ j++
    if pattern[i] == pattern[j]: 
      j += 1
      table[i] = j
      
  return table

def kmp(parent, pattern):
  table = lps(pattern)
  parent_size = len(parent)
  pattern_size = len(pattern)
  j = 0

  for i in range(parent_size):
    # 일치하지 않는 경우 발생하면 j를 이전 값이 있던 곳으로 현재 위치에서 -1 해줌
    while j > 0 and parent[i] != pattern[j]:
      j = table[j-1]
    #일치하는 경우
    if parent[i] == pattern[j]:
      #문자가 모두 매칭하는 경우! j가 P와 길이가 같을 때
      if j == pattern_size -1:
        return True
      else: j += 1 #매칭이 이뤄졌으니 j++
    
  return False 
 
S = input()
P = input()
 
if kmp(S, P): print(1)
else: print(0)










#부분 문자열 KMP(Knuth, Morris, Pratt) 알고리즘

'''
1. 일치하는 패턴의 길이: 본문과 찾으려는 패턴을 맨 앞에서부터 비교. 어느 지점에서 불일치 발생 -> 그 직전까지 일치하는 패턴의 길이
2. 최대 경계 너비: 본문과 패턴 간에 일치하는 부분에서 경계를 찾고, 그들 중 최대의 길이 값

이동거리 = 일치하는 패턴의 길이 - 최대 경계 너비

lps = 접두사와 접미사가 같을 때 그 최대 길이를 가지고 있는 테이블

'''