n = int(input())
state1 = int(input())
sum = 0

for i in range(n - 1):
    state = int(input())
    if state != state1:
        sum += 1
        state1 = state

print(sum)
