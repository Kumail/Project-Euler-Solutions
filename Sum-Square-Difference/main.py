sumOfSquare = 0
squareOfSum = 0

limit = 100

for x in range(limit+1):
    squareOfSum += x
    sumOfSquare += (x*x)

squareOfSum = squareOfSum * squareOfSum

difference = squareOfSum - sumOfSquare
print("Difference= ", difference)