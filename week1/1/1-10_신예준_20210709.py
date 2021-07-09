n = int(input())
d = {}

for i in range(n):
    name = input()
    if name[0] not in d:
        d[name[0]] = 1
    else:
        for key in d.keys():
            if name[0]==key:
                d[key] += 1
li = []
for key, val in d.items():
    if val>=5:
        li.append(key)
if len(li)==0:
        print('PREDAJA')
else:
    li.sort()
    for i in li:
        print(i,end='')
