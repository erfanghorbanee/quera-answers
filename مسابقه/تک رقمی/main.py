import math


def f(n, sum):
    while n >= 10:
        temp = n % 10
        n = n / 10
        n = int(n)
        sum += temp
        if n < 10:
            sum += n
    if sum < 10:
        print(sum)
    else:
        f(sum, 0)


n = int(input())
if n >= 10 and n <= math.pow(10, 18):
    f(n, 0)
elif n >= 1 and n < 10:
    print(n)
