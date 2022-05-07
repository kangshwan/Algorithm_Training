arr = [int(input()) for _ in range(9)]
# arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]
dwarf = []
exitBreak = True

for a in range(len(arr)):
    for b in range(a+1, len(arr)):
        for c in range(b+1, len(arr)):
            for d in range(c+1, len(arr)):
                for e in range(d+1, len(arr)):
                    for f in range(e+1, len(arr)):
                        for g in range(f+1, len(arr)):
                            if (arr[a]+arr[b]+arr[c]+arr[d]+arr[e]+arr[f]+arr[g]) == 100:
                                dwarf = [arr[a], arr[b], arr[c], arr[d], arr[e], arr[f], arr[g]]
                                exitBreak = False
                                break
                        if exitBreak == False:
                            break
                    if exitBreak == False:
                        break
                if exitBreak == False:
                    break
            if exitBreak == False:
                break
        if exitBreak == False:
            break
    if exitBreak == False:
        break
                            
dwarf.sort()
for i in dwarf: print(i)