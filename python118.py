#Write a program to Find Multiplication of two Binary Numbers.
def binaryProduct(binaryOne, binaryTwo):
	i = 0
	remainder = 0
	sum = []
	binaryProd = 0

	# if firstBinary number or second Binary number is not
	# zero then calculate the product of two Binary numbers
	while binaryOne != 0 or binaryTwo != 0:
		sum.insert(i, (((binaryOne % 10) + (binaryTwo % 10) + remainder) % 2))
		remainder = int(((binaryOne % 10) + (binaryTwo % 10) + remainder) / 2)
		binaryOne = int(binaryOne/10)
		binaryTwo = int(binaryTwo/10)
		i = i+1

	# if remainder value is not equal to
	# zero then insert the digit to sum array
	if remainder != 0:
		sum.insert(i, remainder)
		i = i+1
	i = i-1
	while i >= 0:
		binaryProd = (binaryProd * 10) + sum[i]
		i = i-1
	return binaryProd


binaryMultiply = 0
factor = 1
firstBinary = int(input("b1: "))

secondBinary = int(input("b2: "))

# Now check if secondbinary number have any
# digit or not and continue multiplying
# each digit of the second binary number with
# first binary number till the last digit of
# second binary number
while secondBinary != 0:
	digit = secondBinary % 10
	if digit == 1:
		firstBinary = firstBinary * factor
		binaryMultiply = binaryProduct(firstBinary, binaryMultiply)
	else:
		firstBinary = firstBinary * factor
	secondBinary = int(secondBinary/10)
	factor = 10
print("\nMultiplication Result = " + str(binaryMultiply))