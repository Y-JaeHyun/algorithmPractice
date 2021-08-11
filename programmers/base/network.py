#https://programmers.co.kr/learn/courses/30/lessons/43162

def search(arr, computers, computer):
    for i, com in enumerate(computer):
        if com == 1 and arr[i] == 0:
            arr[i] = 1
            search(arr, computers, computers[i])

def solution(n, computers):
    answer = 0
    arr = [0 for i in range (n)]

    for i in range (0,n):
        if arr[i] == 0:
            answer +=1
            arr[i] = 1
            search(arr, computers, computers[i])
                                                                                                                                                        
    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
