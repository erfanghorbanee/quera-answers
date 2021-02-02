n = int(input()) #tedade space
s = 1 #tedade setare ha
n = int(n/2)
while n >= 0:
    l = " " * n + "*" * s + " " * n
    print(l*2)
    n -= 1
    s += 2
else:
    n += 1
    s -= 2
    while s > 1:
        n += 1
        s -= 2
        l = " " * n + "*" * s + " " * n
        print(l*2)


