nm = input().split(" ")
n = int(nm[0]) #tedade satr
m = int(nm[1]) #tedade horuf dar har satr
number = 0 #tedade setare ha

for i in range(0, n):
    aseman = input()
    for j in aseman: 
        if j == '*': 
            number += 1

print(number)