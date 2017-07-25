def PrintZigZag(add):
	cols = len(arr)
	rows = len(arr[0])

	flag = False
	for i in xrange(rows):
		if flag == False:
			for j in xrange(cols):
				print arr[i][j],
			flag = True
			print ''
		else:
			for j in xrange(cols-1,-1,-1):
				print arr[i][j],
			flag = False
			print '' 



if __name__ == '__main__':
	arr = [[1,2,3,4],
		   [5,6,7,8],
		   [9,10,11,12],
		   [13,14,15,16]]
	PrintZigZag(arr)
