
#https://programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


def solution(dartResult):

    scores = []
    num = ''

    for i in range (0, len(dartResult)):
        if dartResult[i].isdigit() == True:
            num += dartResult[i]
        else:
            if dartResult[i] == 'S':
                score = int(num)
                num = ''
                scores.append(score)
            elif dartResult[i] == 'D':
                score = int(num)
                num = ''
                score = score ** 2
                scores.append(score)
            elif dartResult[i] == 'T':
                score = int(num)
                num = ''
                score = score ** 3
                scores.append(score)
            elif dartResult[i] == '*':
                length = len(scores)
                if length == 1:
                    scores[length -1] = scores[length -1] * 2
                else:
                    scores[length -1] = scores[length -1] * 2
                    scores[length -2] = scores[length -2] * 2
            elif dartResult[i] == '#':
                length = len(scores)
                scores[length -1] = scores[length -1] * -1
                

    answer = sum(scores)
    print(answer)
    return answer

if __name__ == "__main__":
    solution("1S2D*3T")
    solution("1D2S#10S")
    solution("1D2S0T")
    solution("1S*2T*3S")
    solution("1D#2S*3S")
    solution("1T2D3D#")
    solution("1D2S3T*")
    print(solution2("1S2D*3T"))
    print(solution2("1D2S#10S"))
    print(solution2("1D2S0T"))
    print(solution2("1S*2T*3S"))
    print(solution2("1D#2S*3S"))
    print(solution2("1T2D3D#"))
    print(solution2("1D2S3T*"))

