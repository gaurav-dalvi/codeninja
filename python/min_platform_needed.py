# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# This of merg function in merge sort.

def min_platforms(arrs):

	arrival = arrs[0]
	departures = arrs[1]
	arrival.sort()
	departures.sort()
	result = 1
	min_plat = 1
	i = 1
	j = 0
	while i < len(arrival) and j < len(departures):
		if arrival[i] < departures[j]:
			i += 1
			min_plat += 1
			if min_plat > result:
				result = min_plat
		else:
			j += 1
			min_plat -= 1
	
	return result

arr  = [9.00,  9.40, 9.50,  11.00, 15.00, 18.00]
dep  = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
arrs = [arr, dep]
print min_platforms(arrs)
