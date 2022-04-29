import tkinter as tk #https://www.geeksforgeeks.org/python-program-to-replace-specific-line-in-file/
from tkinter import filedialog
import string
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path) as f:
    lines = f.readlines()

def getDependsOn(index, array):
    dependsArray = []
    dependsOnIndex = index + 1
    for i in range(dependsOnIndex, len(array)):
        if "-" in array[i]:
            dependsArray.append(array[i])
            dependsOnIndex = i
        else:
            break
    return dependsArray

def arrangeParameters(index, array):
    alphabatizeArray = []
    for i in range(index, len(array)):
        if "DependsOn" in array[i]:
            print("DependsOn")
            alphabatizeArray.append(array[i])
            dependsonArray = getDependsOn(i, array)
        elif "-" in array[i]:
            pass
        elif array[i].strip():
            print("Not blank")
            alphabatizeArray.append(array[i])
        else:
            print("done")
            alphabatizeArray = sorted(alphabatizeArray, key=str.casefold) #https://stackoverflow.com/questions/10269701/case-insensitive-list-sorting-without-lowercasing-the-result
            alphabatizeArray.append(array[i])
            break
    newArrayLength = len(alphabatizeArray) + index
    for singleLine in range(len(alphabatizeArray)): #add in the depends on
        if "DependsOn" in alphabatizeArray[singleLine]:
            for depends in dependsonArray:
                alphabatizeArray.insert(singleLine + 1, depends) #https://www.programiz.com/python-programming/methods/list/insert
    return alphabatizeArray, newArrayLength

goForIt = 0

for line in range(0, len(lines)):
    print(goForIt)
    if goForIt == 1:
        newalphabatizeArray, changeLength = arrangeParameters(line, lines)
        alphabatizeIndex = 0 #set array index
        tempIndex = line
        for i in range(tempIndex, changeLength):
            lines[i] = newalphabatizeArray[alphabatizeIndex]
            if alphabatizeIndex <= len(newalphabatizeArray):
                alphabatizeIndex += 1
        goForIt = 0
    if "parameters" in lines[line]:
        goForIt = 1

with open(file_path, 'w') as file:
    file.writelines(lines)