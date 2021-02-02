inp = input().split(" ")
r = int(inp[0])
c = int(inp[1])

#to right
if c <= 10:
    print("Right", 10-r+1, c)

#to left  
else:
    print("Left", 10-r+1, 20-c+1)
    