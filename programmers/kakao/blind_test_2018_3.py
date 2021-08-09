#https://programmers.co.kr/learn/courses/30/lessons/17677
import re
import math

def solution2(str1, str2):
        str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
        str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

        gyo = set(str1) & set(str2)
        hap = set(str1) | set(str2)

        if len(hap) == 0 :
            return 65536

        gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
        hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

        return int((gyo_sum/hap_sum)*65536)




def solution(str1, str2):
    slice1 = []
    slice2 = []
    union = []
    intersection = []
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(0, len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha() == True:
            slice1.append(tmp)

    for i in range(0, len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha() == True:
            slice2.append(tmp)

    if len(slice1) == 0 and len(slice2) == 0:
        answer = 1
    else :
        for item in slice1:
            if item in slice2:
                intersection.append(item)
                slice2.remove(item)

        union.extend(slice1)
        union.extend(slice2)

        answer = len(intersection) / len(union)

    answer = int(answer * 65536)
    return answer

if __name__ == '__main__':
    print(solution('FRANCE', 'french'))
    print(solution('handshake', 'shake hands'))
    print(solution('aa1+aa2', 'AAAA12'))
    print(solution('E=M*C^2', 'e=m*c^2'))

    print(solution2('FRANCE', 'french'))
    print(solution2('handshake', 'shake hands'))
    print(solution2('aa1+aa2', 'AAAA12'))
    print(solution2('E=M*C^2', 'e=m*c^2'))
