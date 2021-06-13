
#https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = []

    for i in range(0, n):
        value = str(bin(arr1[i] | arr2[i])[2:])
        value = value.zfill(n)
        value = value.replace('1', '#')
        value = value.replace('0', ' ')
        answer.append(value)

    return answer


if __name__ == "__main__":
    solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
    solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
