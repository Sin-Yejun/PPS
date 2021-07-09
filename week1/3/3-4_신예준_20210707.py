n = int(input())
a = int(input())
if(n > 5):
    print('Love is open door')
else:
    for i in range(2,n+1):
        if a == 0:
            print(1)
            a = 1
        else:
            print(0)
            a= 0
