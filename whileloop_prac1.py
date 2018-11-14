orignal_password = "neha123"
first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")

password = input("Enter password: ")

while orignal_password != password:
	password = input("Wrong password! Enter the correct password: ")

print("You are successfully logged in as %s %s " %(first_name , last_name) )