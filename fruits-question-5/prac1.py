'''
	The most lehman way
'''

# take user input


#open files and read content
filePath = "fruits.txt"
fileObject = open(filePath)
fileContents = fileObject.read() #fileContents would be a string


# parse file content and check if input exists
# we know the file is line seperated, hence split the content and
# read line by line
contentList = fileContents.splitlines() #contentList will be a list ['apple','banana', ...]

path = "times.log"
path_object = open(path)
contents = path_object.read()
contentsList = contents.splitlines()
# we know the first index of contentsList is int parsable
times = int(contentsList[0])
i = 0
while i < times:

	user_input = input("Enter a fruit name: ")

	found = False
	if user_input in contentList:
		found = True
    
	if found == True:
		print("Fruit found:: "+user_input)
	else :
		print("Fruit not found")
	i = i + 1


# close the file after processsing
path_object.close()
fileObject.close()
