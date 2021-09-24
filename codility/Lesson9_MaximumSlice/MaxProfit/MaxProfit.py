def solution(A):
    # write your code in Python 3.6

    if len(A) < 2:
        return 0
	
    minValue = A[0]
    ret = 0
    for a in A:
        temp = a - minValue
        if ret < temp:
            ret = temp
        if minValue > a:
            minValue = a

    return ret