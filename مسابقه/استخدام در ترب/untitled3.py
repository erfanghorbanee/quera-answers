inp = input().split(" ")
n = int(inp[0])
q = int(inp[1])

ci = input().split(" ")

sum = 0
list = []
for i in range(0, q):
    list.append(int(input()))


for j in list:
    for i in range(0, n):
        if int(ci[i]) < j:
            sum += 1
    print(sum)
    sum = 0
            