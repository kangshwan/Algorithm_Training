S = input()
P = input()
lS = len(S)
lP = len(P)
# Pi table 생성
Pi = [0 for _ in range(lP)]
lenLPS = 0 
idx = 1
while idx < lP:
    # 현재 패턴과 텍스트가 매칭이 되었다면
    if P[idx] == P[lenLPS]:
        lenLPS+=1
        Pi[idx]=lenLPS
        idx+=1
    else:
        # 패턴과 텍스트가 매칭이 안되었다면
        if lenLPS != 0:
            lenLPS = 0
            # lenLPS 초기화. 매칭을 처음부터 다시 시작한다.
            
        else: # 탐색할 문자열이 처음 인덱스로 돌아왔을 경우이며, 이미 매칭도 실패한 경우
            Pi[idx]=0
            idx+=1
cmpIdx=0
idx=0
while cmpIdx < lS:
    if P[idx] == S[cmpIdx]:
        idx+=1
        cmpIdx+=1
    else:
        if idx != 0:
            idx = Pi[idx-1]
        else:
            cmpIdx+=1
    if idx == lP:
        print(1)
        exit(0)
print(0)

'''
키포인트는 조건문을 틀렸을때 분기하는것이 아닌 맞았을때 분기를 기준으로 하는것이 더 좋다는것.
'''

#유기
# # 중복되는 문자 개수 탐색
# # P[:lP/2]와 P[lP/2:를 매칭하여 매칭이 끝났을 경우 최대 길이를 탐색
# matchIdx=lP//2
# matchlen=0
# while matchIdx < lP:
#     for i in range(lP//2):
#         if matchIdx+i >= lP:
#             # 이는 즉 끝까지 매칭이 끝났다는 것을 의미하므로,
#             # 접미사를 찾은 경우를 의미한다.
#             matchIdx=lP
#             break    
#         if P[matchIdx+i] != P[i]:
#             matchlen=0
#             break
#         matchlen+=1
#     matchIdx+=1


# cmpIdx=0
# match=True
# while cmpIdx < lS:
#     match=True
#     # print('\nnextmatch!')
#     for i in range(lP):    
#         if cmpIdx+i >= lS:
#             print(0)
#             exit(0)
#         # print(f'cmpIdx+i: {cmpIdx+i}, i: {i}')
#         # print(f'S[cmpIdx+i]:{S[cmpIdx+i]}, P[i]={P[i]}')
#         if S[cmpIdx+i] != P[i]:
#             if i <= matchlen:
#                 cmpIdx -= i
#             elif lP-i <= matchlen:
#                 cmpIdx -= lP-i
#             cmpIdx+=i
#             match=False
#             break
#     if match:
#         print(1)
#         exit(0)
#     cmpIdx+=1
# print(0)
'''
아래 처럼 생각 전개를 했으나 28%에서 시간초과 오류가 발생.
따라서 KMP알고리즘에 대해 검색함.
Pi 배열 또는 LPS(Longest proper Prefix which is Suffix) 배열을 생성하고,
여기서 중복되는 접미사와 접두사를 찾아 나선다.
이는 중복되는 접미사 접두사를 찾을 뿐 아니라, mismatch가 났을 경우 어디에서부터 다시 시작하면 되는지도 나타낸다.
예를들어
ABCCCAB 라는 문자열의 Pi배열을 알고자 할 경우
ABCCCAB와 ABCACAB를 매칭시켜 중복되는부분이 어딘지 발견한다.
Pi = [0, 0, 0, 0, 0, 0, 0] 로 초기화 해주고,
Pi[0]는 항상 0이다. 각 인덱스는 문자열 ABCCAB에서 인덱스까지의 부분 문자열을 의미하고,
Pi[idx]는 idx까지의 부분 문자열에서 LPS값을 나타낸다.
Pi[0]에서 idx 0 까지의 부분 문자열은 A이고, 접미사와 접두사가 없으므로 0이다.
Pi[1]에서 idx 1 까지의 부분 문자열은 AB이고, 접미사와 접두사가 다르므로 0이다.
...
Pi[3]에서 idx 3 까지의 부분 문자열은 ABCA이고, 접미사와 접두사 A가 일치하므로 1이다.
Pi[4]에서 idx 4 까지의 부분 문자열은 ABCAC이고, 접미사와 접두사가 일치하지 않으므로 0이다.
Pi[5]에서 idx 5 까지의 부분 문자열은 ABCACA이고, 접미사와 접두사 A가 일치하므로 1이다.
Pi[6]에서 idx 6 까지의 부분 문자열은 ABCACAB이고, 접미사와 접두사 AB가 일치하므로 2이다.

위처럼, 접미사와 접두사가 일치하면 매칭하는 ABCACAB를 하나씩 증가시켜 매칭하고, 그렇지 않다면 하나 줄여서 재 매칭한다.

예를들면
0123456789
ABCABCBABC는
leng=4
Pi[6] ABCABCB
Pi = [0, 0, 0, 1, 2, 3, 0, 1, 2, 3]

'ABCABABC'
는 
Pi = [0, 0, 0, 1, 2, 1, 2, 3] 로 나오게 될 것이다.
결국 Pi 배열은 문자를 매칭하다가 틀렸을 경우, 어디서 부터 다시 매칭하면
될 것인가? 를 알려준다.
예를들어
ABCABCABCABCABABC와 매칭한다고 할 경우
i=5에서, lenLPS=2인상태이고,
ABCAB..까지는 매칭 되었으나 A와 C가 달라 매칭이 실패한다.
lenLPS = Pi[2-1]=Pi[1]=0
여기서 Pi[5] = 2이므로, 문자열에서 C부터 매칭을 시작해도 된다는 뜻이다
보는바와 같이

으로 나오게 될 것이다.
'''


# 생성한 예외 ex
'''
abccabcccaabcccab
abcccab
1

aabbcccabb
abbcccabb
1

ababccab  
abccab
1

P의 맨앞과 맨뒤 문자가 같을 경우에 예외가 생길 수 있음.
따라서 P의 앞과 맨뒤 문자 (접두사, 접미사)가 얼마까지 같은지를 파악한 후, 
그 길이만큼을 다시 빼 주어서 검색해야함.


nextmatch!
S[cmpIdx+i]:a, P[i]=a
S[cmpIdx+i]:b, P[i]=b
S[cmpIdx+i]:c, P[i]=c
S[cmpIdx+i]:c, P[i]=c
S[cmpIdx+i]:c, P[i]=c
S[cmpIdx+i]:a, P[i]=a
cmpIdx+i: 12, i: 6
S[cmpIdx+i]:a, P[i]=b

nextmatch!
cmpIdx+i: 13, i: 0
S[cmpIdx+i]:b, P[i]=a

cmpIdx = 6, i = 6에서 오류가 났음.
lP-i = 7-6 = 1, 1은 앞, 뒤 중복되는 문자 개수인 2보다 작으므로
1만큼 뒤로 가주어야 한다.
그렇다면 cmpIdx=12 부터 재 검사를 시작하는 것이다.
위에서는 12가 아닌 13부터 재검사를 하고 있기 때문에 매칭에 실패한다.

aabbcccabb
abbcccabb
의 경우처럼, 앞에서 다시 검사를 해야 할 경우도 있다.
i가 중복되는 문자 개수인 3보다 작기 때문에,
i만큼 뒤로 가주고 재검사를 실시하는것이다.

답은 1이 나와야함
'''