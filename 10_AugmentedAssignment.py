
# ============================
# 10_AugmentedAssignment.py:
# ============================

# Using Augmented assignment

number = "564,87,945,12" # define string
cleanedNumber = '' # Define with null

for i in range(0, len(number)): # Loop through range
    if number[i] in '0123456789': # test each letter in number
        cleanedNumber = cleanedNumber + number[i] # concatenate

newNumber = int(cleanedNumber)
print("Cleaned Number is: {}".format(newNumber)) # print results

# We can write above code with Augmented assignment for line 9
# note that if you hover over the lines, python will give suggestions of indications of errors

print("="*30)
print("Second line using augmented assignments")
number = "123,45,678,9" # define string
cleanedNumber = '' # Define with null

for i in range(0, len(number)): # Loop through range
    if number[i] in '0123456789': # test each letter in number
        cleanedNumber += number[i] # concatenate

newNumber = int(cleanedNumber)
print("Cleaned Number is: {}".format(newNumber)) # print results

# Examples of augmented assignments using numbers
# and binary operators

print("="*30)
x = 23
print("Original x = {}".format(x))
x += 1
print("x + 1 = {}".format(x))
x -= 4
print("x - 4 = {}".format(x))
x *= 5
print("x * 5 = {}".format(x))
x /= 4
print("x / 4 = {}".format(x))
x **= 2
print("x to power 2 = {}".format(x))
x %= 60
print("x modulus 60 (remainder of x/60) is {}".format(x))

# using binary operators on strings
# Below two are the only binary operators that work with strings

print("="*30)
greeting = "Good"
greeting += " morning" # Concatenate good with morning
print(greeting)

print("="*30)
greeting = "Hallo "
greeting *= 3 # Concatenate Hallo 3 times
print(greeting)

# Here is a list of all the binary operators
# +=, -=, /=, %=, **=, <<=, >>=, &=, ^=, |=

