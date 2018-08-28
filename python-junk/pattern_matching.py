import requests

# find whether str1 is subsequence of str or not
def is_subsequence(str1, str2):
    if str1 is None or str2 is None:
        return False

    j = 0
    i = 0
    while i < len(str2) and j < len(str1):
        if str1[j] == str2[i]:
            j += 1
        i += 1

    return j == len(str1)


# Naive string pattern matching
# http://www.geeksforgeeks.org/?p=11871
def is_substring_naive(pattern, text):

    if pattern is None or text is None:
        return 'Invalid input'

    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len == 0:
        return False

    for i in xrange(text_len - pattern_len + 1):
        j = 0
        while j < pattern_len:
            if pattern[j] != text[i + j]:
                break
            j += 1
        if j == pattern_len:
            print 'Pattern match found at = ' , i


# 2: http://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/
# Based on hashing

# Complete the function below.

# Wrapper HTTP_GET function
BASE_URL = 'https://jsonmock.hackerrank.com/api/movies/search/?'
# Wrapper HTTP_GET function
def httpGet(url):
    ret = requests.get(url)
    return ret

# To check whether we have got 200 OK response or not
def response_is_ok(inp):
    if inp.status_code != requests.codes.ok:
        print "ERROR - Expected HTTP Status 200.  Instead got:"
        print inp
        print inp.text
        return False
    return True



def solution(substr):
    params = 'Title=' + substr
    URL = BASE_URL + params

    response = httpGet(URL)
    if not (response_is_ok(response)):
        print 'ERROR: Unable to make reuqest'

    obj = response.json()
    total_records = obj['total']
    total_pages = obj['total_pages']
    per_page = obj['per_page']
    output = []

    # for page1
    for i in obj['data']:
        if substr in i['Title']:
            output.append(i['Title'])

    if total_pages > 1:
        count = 2
        params = 'Title=' + substr + '&' + 'page=' + str(2)
        count += 1
        URL = BASE_URL + params
        response = httpGet(URL)
        if not (response_is_ok(response)):
            print 'ERROR: Unable to make reuqest'

        obj = response.json()
        total_records = obj['total']
        total_pages = obj['total_pages']
        per_page = obj['per_page']
        output = []




if __name__ == '__main__':

    # is_subsequence
    # print is_subsequence('geeksgeeks','geeksforgeeks')
    # print is_subsequence('abc', 'aprqstbtuvw')
    # print is_subsequence('abc', 'aaabbc')
    # print is_subsequence('a','b')
    # print is_subsequence('a', '')
    # print is_subsequence('geeks', 'geeges')

    # is_substring_naive('abc', 'abc')
    # is_substring_naive('abc','abcabdsdfkabcasd')
    solution('abcd')
