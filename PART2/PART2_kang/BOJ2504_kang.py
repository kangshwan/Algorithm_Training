brackets = input()
stack = []
tmp = 1
answer = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        tmp *= 2
        stack.append(brackets[i])
    elif brackets[i] == '[':
        tmp *= 3
        stack.append(brackets[i])
    elif brackets[i] == ')':
        if not stack or stack[-1] == '[':
            print(0)
            exit()
        if brackets[i-1]=='(':
            answer += tmp
        tmp //=2
        stack.pop()
    elif brackets[i] == ']':
        if not stack or stack[-1] == '(':
            print(0)
            exit()
        if brackets[i-1]=='[':
            answer += tmp
        tmp //=3
        stack.pop()
if stack:
    answer=0
print(answer)