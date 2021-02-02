x = int(input())
n = int(input())
ans = 0
if n == 0:
    ans = 20
elif n == 7:
    ans = x
else :
    ans = x - n

if ans < 0:
    print(0)
else :
    print(ans)