n = int(input())
for i in range(n):
    string = input()
    O_count = 1
    total = 0
    pv = ''
    for i in string:
        if i == pv:
            O_count += 1
        else:
            O_count = 1
        if i == 'O':
            total += O_count
        pv = i
    print(total)
