'''
How to run this program:
1: To generate random file for testing:
./s.sh <total numbers in the file>
ef: ./s.sh 100 -> this will print 100 random numbers on the screen

2: After this you can run topK.py program in python2 env
python topK.py <file> topKNumber


Design of this Program:

To find topK elements from big file, we assume following things:
1: file size is very large as compared to topK.
2: topK elements can be fit into main memory
3: each sub file can be loaded into main memory and then we work on it.
4: large file can not be loaded into main memory and opened during the lifetime of program

Design:
If the file size is greater than our threashold (max file size that can be loaded into main memory),
we split the file into chunks.
Then for each file, we create min heap of first k elements. For next numbers in that file,
we check if incoming number is greater than root of min heap, then we remove root and 
insert this new incoming number. Because of this, we get topK elements from that file
at the end of processing. Order of those numbers in the heap are NOT in the descending order

After we get these min_heaps from all files, we collect them in big array (size = topK * MAX_THREADS)
We sort this big array in descending order.

Output = first topK elements from this array.

Alternative approach:
1: create max_heap from each file
2: merge these max_heaps into new max_heap of size topK.

'''
import heapq
import sys
import glob
import os
import threading

SPLIT_FILE_PREFIX = 'split_file_'
THRESHOLD_FILE_SIZE = 100000000
MAX_THREADS = 10
WHITE_SPACES = ['\n', ' ', '', '\t', '\r']
all_min_heaps = []

# From given file and K, create min heap of k elements.
# if incoming number is greater than root of heap then replace it,
# resulting top k elements from that file
# complexity of this function:
# 1: complexity to form min heap = O(k)
# 2: complexity of heapify = O(log k)
# Total complexity for checking N elements from the file = O(Nlog K)
def create_min_heap_from_file(file_name, topK):

	with open(file_name, "r") as file_ds:
		lines = file_ds.readlines()

	if len(lines) < topK:
		raise Exception('topK={} is greater than total numbers {} in the file'.format(topK, len(lines)))
	
	min_heap_arr = []
	index = 0
	while index < len(lines):
		if lines[index] not in WHITE_SPACES:
			while len(min_heap_arr) != topK:
				min_heap_arr.append(int(lines[index]))
				heapq.heapify(min_heap_arr)	
				index += 1
			if int(lines[index]) >= min_heap_arr[0]:
				# remove this, add new number and do hepify again
				min_heap_arr[0] = int(lines[index])
				heapq.heapify(min_heap_arr)
		index += 1
	return min_heap_arr

# if file is binner than THRESHOLD_FILE_SIZE, then split into MAX_THREADS number of files
# we dont want to create too many threads, as it might not give better performance after certain limit
def split_files(file_name):
	file_size = os.path.getsize(file_name)
	each_file_size = int(file_size/MAX_THREADS)
	if file_size > THRESHOLD_FILE_SIZE:
		print('Going to split {} file into files of size {} each'.format(file_name, each_file_size))
		# split files in to chunks
		cmd = 'split -b {} {} {}'.format(each_file_size, file_name, SPLIT_FILE_PREFIX)
		print(cmd)
		execute_shell_command(cmd)

# get the list of split file names
def get_list_of_files(file_name):
	split_files(file_name)
	files = glob.glob(SPLIT_FILE_PREFIX+'*')
	if len(files) > 0:
		return files
	return [file_name]

# to execute any shell command in python
def execute_shell_command(cmd):
	ret = os.system(cmd)
	if ret != 0:
		raise Exception('Executing {} command resulted in failure'.format(cmd))

# after having topK elements from all split files, we will put all elements in array
# sort array in descending order.
# time complexity of this function is : O(klog k), k = topK elements requested, because of sorting
def join_all_heaps(all_heaps, topK):
	max_array = []
	for heap in all_heaps:
		while len(heap) != 0:
			max_array.append(heapq.heappop(heap))
	return sorted(max_array, reverse=True)[:topK]

# Threading class to run each file processing in parallel
class FileThread (threading.Thread):
   
   def __init__(self, name, topK):
      threading.Thread.__init__(self)
      self.name = name
      self.topK = topK
      
   def run(self):
      print('Starting ' + self.name)
      heap = create_min_heap_from_file(self.name, self.topK)
      threadLock.acquire()
      all_min_heaps.append(heap)
      threadLock.release()
      print('Exiting ' + self.name)

# main function
if __name__ == '__main__':

	if len(sys.argv) != 3:
		raise Exception('Filename  and K must be specified')

	file_name = sys.argv[1]
	if sys.argv[2] in WHITE_SPACES:
		raise Exception('Invalid value for topK number')
	try:
		topK = int(sys.argv[2])
	except ValueError:
		raise Exception('Invalid value for topK number')
	
	files = get_list_of_files(file_name)
	if len(files) == 1:
		min_heap = create_min_heap_from_file(files[0], topK)
		print 'Top {} elements from the file {} are {}'.format(topK, file_name, sorted(min_heap))
	else:
		threads = []
		threadLock = threading.Lock()
		index = 0
		for file in files:
			t = FileThread(file, topK)
			threads.append(t)
		
		for t in threads:
			t.start()
		
		for t in threads:
			t.join()
		
		print join_all_heaps(all_min_heaps, topK)
		
		# clean up the split files
		for file in files:
			os.remove(file)