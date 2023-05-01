n = int(input())
str1 = input()
str2 = input()
k = 0  # tedade horufe motafavet

for i in range(0, n):
    if str1[i] != str2[i]:
        k += 1

print(k)
