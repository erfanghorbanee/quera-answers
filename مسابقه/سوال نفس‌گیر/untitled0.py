n = int(input())
ai = input().split(' ')
bi = input().split(' ')

x = 0
for i in range(n):
    x += int(ai[i]) * int(bi[i])
    
print(x)