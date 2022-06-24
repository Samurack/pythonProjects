# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# 2. Sort a list
# Create a function in Python that accepts two parameters. The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
# If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

def listSort(listToSort):
    howToSortList = input("Do you want to sort the list in ascending order \"asc\" descending order \"desc\" or just sort it \"none\" ")
    if howToSortList == 'asc':
        listToSort.sort()
    elif howToSortList == 'desc':
        listToSort.sort(reverse = True)
    else:
        pass
    return listToSort

print(listSort([1,9,2,5,3,4]))