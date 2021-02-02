def getnumber(string):
    list=[]
    for i in string:
        if i not in list:
            list.append(i)         
    return len(list)  
    

n=int(input())
max=0
for i in range(n):
    s= input()
    if getnumber(s) > max:
        max = getnumber(s)

print(max)