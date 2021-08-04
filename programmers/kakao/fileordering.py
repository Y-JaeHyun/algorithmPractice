#https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    regex = re.compile("([a-zA-Z\-\.\ ]+)([0-9]+)")
    splitFiles = []
    sortedFiles = []
    answer = []
    index = 0

    for fileName in files:
        match = regex.search(fileName)
        splitFiles.append([match.group(1).lower(), int(match.group(2)), index])
        index += 1


    splitFiles.sort()

    
    temp = []
    for i in range (0, len(splitFiles)):
        temp.append(splitFiles[i])
        if i == len(splitFiles)-1 or splitFiles[i][0] != splitFiles[i+1][0]:
            temp = sorted(temp, key = lambda x : x[1])
            sortedFiles.extend(temp)
            temp = []

    for t in sortedFiles:
        answer.append(files[t[2]])

    return answer

            

if __name__ == '__main__':
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))


    
