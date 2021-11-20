#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = [number[0]]

    for num in number[1:]:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
