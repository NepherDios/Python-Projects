def filterNameBySize(namesList):
	for i in namesList:
		if len(i) > 4:
			print(f"{i}")

namesList = ["Moreira", "Derick", "Pietro", "Tay", "Price"]
filterNameBySize(namesList)
