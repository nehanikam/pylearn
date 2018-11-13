'''
	The most lehman way
'''

# take user input
user_input = input("Enter a fruit name: ")

#open files and read content
filePath = "fruits.txt"
fileObject = open(filePath)
fileContents = fileObject.read() #fileContents would be a string

# parse file content and check if input exists
# we know the file is line seperated, hence split the content and
# read line by line
contentList = fileContents.splitlines()

# display the result to the user