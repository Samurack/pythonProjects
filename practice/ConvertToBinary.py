# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 3. Convert a decimal number into binary
# Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
# To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
# https://www.cuemath.com/numbers/decimal-to-binary/#:~:text=The%20simplest%20way%20to%20convert,of%20the%20given%20decimal%20number.
import math

def convert_decimal_to_binary(quotient):
    binary = ""
    while quotient > 0:
        quotient = quotient / 2
        if quotient.is_integer():
            binary = "0" + binary
        else:
            binary = "1" + binary
            quotient = int(quotient)
    return binary

userDec = int(input('What decimal number do you want to convert to binary? It must be less than 1,024 '))
print("My answer", convert_decimal_to_binary(userDec))
print("Computer answer", bin(userDec)[2:])