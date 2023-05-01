n = int(input())
gp = input().split(" ")

for i in range(n):
    if int(gp[i]) > 3:
        print("*")
    else:
        print(int(gp[i]) * "*")
