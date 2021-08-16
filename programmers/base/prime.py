#https://programmers.co.kr/learn/courses/30/lessons/42839

import itertools
import math
def isPrime(number):
    if number == 0 or number == 1 : return False    
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0 : return False
                           
    return True


def solution(numbers):
    numberSet = list(numbers)
    testSet = []
    resultSet = []
    for i in range(1, len(numberSet)+1):
        testSet += list(map(''.join, itertools.permutations(numberSet,i)))
    
    testSet = set(map(int, testSet))
                                                                                
    for ts in testSet:
        if isPrime(ts): resultSet.append(ts)
    
    return len(resultSet)

if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))
