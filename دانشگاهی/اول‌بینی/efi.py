def checkprime(num):
    t=1
    for i in range(2,num):
       if (num % i) == 0:
           t=0
           break
    return t


a=int(input())
b=int(input())
list=[]
for i in range(a+1,b):
    if checkprime(i)==1:
        list.append(i)
        
for i in list:
    print (i , end='')
    if i==list[len(list)-1]:
        break
    print("," , end='')