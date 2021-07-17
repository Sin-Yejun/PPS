n = int(input())
t = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    t.append((age, name))
t.sort(key = lambda x:x[0])
for i in t:
    print(i[0],i[1])

