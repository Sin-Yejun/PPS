n = int(input())

c = 1
i = 1
while True:
    if n==1:
        print(1)
        break
    elif n > c and n <= c+6*i:
        print(i+1)
        break
    c = c + 6*i
    i += 1
