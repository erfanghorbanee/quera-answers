x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

if x2 > x1 and v2 > v1: 
    print("BORO BORO")
if x2 < x1 and v2 < v1: 
    print("BORO BORO")
    
if x2 > x1 and v2 == v1: 
    print("WAIT WAIT")
if x2 < x1 and v2 == v1:
    print("WAIT WAIT")

if x2 > x1 and v2 < v1:
    print("SEE YOU")
if x2 < x1 and v2 > v1:
    print("SEE YOU")



