import math

inp = int(input())
fact = math.factorial(inp)


def f(n):
    n = str(n)
    for i in range(len(n) - 1, -1, -1):
        if int(n[i]) != 0:
            print(n[i])
            break


f(fact)
