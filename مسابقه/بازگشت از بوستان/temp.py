x, y = input().split(" ")
x1, y1 = input().split(" ")
x = int(x)
y = int(y)
x1 = int(x1)
y1 = int(y1)

if x1 > x:
    print("Right")
elif x1 < x:
    print("Left")