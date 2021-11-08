#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort(reverse=True)
    for i in range (length):
        if citations[i] <= i:
            return i
    return length
