n = int(input())
t = 0
for i in range(1, n + 1) :
    for j in range(1, n + 1):
        print(i*j , "",end="")
        t+=1
        if t == n:
            print("")
            t=0
            
    
