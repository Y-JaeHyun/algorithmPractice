def solution(A):
    # write your code in Python 3.6
    dic = {}
    half = len(A)/2

    for i in range(len(A)):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
        if dic[A[i]] > half:
                return i
    return -1