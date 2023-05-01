n = input()
m = input()

if int(n[2]) < int(m[2]):
    print(n, "<", m)

elif int(n[2]) > int(m[2]):
    print(m, "<", n)

elif int(n[1]) < int(m[1]):
    print(n, "<", m)

elif int(n[1]) > int(m[1]):
    print(m, "<", n)

elif int(n[0]) < int(m[0]):
    print(n, "<", m)

elif int(n[0]) > int(m[0]):
    print(m, "<", n)

else:
    print(n, "=", m)
