#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, red):
    testSet = []
    sum = brown + red
    for i in range (1, sum+1):
        if sum % i == 0 and i >= sum/i:
            testSet.append([i,sum/i])
                                               
    for ts in testSet:
        if (ts[0] - 2) * (ts[1] - 2) == red: 
         return ts


if __name__ == "__main__":
    print(solution(10,2))
    print(solution(8,1))
    print(solution(24,24))
