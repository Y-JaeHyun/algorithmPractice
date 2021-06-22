#https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
# TODO : reverse -> pop -> reverse 는 너무 괴랄함... 다른 방법 찾아봐야할듯

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
