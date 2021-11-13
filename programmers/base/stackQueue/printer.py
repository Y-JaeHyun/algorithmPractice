#https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    priority = max(priorities)
    
    while True:
        now = priorities.pop(0)
        if now == priority:
            answer += 1
            if location == 0:
                break;
            location -= 1
            priority = max(priorities)
        else:
            priorities.append(now)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer
