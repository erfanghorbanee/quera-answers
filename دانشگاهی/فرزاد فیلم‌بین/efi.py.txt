def moratab(s):
    string=s.split()
    j=0
    for i in string:
        string[j]=i[0].upper()+i[1:].lower()
        print(string[j],end='')
        j+=1
        if j<len(string):
            print(" ",end='')

list=[]
n= int(input())
for i in range(n):
    s=input()
    list.append(s)
    
for i in list:
    moratab(i)
    if i!=list[len(list)-1]:
        print("")