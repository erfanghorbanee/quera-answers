n = int(input())
s = input().split()
s2 = [None] * n
for i in range(n):
    s2[n - 1] = s[i]
    n -= 1

for i in s2:
    print(i, end="")
    if i != s2[n - 1]:
        print(" ", end="")
