
def solution(S, P, Q):
    # write your code in Python 3.6
    
    val = []

    for i in range (len(P)):
        start = P[i]
        end = Q[i]
        num = 0
        if 'A' in S[start:end+1]:
            val.append(1)
        elif 'C' in S[start:end+1]:
            val.append(2)
        elif 'G' in S[start:end+1]:
            val.append(3)
        elif 'T' in S[start:end+1]:
            val.append(4)

    return val
	