import collections 
 
de = collections.deque() 

mosafer1 = input().split(" ")
mosafer2 = input().split(" ")
mosafer3 = input().split(" ")
mosafer4 = input().split(" ")

mosafers = [mosafer1, mosafer2, mosafer3, mosafer4]

for i in mosafers:
    
    if i[1] == 'R':
        de.append(i[0])
        
    elif i[1] == 'L':
        de.appendleft(i[0])
        

print(de[1])