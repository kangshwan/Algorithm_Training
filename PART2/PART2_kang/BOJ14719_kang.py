H,W = map(int, input().split())

world =[[0 for _ in range(W)]for _ in range(H)]

blocks = list(map(int, input().split()))
for w in range(W):
    n = blocks[w]
    for h in range(H-n, H):
        world[h][w] = 1

def in_range(y):
    return 0<=y<W

# fill the water
answer=0
for h in range(H):
    waterCount = 0
    bStart=False
    for w in range(W):

        # if meet block
        if world[h][w]:
            # if already started
            if bStart:
                # if already water is filled
                if waterCount:
                    bStart=False
                    answer+=waterCount
                    waterCount=0
                # but next is empty
                if in_range(w+1) and not world[h][w+1]:
                    bStart = True
            else:
                if in_range(w+1) and not world[h][w+1]:
                    bStart = True
        else:
            if bStart:
                waterCount+=1        
print(answer)