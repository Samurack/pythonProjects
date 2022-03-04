import sys

i = 1
number_Of_arguments = len(sys.argv)

while i < number_Of_arguments:
    print(str(i) + ". " + sys.argv[i])
    i += 1
