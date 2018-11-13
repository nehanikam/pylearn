'''
	A better way
'''

# take user input
def get_user_input(screen_msg):
	inp = input(screen_msg)
	return inp


# open files and read content
def getFileContents(filePath):
	# open the file
	fileObject = open(filePath)
	# read file content
	content = fileObject.read()
	# close the file to return system resource
	fileObject.close()
	# return the content
	return content


# Finds the string you are looking for(needle)
# in the haystack list
def check(needle, haystack):
	if needle in haystack:
		return True
	return False



# module start

# Step1: Load the file first since it can be big
fileContents = getFileContents("fruits.txt")
contentList = fileContents.splitlines()


# Lets read the log file and get the number of times
# to be executed
timesContent = getFileContents("times.log");
times = int((timesContent.splitlines())[0])

i = 0
while i < times:
	# step2: Get the user input
	user_input = get_user_input("Enter a fruit name: ")

	# step3: Check if the input exists
	found = check(user_input, contentList)

	# step4:Display results
	if found == True:
		print("Fruit found:: "+user_input)
	else :
		print("Fruit not found")
	i = i+1
