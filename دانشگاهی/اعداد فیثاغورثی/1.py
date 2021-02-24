n1 = int(input())
n2 = int(input())
n3 = int(input())
a = 0
b = 0
c = n1

if n2 > c:
    c=n2
    b=n1
else:
    b = n2
		
if n3 > c: 
	c=n3
	a=n1
else:
    a = n3
    
if a*a + b*b == c*c:
    print("YES")		
else:
    print("NO")
