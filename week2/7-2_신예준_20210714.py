a, b = input().split()
a = int(a)
b = int(b)
d = {0: 'zero' , 1:'one', 2:'two', 3:'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8:'eight', 9:'nine'}
t = []
for k in range(a,b+1):
    temp = list(map(int, str(k)))
    tp =''
    for i in temp:
        tp += d[i]
    t.append((int(k),tp))
t.sort(key = lambda x:x[1])

for i in range(1, len(t)+1):
    print(t[i-1][0],end=' ')
    if i%10==0:
        print()
