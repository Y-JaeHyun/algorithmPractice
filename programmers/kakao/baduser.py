#https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import permutations 

def solution(user_id, banned_id):
    banPattern = []
    answer = []

    for banId in banned_id:
        patternString = banId.replace("*", "[a-zA-Z0-9]")
        banPattern.append(re.compile(patternString))

    for candidateCheck in permutations(user_id, len(banned_id)):
        check = True
        for i in range(0, len(candidateCheck)):
            if len(candidateCheck[i]) != len(banned_id[i]):
                check = False
                break 
            match = banPattern[i].match(candidateCheck[i])
            if match == None:
                check = False
                break

        if check == False:
            continue
        
        banSet = set(candidateCheck)
        if banSet not in answer:
            answer.append(banSet)

    return len(answer)

if __name__ == "__main__":
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
