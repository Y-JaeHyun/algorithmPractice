#https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    minMove = len(name) - 1

    count = 0

    for idx, alphabet in enumerate(name):
        answer += min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1)

        nextIdx = idx + 1
        while nextIdx < len(name) and name[nextIdx] == 'A':
            nextIdx += 1

        minMove = min(minMove, idx + idx + len(name) - nextIdx)

    answer += minMove

    return answer
