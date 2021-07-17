n = int(input())
d = []
for i in range(n):
    x, y = input().split()
    d.append((int(x),int(y)))
d.sort(key = lambda x:(x[0],x[1]))
for i in range(len(d)):
    print(d[i][0], d[i][1])
