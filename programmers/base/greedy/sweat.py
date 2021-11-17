#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)
    
    for rev in reserveSet:
        if rev - 1 in lostSet:
            lostSet.remove(rev - 1)
        elif rev + 1 in lostSet:
            lostSet.remove(rev + 1)
    
    return n - len(lostSet)
