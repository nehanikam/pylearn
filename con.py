def string_length(mystring):
     if type(mystring) == int:
         return "Sorry, integers don't have length"
     elif type(mystring) == float:
         return "Sorry, floats don't have length"
     else:
         return len(mystring)


b= mytypee 
print(string_length(b))