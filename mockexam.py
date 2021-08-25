
#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    answerValue = [0,0,0]

    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    for i in range (0, len(answers)):
        if (answers[i] == a[i%len(a)]):
            answerValue[0] +=1
        if (answers[i] == b[i%len(b)]):
            answerValue[1] +=1
        if (answers[i] == c[i%len(c)]):
            answerValue[2] +=1


    mVal = max(answerValue)

    for i in range(0, len(answerValue)):
        if (mVal == answerValue[i]):
            answer.append(i+1)

    return answer

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))
