n = int(input())
list = []
sum = 0  # hasele jame adad ha

for i in range(0, n):
    k = float(input())
    list.append(k)
    sum += k

list.sort()
avg = sum / n


# baraie vaghti k tedad ashar bishtar az 3ta bashe auto round ro control mikone ta asharo daghigh b dast biare!
def func(i):
    n = len(str(i).split(".")[1])
    if n >= 3:
        return int(i * 10**3) / 10**3

    else:
        return i


print("Max: %.3f" % func(list[n - 1]))  # max
print("Min: %.3f" % func(list[0]))  # min
print("Avg: %.3f" % func(avg))  # avg
