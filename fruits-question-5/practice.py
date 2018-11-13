fpath1 = "fruit1.txt"
fpath1_Object = open(fpath1)
fpath1_Contents = fpath1_Object.read()
content_list1 = fpath1_Contents.splitlines()


fpath2 = "fruit2.txt"
fpath2_Object = open(fpath2)
fpath2_Contents = fpath2_Object.read()
content_list2 = fpath2_Contents.splitlines()



i = 0
commonFruits = []
while i < len(content_list1):
	if content_list1[i] in content_list2 and content_list1[i] not in commonFruits:
		commonFruits.append(content_list1[i])
	i = i + 1

if len(commonFruits) == 0:
	print("No fruit found")
else:
	print("Common Fruits are: ")
	print(commonFruits)

fpath2_Object.close()
fpath1_Object.close()