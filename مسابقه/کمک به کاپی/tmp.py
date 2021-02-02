inp = input().split(" ")
s=""
n = int(inp[0])

for i in range(n):
    s += "copy of "

s += inp[1]

print(s)