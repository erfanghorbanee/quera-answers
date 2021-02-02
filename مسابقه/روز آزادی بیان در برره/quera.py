bb = 0  
pb = 0
k = int(input())

while (True):
    bb = pb + 1
    pb = bb + 1
    # print("bb: ", bb)
    # print("pb: ", pb)
    
    if bb == k:
        print("Payin Barare")
        break
    if pb == k:
        print("Bala Barare")
        break