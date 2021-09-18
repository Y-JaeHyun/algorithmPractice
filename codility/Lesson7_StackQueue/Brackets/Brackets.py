def solution(S):
    # write your code in Python 3.6
    Slist = list(S)
    stack = []
    for s in Slist:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        else:
            if len(stack) == 0: return 0
            if s == '}':
                if stack.pop() == '{':
                    continue
                else:
                    return 0
            elif s == ']':
                if stack.pop() == '[':
                    continue
                else:
                    return 0
            elif s == ')':
                if stack.pop() == '(':
                    continue
                else:
                    return 0
    if len(stack) == 0: return 1
    else: return 0