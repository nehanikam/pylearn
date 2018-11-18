import json


#Step1 open the file and load contents
file_path = "jsontest.json"
file_oject = open(file_path)
file_content = file_oject.read()

#Step2 Load contents in Json object
jo = json.loads(file_content)


# The outputs
num_of_curr = 0
non_btc_curr = 0
unique = {}
highTxFee = []
# Q1
num_of_curr = len(jo["result"])


#Q2/Q3
i = 0
while i < len(jo["result"]):
	# Check if the coin type is not of type btc
	if jo["result"][i]["CoinType"] != "BITCOIN":
		non_btc_curr = non_btc_curr + 1
		unique[ jo["result"][i]["CoinType"] ] = True
		

	if jo["result"][i]["TxFee"] >= 1.0:
		highTxFee.append(jo["result"][i]["Currency"])

	# Loop counter
	i += 1



# ======================================================== #
print("Total num of currencies: "+str(num_of_curr))
print("Total non btc currencies: "+str(non_btc_curr))
for coinType in unique:
	print(coinType)

print("Currencies with high Tx fee (>1.0):")
# index=0
# while index < len(highTxFee):
# 	curr = highTxFee[index]
# 	print(curr)
# 	index += 1
print(highTxFee)