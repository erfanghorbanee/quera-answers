s=[]
while(True):
    n=int(input())
    if n!= 0:
        s.append(n)
    elif n== 0:
        for i in range(len(s)-1,-1,-1):
          print(s[i])
        break