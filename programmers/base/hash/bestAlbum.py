#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    totalDict = {}
    detailDict = {}
    for i in range(len(genres)):
        if genres[i] in totalDict:
            totalDict[genres[i]] += plays[i]
            detailDict[genres[i]].append((i, plays[i]))
        else:
            totalDict[genres[i]] = plays[i]
            detailDict[genres[i]] = [(i, plays[i])]
    
    totalSort = sorted(totalDict.items(), key = lambda x: x[1], reverse = True)
    
    for genre, value in totalSort:
        candidate = sorted(detailDict[genre], key = lambda x: x[1], reverse = True)
        
        for idx, play in candidate[:2]:
            answer.append(idx)
    return answer
