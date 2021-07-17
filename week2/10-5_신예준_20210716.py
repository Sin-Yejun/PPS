def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    yoil = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    day = 0
    if a==1:
        day = b
    else:
        for i in range(a-1):
            day += days[i]
        day += b
    index = day%7
    answer = yoil[index]
    return answer
