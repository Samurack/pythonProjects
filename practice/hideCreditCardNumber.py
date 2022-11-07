# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 5. Hide the credit card number
# Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden with an asterisk except the last four. 
# For example, if the function gets sent "4444444444444444", then it should return "4444".

def replace(creditCardNumber):
    secretCard = creditCardNumber[-4:]
    return secretCard

print(replace("4444444444444444"))