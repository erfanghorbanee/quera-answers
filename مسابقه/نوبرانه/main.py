inp = input().split()
count = 0

for i in inp:
    if int(i) >= 80:
        count += 1

if count >= 3:
    print("Mamma mia!")
elif 0 < count < 3:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
