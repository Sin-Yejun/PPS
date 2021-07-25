n = int(input())
d = list(map(int,input().split()))
f = [0 for i in range(n)]
ct = 0
for i in range(n):
    if d[i]==1:
        ct+=1
        for j in range(3):
            if i+j < n:
                if d[i+j] == 0:
                    d[i+j] = 1
                else:
                    d[i+j] = 0
print(ct)
