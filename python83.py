#Write a Python function that prints out the first n rows of Pascal's triangle.
# Print Pascal's Triangle in Python
from math import factorial
 
# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()

print("******************************************************************************************")
#Print Pascal's Triangle in Python
 
# input n
n = 5
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()
