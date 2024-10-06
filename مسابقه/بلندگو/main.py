s = input()
print(s)
i = 0
while i < len(s) - 1:
    i += 1
    s = s[i] * (i + 1) + s[i + 1 :]
    print(s)
