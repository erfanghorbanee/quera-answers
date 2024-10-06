n, k = input().split(" ")
n, k = int(n), int(k)

s = []
for i in range(1, n + 1):
    s.append(i)

i = 0
rounds = 0
while True:
    i += k
    rounds += 1

    if i <= n - 1:
        if s[i] == 1:
            # print(i)
            break

    elif i > n - 1:
        i = i - (n)
        if s[i] == 1:
            break

print(rounds)
