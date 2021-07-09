def solution(x):
    s = 0
    temp = x
    while temp !=0:
        a = temp%10
        s += a
        temp = temp // 10
    if x % s == 0:
        answer = True
    else:
        answer = False
    return answer
