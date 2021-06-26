#https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
from datetime import datetime, timedelta

def solution(lines):
    events = []
    i = 1
    for line in lines:
        splitData = line.split()
        endtime = datetime.strptime(' '.join(splitData[:2]),"%Y-%m-%d %H:%M:%S.%f")
        #events.append([endtime, 1, i])
        #deltaData = splitData[2][:-1].split('.')
        deltaData = splitData[2][:-1]
        #td = timedelta(seconds = int(deltaData[0]), milliseconds = int(deltaData[1]))
        td = timedelta(milliseconds = int(float(deltaData) * 1000)-1)
        starttime = endtime - td
        events.append([starttime, endtime, 2, i])
        i = i + 1

    events.sort()
    maxTraffic = 0
    currentTraffic = 0
    manageData = []

    for event in events:
        if currentTraffic == 0:
            currentTraffic = currentTraffic + 1
            manageData.append(event)
        else:
            td = timedelta(seconds = 1)
            beforeTime = event[0] - td
            manageData = [ md for md in manageData if md[1] > beforeTime ] 
            manageData.append(event)
            currentTraffic = len(manageData)

        if maxTraffic < currentTraffic:
            maxTraffic = currentTraffic
    return maxTraffic

if __name__ == '__main__':
    print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
