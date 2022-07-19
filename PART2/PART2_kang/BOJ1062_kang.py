N, K = map(int,input().split())
essentialWord = ['a','c','n','t','i']
# knowledge is for bruteforce
knowledge = [False for _ in range(26)]
fixVisit = [ord('a')-97, ord('c')-97, ord('i')-97, ord('n')-97, ord('t')-97]
# print(fixVisit)
for i in fixVisit:
    knowledge[i]=True
if K < 5:
    print(0)
    exit(0)
essentialBit = 0
for w in essentialWord:
    essentialBit += 2**(ord(w)-97)
# print(essentialBit)
# print(bin(essentialBit))
wordDict = []
for wdict in range(N):
    word = set(list(input()))
    tobit=0
    for w in word:
        tobit += 2**(ord(w)-97)
    wordDict.append(tobit)

maxNum = K-5
answer = 0
def bruteForce(idx, step):
    global knowledge
    global wordDict
    global answer
    if step == maxNum:
        # print('\n\nreached max step!!!')
        wordCount=0
        knowledgeBit = 0
        for idx, flag in enumerate(knowledge):
            if flag:
                knowledgeBit += 2**idx
        # print(bin(knowledgeBit))
        
        for word in wordDict:
            # print('words')
            # print(bin(word))
            # print(bin(knowledgeBit&word))
            if word == knowledgeBit & word:
                wordCount+=1
        # print(wordCount)
        answer = max(answer, wordCount)
        return
    for i in range(idx, 26):
        if knowledge[i]:
            continue
        else:
            knowledge[i] = True
            bruteForce(i+1,step+1)
            knowledge[i] = False
bruteForce(1, 0)
print(answer)