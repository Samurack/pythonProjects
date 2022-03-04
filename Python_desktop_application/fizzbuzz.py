import sys
number_Of_arguments = len(sys.argv)
i = 1

while i < number_Of_arguments:
    if int(sys.argv[i]) % 3 == 0 and int(sys.argv[i]) % 5 == 0:
        print("fizzbuzz")
    elif int(sys.argv[i]) % 3 == 0:
        print("fizz")
    elif int(sys.argv[i]) % 5 == 0:
        print("buzz")
    else:
        print(sys.argv[i])
    i += 1

