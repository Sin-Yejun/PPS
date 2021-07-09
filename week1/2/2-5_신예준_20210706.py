n = input()
n = n.upper()
t = {}
for i in range(len(n)):
    if n[i] in t:
        for key, val in t.items():
            if n[i] == key:
                t[key] += 1
    else:
        t.setdefault(n[i],1)
outarray = []
for key, val in t.items():
    if max(t.values()) == val:
        outarray.append(key)

if len(outarray)>1:
    print('?')
else:
    print(outarray[0])
