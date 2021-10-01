# O(N**2) 수정 필요

from collections import Counter

def solution(A):
    count = Counter(A)
    d = dict()
    length = len(A)
    val = [0] * length
    key = count.keys()

    for i in range (length):
        if A[i] in d:
            val[i] = d[A[i]]
        else:
            # 이쪽 로직 수정 필요
            temp = 0
            for k in key:
                if A[i] % k != 0:
                    temp += count[k]
            
            val[i] = temp
            d[A[i]] = temp
    return val