list=[1,1,2,2,2,8]
vorudi=input().split()
for i in range(6):
    list[i]=list[i]-int(vorudi[i])
    
print(list[0],list[1],list[2],list[3],list[4],list[5])   