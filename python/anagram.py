# Given a list of words group them together if they are anagram of each other.
# Do frequency counting on each word and then put in hashMap.
# find frequency of each work and check if exists in hashmap or not.

def GroupAnagram(wordList):

    op = {}
    for word in wordList:
        fr = findReqency(word)
        if op.has_key(fr):
            temp = op.get(fr)
            temp.append(word)
            op[fr] = temp
        else:
            op[fr] = [word]
    return op.values()

def findReqency(word):
    freqList = [0] * 26
    for i in word:
        freqList[ord(i) - ord('a')] = 1
    #print ''.join(str(e) for e in freqList)
    return ''.join(str(e) for e in freqList)

if __name__ == '__main__':

    l = ['abc','pqr','cab','rqp','gau','rav']
    dict = GroupAnagram(l)
    print dict
