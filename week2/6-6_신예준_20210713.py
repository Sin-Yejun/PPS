n = int(input())
li = []
d = {}
for i in range(n):
    serial = input()
    li.append(serial)
li = sorted(li, key = len)
for i in li:
    digit_sum = 0
    for j in i:
        if j.isdigit():
            digit_sum += int(j)
    d[i] = digit_sum
#문자열 길이 순, 각자리 숫자 합, 알파벳 순으로 정렬
li = sorted(d.items(),key = lambda x: (len(x[0]),x[1],x))

for i in range(n):
    print(li[i][0])
