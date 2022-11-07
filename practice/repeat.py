# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 10. Repeat the characters
# Create a Python function that accepts a string. 
# The function should return a string, with each character in the original string doubled. 
# If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def repeats(userString):
    repeats = ""
    for each in userString:
        repeats += each
        repeats += each
    return repeats

userInput = input("Please feed me a string: ")
print(repeats(userInput))