def solution(A):
    ans = 0
    for i in range(len(A)):
        ans = ans + A[i]
    return ans



-------------------------------------------------------
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    returnVaule = ""
    for i in range(N):
        if (i % 2 ) == 0:
            returnVaule += "+"
        else:
            returnVaule += "-"
    return returnVaule


    ------------------------------------------------
    def solution(s):
    c = s[0]
    if c.isupper():    # please fix condition
        return "upper"
    elif c.islower():  # please fix condition
        return "lower"
    elif c.isdigit():  # please fix condition
        return "digit"
    else:
        return "other"

----------------------------------------------
