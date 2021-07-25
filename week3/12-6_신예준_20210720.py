n = int(input())
a = [1,1]
c = 0
for i in range(1, n-1):
    c = a[i-1]+a[i]
    a.append(c)
print(a[-1])
    
    
