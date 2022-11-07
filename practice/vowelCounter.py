# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 4. Count the vowels in a string
# Create a function in Python that accepts a single word and returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u will be counted as vowels — not y.

def countVowels(word):
    count = 0
    for each in word:
        if each == 'a' or each ==  'e' or each ==  'i' or each ==  'o' or each == 'u':
            count += 1
    return count

print(countVowels("camera"))