file_path = "frt.txt"
file_path_object = open(file_path)
contents_file_path = file_path_object.read()

file_path_object.close()
contents = contents_file_path.splitlines()


for i in contents:
	print(len(i))