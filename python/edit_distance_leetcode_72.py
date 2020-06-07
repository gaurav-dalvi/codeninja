# https://www.geeksforgeeks.org/edit-distance-dp-5/
# https://leetcode.com/problems/edit-distance/
# https://www.youtube.com/watch?v=We3YDTzNXEk
# key is to think from the end of the string, otherwise becomes messy with indices of both string

def edit_distance_recursive(source, destination, m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if source[m] == destination[n]:
		return edit_distance_recursive(source, destination, m-1, n-1)
	else:
		delete_count = edit_distance_recursive(source, destination, m-1, n)
		replace_count = edit_distance_recursive(source, destination, m-1, n-1)
		insert_count = edit_distance_recursive(source, destination, m, n-1)
		return 1 + min(delete_count, replace_count, insert_count)

# source='rosrose'
# destination='rose'
# print(edit_distance_recursive(source, destination, len(source)-1, len(destination)-1))

# source='sunday'
# destination='saturday'
# print(edit_distance_recursive(source, destination, len(source)-1, len(destination)-1))

source='geek'
destination='gesek'
print(edit_distance_recursive(source, destination, len(source)-1, len(destination)-1))


