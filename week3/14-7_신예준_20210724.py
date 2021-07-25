n = int(input())
d = []
for i in range(n):
    w = input()
    d.append(w)
x = set(d)
d = list(x)
d.sort()
d.sort(key = len)
for i in d:
    print(i)
