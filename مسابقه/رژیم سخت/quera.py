barchasb = input()
red = 0  
green = 0 
yellow = 0

for i in barchasb:
    if i == "R":
        red+=1
    elif i == "Y":
        yellow+=1
    elif i == "G":
        green+=1

if red==3 or green==0 or (red==2 and yellow==2):
    print("nakhor lite")
else:
    print("rahat baash")