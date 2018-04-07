# https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/
# Generate binary numbers from 1 to n
# Key learnings :
# 1: How to use Queue data strucutre : Its FIFO
# 2: Add 1 in Queue
# 3: Now run for loop for n number of times
# 4: Remove from queue and print
# 5: Append 0 enqueue It
# 6: Append 1 enqueue It

import Queue

def generate_numbers(n):

	q = Queue.Queue()
	if n > 0:
		q.put('1')
		while n > 0:
			 n = n - 1
			 s1 = q.get()
			 print s1
			 s2 = s1
			 q.put(s1+'0')
			 q.put(s2+'1')

if __name__ == '__main__':
	generate_numbers(6)
