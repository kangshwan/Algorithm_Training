T = int(input())
for _ in range(T):
    len=0
    num=int(input())
    answer=[]
    while num!=1 :
        if num%2 == 1:
            answer.append(len)
        num=num//2
        len+=1
    answer.append(len)
    for num in answer:
        print(num,end=" ")
    print()