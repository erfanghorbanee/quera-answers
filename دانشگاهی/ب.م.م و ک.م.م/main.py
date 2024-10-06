import math

input = input().split(" ")
n = int(input[0])
m = int(input[1])


def lcm(a, b):
    return (a * b) / math.gcd(a, b)


print(math.gcd(n, m), int(lcm(n, m)))
