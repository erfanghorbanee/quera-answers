n = input()

#b = sum of digits of input
b = 0

for i in n:
    b+= int(i)

#checkprime function
def checkprime(num):
    t=1
    for i in range(2,num):
       if (num % i) == 0:
           t=0
           break
    return t


i = 0
n = int(n)
while i < b:
    n += 1
    if checkprime(n)== 1:
        i += 1
    
print(n)
