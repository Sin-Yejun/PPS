n = int(input())
for i in range(n):
    count = 0
    li = list(map(int,input().split()))
    size = li[0]
    del li[0]
    avg = sum(li)/float(size)
    for j in li:
        if j > avg:
            count +=1
    result = float(count)/size*100
    print('{:.3f}%'.format(result))
