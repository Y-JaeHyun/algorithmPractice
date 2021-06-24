#https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    checkBoard = [ [0 for col in range(n)] for row in range (m) ]   
    board = [ list(string) for string in board ]

    answer = 0
    find = 0
    for i in range (0, len(board)-1):
        for j in range (0, len(board[i])-1):
            if board[i][j] == 'x' or board[i][j] == 'y': 
                continue
            if board[i][j] == board[i][j+1] and board [i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                find = find + 1
                checkBoard[i][j] = 1
                checkBoard[i][j+1] = 1
                checkBoard[i+1][j] = 1
                checkBoard[i+1][j+1] = 1

    if find == 0: 
        return 0

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if checkBoard[i][j] == 1:
                answer = answer + 1
                board[i][j] = 'x'


    for i in range(n):
        temp = []
        for j in range(m):
            if board[j][i] != 'x':
                temp.append(board[j][i])
        for j in range(m-len(temp)):
            board[j][i] = 'x'
        for j in range(m-len(temp), m):
            board[j][i] = temp.pop(0)

    return answer + solution(m, n, board)

if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
