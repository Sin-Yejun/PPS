s = input()
d = []
for i in range(len(s)):
    pv = ''
    pv += s[i:len(s)]
    d.append(pv)
d.sort()
for i in d:
    print(i)
