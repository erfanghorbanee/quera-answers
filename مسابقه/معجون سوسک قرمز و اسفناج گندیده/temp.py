a, b, c, d, m = input().split(" ")
a, b, c, d, m = int(a), int(b), int(c), int(d), int(m)


for i in range(m):
    a += c
    b += d

if (a > b and c > d) or (b > a and d > c) :
    print("Eyval baba!")
else:
    print("Naaa, eshtebahe!")