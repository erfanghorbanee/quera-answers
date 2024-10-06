xl = input().split(" ")
winner = input().split(" ")

if int(xl[0]) >= int(winner[0]) and int(xl[1]) >= int(winner[1]):
    print("yes")
else:
    print("no")
