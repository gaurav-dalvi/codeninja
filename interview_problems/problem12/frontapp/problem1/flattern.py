def flattern(arr, output):

	if arr is None: 
		return None
	for item in arr:
		if type(item) == list:
			flattern(item, output)
		else:
			output.append(item)
