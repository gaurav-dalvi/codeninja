"""
1. Given a deck of N cards, shuffle them such that every possible ordering is equally likely
def shuffle(deck)

1.1 Implement a MagicMap
Kind of like a HashMap
get(key) //O(1)
set(key, val) //O(1)
delete(key) //O(1)
get_random_val() //O(1)

{
1: 0
2: 1
16: 2
14: 3
}
[(1, 0), (2, 1), (16, 2), (14, 10), (12, 3)]
len = 4

get 16
- get the index from the map => 2
- get the key val pair from arr => (16, 2)
- return (16, 2)[1] => 2

set 14, 10
- check if 14 exists

delete 12
- get the index from the map => 3
- key at the end of the array => 14
- map[14] = 3
- swaps
- decrement len
- remove 12 from map



2. Given a list of intervals, merge the overlapping intervals
[(1, 5), (10, 15), (2, 4), (4, 6)]
=> [(1, 6), (10, 15)]

- brute force
Pick an interval
Go through the array until there are no more merges possible
Every time you merge, remove the interval involved in the merge from the original array
Add the merged interval to the output array

- better?
Sort the intervals by start
Merge consecutive if overlap
If no overlap, add the merged interval to the output
[(1, 5), (12, 15), (2, 4), (4, 11)]
sort => [(1, 5), (2, 4), (4, 11), (12, 15)]
(1, 5) => (1, 11), (12, 15).
[(1, 11), (12, 15)]
O(N.logN), O(N)

- another?
O(N.logN), O(N)
[(1, 5), (12, 15), (2, 9)]
=> [(1, 1), (5, -1), (12, 1), (15, -1), (2, 1), (9, -1)]
sort => [(1, 1), (2, 1), (5, -1), (9, -1), (12, 1), (15, -1)]
As I go over this number line, whenever the cumulative sum of indicators
becomes 0, I have a merged interval.
[(1, 9), (12, 15)]

2.1 Given a list of intervals, and an integer, find out how many intervals
contain the integer.
[(1, 5), (12, 15), (2, 9)], 3 => 2

2.2 Given a list of intervals once and multiple queries are to be made passing
in an integer. For each query, return the number of intervals containing
the given integer.
[(1, 5), (12, 15), (2, 9)]
1 => 1
2 => 2
17 => 0
3 => 2
9 => 1
...
Decouple and sort.
[(1, 1), (2, 1), (5, -1), (9, -1), (12, 1), (15, -1)]
As I go along the number line until I reach the query number,
the cumulative sum is the answer. ** O(N) per query **

- improvement?
[(1, 1), (2, 1), (6, -1), (10, -1), (12, 1), (16, -1)]
Update each value with cumulative sum
=> [(1, 1), (2, 2), (6, 1), (10, 0), (12, 1), (16, 0)]
Binary search for the number less than or equal to the given integer
Return the cumulative sum at that number.

[(1, 1, T), (2, 2, T), (5, 1, F), (9, 0, F), (12, 1, T), (15, 0, F)]


3. Given an array of size N+1 and that all the elements in the array
are in the range [1, N]

3.1 Prove that there has to be at least one repeating element
Pigeon hole principle

3.2 Identify at least one repeating element
- brute force?
Pick each element, check if it repeats
O(N**2), O(1)

- improvements?
Count the occurrences of each number in the range [1, N]
-OR-
Flag for occurrences of each number in the range [1, N]
O(N), O(N)

- improvements?
Use the given array to track the occurrences.
* Mark visited index as negative
* Add N+1 to visited index
* Swapping the values at the visited index
O(N), O(1)

3.2.1 Can you do this assuming it's a read only array and not using additional
memory.
- brute force?
Same as the brute force above

- improvements?
Hint: What can we infer from counting the number of elements <= (1+N)/2 (COUNT_LT)?
[3, 3, 2, 2]
median - 2
COUNT_LT = 3 > median => There is a duplicate element less than or equal to median!!

COUNT_LT = 2 == median => There is a duplicate element greater than median!!

- optimal?
O(N) time
Using Linked List equivalence of an array like this
Why is it necessary that we have N+1 elements in the array??

4. Bomber man



"""


def count_less_than_median(arr, range_start, range_end):
    """Returns the number of elements less than or equal to the median"""
    median = (range_start + range_end) / 2
    count = 0
    for val in arr:
        if val <= median:
            count += 1
    return count


def find_repeating(arr, range_start, range_end):
    """Range start and end are inclusive"""
    if range_start == range_end:
        return range_start

    median = (range_start + range_end) / 2
    if (count_less_than_median(arr, range_start, range_end) <=
            (median - range_start + 1)):
        return find_repeating(arr, median+1, range_end)
    return find_repeating(arr, range_start, median)

# What if there are repeating elements on both sides



def rank(arr, key, start=0, end=None):
    """
    Returns the rank of key in the given array
    end is non-inclusive
    """
    if end is None:
        end = len(arr)

    if start == end:
        return start

    mid = (start+end)/2
    if arr[mid] < key:
        # Strictly less than since we want to return the left most possible
        # occurrence of key if key occurs multiple times in the array.
        # If we want right most, do <=
        return rank(arr, key, mid+1, end)
    return rank(arr, key, start, mid)




def random(end):
    return 0


class MagicMap(object):

    def __init__(self):
        self.map = dict()  # Mapping from key to index in the arr
        self.arr = []  # Every element will be (key, val)
        self.len = 0

    def get(self, key):
        if key not in self.map:
            return None
        return self.arr[self.map[key]][1]

    def set(self, key, val):
        if key not in self.map:
            # Add to the arr
            if self.len == len(self.arr):
                self.arr.append((key, val))
            else:
                self.arr[self.len] = (key, val)
            self.len += 1
            self.map[key] = self.len
        else:
            # Update the val
            self.arr[self.map[key]] = (key, val)

    def delete(self, key):
        idx = self.map[key]
        # While swapping also move the self.map key pointing to self.len-1 into idx
        self.map[self.arr[self.len-1][0]] = idx
        self.arr[idx], self.arr[self.len-1] = self.arr[self.len-1], self.arr[idx]
        self.len -= 1
        self.map.pop(key)

    def get_random(self):
        # get random from arr and return its value
        pass
