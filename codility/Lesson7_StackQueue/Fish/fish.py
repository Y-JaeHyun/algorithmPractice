def solution(A, B):
    # write your code in Python 3.6

    stack = []
    ret = 0

    for i in range(len(A)):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            if len(stack) == 0:
                ret += 1
        else:
            stack.append(A[i])
    ret += len(stack)
    return ret