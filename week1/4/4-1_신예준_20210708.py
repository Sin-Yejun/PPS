li = []
for i in range(5):
    s = []
    s = list(map(int,input().split()))
    li.append(sum(s))
for i in range(5):
    if max(li) == li[i]:
        print(i+1, max(li))
    
