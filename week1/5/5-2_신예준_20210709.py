n = int(input())
s = 0
for k in range(n):
    a = []
    a = input().split()
    s = 0
    for i in a:
        if i == '@':
            s = s *3
        elif i == '%':
            s += 5
        elif i == '#':
            s -=7
        else:
            i = float(i)
            s += i
    print('{:.2f}'.format(s))

