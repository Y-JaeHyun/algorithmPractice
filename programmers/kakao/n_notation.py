#https://programmers.co.kr/learn/courses/30/lessons/17687

def changeNotation(num, noType):
    notationMap = '0123456789ABCDEF'
    notation = ''
    while num > 0:
        num, mod = divmod(num, noType)
        notation += notationMap[mod]

    return notation[::-1]

def solution(n, t, m, p):
    gameString = '0'
    retVal = ''
    num = 1

    while len(gameString) < (t*m):        
        gameString += changeNotation(num, n)
        num += 1

    for i in range (0, t):
        retVal += gameString[(i*m)+(p-1)]

    return retVal 

if __name__ == "__main__":
    print(solution(2,4,2,1))
    print(solution(16,16,2,1))
    print(solution(16,16,2,2))
    
