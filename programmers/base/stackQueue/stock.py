#https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [0]
    
    
    for i in range (1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(prices) - i - 1
    return answer
