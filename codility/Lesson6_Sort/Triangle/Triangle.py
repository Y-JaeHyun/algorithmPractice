def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(len(A)-2):
        P = A[i]
        Q = A[i+1]
        R = A[i+2]

        if P + Q > R:
            return 1
            
    return 0