n = int(input())
s = input()
path = input().split(" ")
path[0] = int(path[0])
path[1] = int(path[1])

if path[0] == path[1]:
    print(0)
    
else:
    def func(zurgir, count):    
            for i in range(10):
                if pow(2, i) == zurgir:
                    count +=1
                    return count
                
                elif pow(2,i) > zurgir:
                    zurgir -= pow(2, i-1)
                    count += 1
                    return func(zurgir, count)
    
    zurgir = 0
    ls = list()
    if path[1] > path[0]:
        for i in s[path[0]-1:path[1]]:
            if i == "H":
                zurgir += 1
            elif zurgir != 0:
                ls.append(zurgir)
                zurgir = 0
                
    else:
        for i in s[path[1]-1:path[0]]:
            if i == "H":
                  zurgir += 1
            elif zurgir != 0:
                ls.append(zurgir)
                zurgir = 0
    
    # print(ls)
    ans = 0
    for i in ls:
        ans += func(i, 0)
    
    print(ans)