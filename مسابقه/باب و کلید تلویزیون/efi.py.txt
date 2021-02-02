n=input().split(" ")
number=int(n[0])
x=int(n[1])
k=int(n[2])
kanal=[None]*number

for i in range(number):
    kanal[i]=input()
    
for i in range(k):
    if x < number :
        x+=1
    elif x==number:
        x=0
        x+=1
        
print(kanal[x-1])