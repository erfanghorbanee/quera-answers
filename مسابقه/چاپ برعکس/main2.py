list = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        list.append(n)

list.reverse()
for i in list:
    print(i)
