def solution(A, B, K):
    # write your code in Python 3.6
    plus = 1 if A % K == 0 else 0
    val = int((B - A) / K)+ plus
    return val