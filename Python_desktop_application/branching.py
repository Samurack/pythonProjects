import sys
if int(sys.argv[1]) + int(sys.argv[2]) <= 0:
    print("You have chosen the path of destitution.")
elif int(sys.argv[1]) + int(sys.argv[2]) <= 100:
    print("You have chosen the path of plenty.")
elif int(sys.argv[1]) + int(sys.argv[2]) > 100:
    print("You have chosen the path of excess.")