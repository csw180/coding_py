def solution(my_string):
    tokens = my_string.split(" ")
    stack = []
    op =""
    for token in tokens :
        if token in ["+","-"] :
            op = token
            print(f'stack={stack},op={op}')
            continue
        if token.isdigit() :
            if stack and op=="+":
                stack.append(stack.pop() + int(token))
            elif stack and op=="-":
                stack.append(stack.pop() - int(token))
            else :
                stack.append(int(token))
        print(f'stack={stack},op={op}')
    return stack[0]

print(solution("3 + 4"))
print(solution("7 - 2 + 5 - 3"))