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
contentList = fileContents.splitlines() #contentList will be a list ['apple','banana', ...]
found = False
if user_input in contentList:
	found = True




# display the result to the user
if found == True:
	print("Fruit found:: "+user_input)
else :
	print("Fruit not found")

# close the file after processsing
fileObject.close()