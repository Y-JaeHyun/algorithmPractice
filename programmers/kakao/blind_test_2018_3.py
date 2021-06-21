#https://programmers.co.kr/learn/courses/30/lessons/17677

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
