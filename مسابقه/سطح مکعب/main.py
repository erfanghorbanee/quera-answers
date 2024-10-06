v=int(input())
maghsum=[]
s=[]
for i in range(1,v+1):
    if v%i==0: maghsum.append(i)    

for a in maghsum :
    for b in maghsum:
        for c in maghsum:
            if a*b*c==v:
                m=2*a*b + 2*b*c + 2*a*c
                s.append(m)

min=s[0]
for i in s:
    if i< min: min=i
print(min)    
          