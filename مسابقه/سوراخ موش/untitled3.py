x1, x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)

if x1 == x2:
    print("Saal Noo Mobarak!")
elif x1 < x2:
    print((x2 - x1) * "R")
elif x1 > x2:
    print((x1 - x2) * "L")
