n, m = input().split(" ") 
n = int(n)
m = int(m)

count1 = 0
count2 = 0

for i in range(2*n):
    inp = input()
    for j in inp:
        if j == "*" and i < n:
            count1 += 1
        elif j == "*" and i >= n:
            count2 += 1

print(count1, count2)
            