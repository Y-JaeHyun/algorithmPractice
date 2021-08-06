#https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
#-*-coding:utf-8-*-

def solution(record):
    answer = []
    d = dict()

    behavior = []

    for r in record:
        r = r.split()
        if r[0] == "Enter":
            d[r[1]] = r[2]
            behavior.append([1, r[1]])
        elif r[0] == "Leave":
            behavior.append([2, r[1]])
        elif r[0] == "Change":
            d[r[1]] = r[2]

    for b in behavior:
        string = str(d[b[1]]) + "님이 "

        if b[0] == 1:
            string += "들어왔습니다."
        else:
            string += "나갔습니다."

        answer.append(string)        

    return answer

if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
