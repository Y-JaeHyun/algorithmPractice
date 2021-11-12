#https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

import math

def solution(progresses, speeds):
    answer = []
    jobs = []

    for i in range(len(progresses)):
        jobs.append(int(math.ceil((100.0 - progresses[i]) / speeds[i])))

    priority = jobs[0]
    count = 1
    for i in range(1, len(jobs)):
        if priority >= jobs[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            priority = jobs[i]

    answer.append(count)


    return answer
