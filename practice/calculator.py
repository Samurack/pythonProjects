#https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# Write a Python function that accepts three parameters. The first parameter is an integer. 
# The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.
# The function should perform a calculation and return the results. 
# For example, if the function is passed 6 and 4, it should return 24.

def add(firstNum, secondNum):
    return firstNum + secondNum

def subtract(firstNum, secondNum):
    return firstNum - secondNum

def divide(firstNum, secondNum):
    return firstNum / secondNum

def multiply(firstNum, secondNum):
    return firstNum * secondNum

firstNumber = int(input("firstNumber: "))
operator = input("operator: ")
secondNumber = int(input("secondNumber: "))

if operator == '+':
    print(add(firstNumber, secondNumber))
elif operator == '-':
    print(subtract(firstNumber, secondNumber))
elif operator == '/':
    print(divide(firstNumber, secondNumber))
else:
    print(multiply(firstNumber, secondNumber))