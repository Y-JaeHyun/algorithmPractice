from math import gcd

def solution(N, M):
    return int(N/gcd(M,N))
