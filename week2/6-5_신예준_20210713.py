n = int(input())
a = list(map(int,input().split()))
d = {}
li = []
for i in a:
    if i not in d:
        li.append(i)
        d[i] = 0
    else:
        d[i] += 1
li.sort()
for i in li:
    print(i, end=' ')
