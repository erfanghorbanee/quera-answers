# Returns '0' for '1' and '1' for '0'
def flip(c):
    return "1" if (c == "0") else "0"


def One_Complement(bin):

    n = len(bin)
    ones = ""

    for i in range(n):
        ones += flip(bin[i])

    return ones


l, r = input().split(" ")
b = "1"
for i in range(17):
    b += One_Complement(b)

print(b[int(l) - 1 : int(r)])
