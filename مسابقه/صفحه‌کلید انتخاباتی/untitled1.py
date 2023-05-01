n = int(input())
string = ""
caps = -1  # CapsLock off

for i in range(n):
    inp = input()
    if inp == "CAPS":
        caps = -caps
        inp = ""

    if caps == 1:  # CapsLock on
        string += inp.upper()
    elif caps == -1:
        string += inp

print(string)
