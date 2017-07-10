import sys

def maxPathSum(arr, i, j):

	col = len(arr[0])
	row = len(arr)
	if i < 0 or i >= row or j < 0 or j >= col:
		return 0
	elif i == row-1 and j == col-1:
		return arr[i][j]
	else:
		sum1 = maxPathSum(arr, i, j+1)
		sum2 = maxPathSum(arr, i+1, j)
		return max(sum1,sum2) + arr[i][j]

if __name__ == '__main__':
	
	arr = [[5,0,8,12],
		   [11,16,9,13],
		   [10,2,15,300],
		   [3,14,18,19],
		   [4,6,7,20]]

	print maxPathSum(arr,0,0)
