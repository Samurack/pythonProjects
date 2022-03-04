yamlRequired = ['ServiceConnection', 'SecondServiceConnection']

# opening a text file
file1 = open("testing.yml", "r")

# read file content
readfile = file1.read()

# checking condition for string found or not
for x in yamlRequired:
	if x in readfile:
		print('String', x, 'Found In File')
	else:
		print('String', x, 'Not Found')

# closing a file
file1.close()
