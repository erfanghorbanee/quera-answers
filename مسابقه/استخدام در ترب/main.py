n = int(input())
a = input().split(" ")
s = 0
# cnt = 0

for i in range(0, n):
    for j in range(0, n):
        if a[i] < a[j]:
            continue
        f = int(int(a[i]) / int(a[j]))
        s += f
        # cnt +=1

print(s)
