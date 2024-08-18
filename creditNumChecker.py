from sys import exit

# Accepting user input
originalInput = input("Insert card number: ")

# Removing dashes or spaces in between
strippedNum = originalInput.replace(' ','').replace('-','')

# Checking for errors
try:
    strippedNum = int(strippedNum)
except ValueError:
    print("Incorrect value! Can not be a string or contain characters other than dashes or spaces.")
    exit()
else:
    strippedNum = str(strippedNum)

# Variables
oddNumbers = []
evenNumbers = []
numArray = []
doubleEvenNumbers = []
sumOddNumbers = 0
sumEvenNumbers = 0
sumAll = 0

# Transforming the number into a list so we can manipulate the number
for i in strippedNum:
    numArray.append(int(i))

# Reversing the number so we can manipulate from right to left
numArray.reverse()

# Adding up numbers in the odd places from right to left
for x,y in enumerate(numArray):
    if x % 2 == 0:
        oddNumbers.append(y)
    else:
        pass

# Adding up numbers in the even places from right to left
for x,y in enumerate(numArray):
    if x % 2 != 0:
        evenNumbers.append(y)
    else:
        pass

# Doubling up the even-place-numbers
for x in evenNumbers:
    x *= 2
    doubleEvenNumbers.append(x)

# Clearing up the first array so we would not be creating a ton of arrays for each thing
evenNumbers.clear()

# Checking if the number doubled up results in a 2-digit number, so we split it and add the digits
for o in doubleEvenNumbers:
    if o >= 10:
        y = list(str(o))
        num = 0
        for i in y:
            num += int(i)
        o = num
    else:
        pass
    evenNumbers.append(o)

# Adding up all of the odd-place-numbers
for z in oddNumbers:
    sumOddNumbers += z

# Adding up all of the even-place-numbers
for w in evenNumbers:
    sumEvenNumbers += w

# Adding everything up
sumAll = sumEvenNumbers + sumOddNumbers

# Checking the divisibility by 10 and returning if the number is valid or not
if sumAll % 10 == 0:
    print("VALID")
else:
    print("INVALID")