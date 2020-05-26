# https://www.geeksforgeeks.org/look-and-say-sequence/
def say(input):
	ans = ''
	count = 1
	i = 0
	while i < len(input):
		while i+1 < len(input) and (input[i] == input[i+1]):
			count += 1
			i += 1
		if count > 1:
			ans = ans + str(count) + input[i]
			count = 1
		else:
			ans = ans + '1' + input[i]
		i += 1
	return ans

n = 3
start = '1'
for i in range(n-1):
	start = say(start)
print(start)
