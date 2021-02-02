n = int(input())
f0 = 0
f1 = 1
i = 1

while i <= n:
    fn = f1 + f0
    if i == fn:
        print("+", end="")
        f0 = f1
        f1 = fn
        i+=1
    else:
        print("-", end="")
        i+=1