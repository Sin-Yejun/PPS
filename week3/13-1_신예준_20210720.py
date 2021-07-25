import sys
n, won = sys.stdin.readline().split()
n = int(n)
won = int(won)
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse = True)
i = 0
count = 0
while won != 0:
    x = 0
    if coin[i] <= won:
        x = won // coin[i]
        won -= coin[i]*x
        count+=x
    elif coin[i] > won:
        i+=1
print(count)
    
