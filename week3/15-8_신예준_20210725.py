n = int(input())
d = list(map(int,input().split()))
sup = []
up = []
pv = 0
ct = 0
for i in d:
    ct +=1
    if i>pv:
        sup.append(i)
    if i<=pv or ct == n:
        if len(sup)>1:
            up.append(sup)
        sup = []
        sup.append(i)
    pv = i
if len(up)==0:
    print(0)
else:
    for i in range(len(up)):
        up[i] = up[i][-1] - up[i][0]
    print(max(up))
        
