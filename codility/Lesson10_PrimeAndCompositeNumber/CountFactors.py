def solution(N):
    candidate = 1
    result = 0
    while candidate ** 2 < N:
        if N % candidate == 0:      
          result += 2

        candidate += 1

    if candidate ** 2 == N:  result += 1

    return result