# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 9. Just the numbers
# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
# The function should return a list with only the integers in the original list in the same order.

def convertToCompare(uI, uS):
    sameList = ""
    for each in uS:
        if each in uI:
            sameList += each
    return sameList    

userInt = str(input("Please feed me an int: "))
userString = str(input("Please feed me a string with numbers in it: "))

print(convertToCompare(userInt, userString))