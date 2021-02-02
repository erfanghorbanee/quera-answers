import sys
sys.setrecursionlimit(10**6)
inp = input()
cnt = inp.count('=')

if cnt == 0:
    print(inp)
else:  
    for i in range(cnt):
        if len(inp)>=2:
            position = inp.find('=')
            
            if position != -1:     
                inp = inp[0:position-1] + inp[position+1:]
        
print(inp)
