from math import floor
inp = input().split(" ")
n = int(inp[0])

for i in range(0, int(inp[1])):
    n = n / 2

print(floor(n))
    