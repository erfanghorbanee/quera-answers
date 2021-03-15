t = int(input())
lst = []

for i in range(t):
    lst.append(input())
    
def f1(x):
    
    for i in range(10):
        
        count = 0
        for j in x: 
            if j == str(i): 
                count = count + 1
                if count >= 4:
                    return True

def f2(x):
    for i in range(10):
        if x.count(3*str(i)) >= 1:
            return True

def f3(x):
    if x == x[::-1]:
        return True
                
    
    

for i in lst:
    
    if f1(i) == True or f2(i) == True or f3(i) == True:
        print("Ronde!")
    else:
        print("Rond Nist")