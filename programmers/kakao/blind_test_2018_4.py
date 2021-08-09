#https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

import collections
def solution2(cacheSize, cities):
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

def solution(cacheSize, cities):
    cache = [''] * cacheSize
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer = answer + 1
        else:
            cache.reverse()
            cache.pop()
            cache.reverse()
            answer = answer + 5

        cache.append(city)

    return answer


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

    print(solution2(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution2(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution2(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution2(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution2(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution2(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
