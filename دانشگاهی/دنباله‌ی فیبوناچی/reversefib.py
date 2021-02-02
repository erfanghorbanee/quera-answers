def ShowFibNth(n0,n1):
    print(n0)
    
    x = n0
    n0 = n1-n0
    n1 = x
    
    if n0 <= 0 :
        return 0
    else:
        return ShowFibNth(n0,n1)
    
    

n0 = int(input())
n1 = int(input())
ShowFibNth(n0, n1)