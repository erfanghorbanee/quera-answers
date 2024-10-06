# Python 3 code for Pascal's Triangle
# A simple O(n^3)
# program for
# Pascal's Triangle

# Function to print
# first n lines of
# Pascal's Triangle
def printPascal(n):

    # Iterate through every line
    # and print entries in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print(binomialCoeff(line, i), " ", end="")
        print()


# See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
# for details of this function
def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


# Driver program
n = int(input())
printPascal(n)


# This code is contributed by Nikita Tiwari.
