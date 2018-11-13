
# lets define a method to add two numbers
def add_nums(first, second):
	# first lets do some type checking on the params
	if type(first) is not int or type(second) is not int or first <0 or second < 0:
		print("Invalid input")
		return -99999999
	return first+second


def sunil():
	print("bhaiyaaaaa!")


def non_returning_func():
	print("THis func returns nothing")

# a = 123
# b = 0
# print("The output is: "+ str(add_nums(a,b) ))
# sunil()

a = non_returning_func() +20
print(a)



