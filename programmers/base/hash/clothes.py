#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothDict = {}

    for value, key in clothes:
        if key in clothDict:
            clothDict[key] += 1
        else:
            clothDict[key] = 1
    answer = 1

    for value in clothDict.values():
        answer *= (value + 1)

    return answer -1
