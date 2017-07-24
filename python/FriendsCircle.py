# Problem : Friends Circle Problem
# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C, then A is also friend of C.
# A friend circle is a group of students who are directly or indirectly friends.
#
# You are given a N X N matrix M which consists of characters Y or N. If M[i][j] = Y, then ith and jth students are
# friends with each other, otherwise not. You have to print the total number of friend circles in the class.
#
# Each element of matrix friends will be Y or N.
# Number of rows and columns will be equal in the matrix.
#
# M[i][i] = Y, where 0<=i<N<=i<N
# M[i][j] = M[j][i], where 0<=i<j<N
#
# Example 1
# Input:
# YYNN
# YYYN
# NYYN
# NNNY
# Output: 2
#
# Example 2
# Input
# YNNNN
# NYNNN
# NNYNN
# NNNYN
# NNNNY
# Output: 5

def friendCircles(friends):
    # make tuple array from friends 2D array
    tupArr = []
    tup = ()
    for i in xrange(len(friends)):
        for j in xrange(len(friends[0])):
            if friends[i][j] == 'Y':
                tup = (i,j)
                tupArr.append(tup)

    print tupArr

    # Now find friends circle
    listUniqueFriends = []

    for i in tupArr:
        found = False
        # Find group
        for j in listUniqueFriends:
            if i[0] in j:
                found = True
                uniqueFriends = j

        if found == False:
            uniqueFriends = set()
            uniqueFriends.add(i[0])
            listUniqueFriends.append(uniqueFriends)

        if i[1] not in uniqueFriends:
            for k in listUniqueFriends:
                if i[1] in k:
                    # union k and uniqueFriends and then push again to list
                    temp = uniqueFriends.union(k)
                    listUniqueFriends.remove(k)
                    listUniqueFriends.remove(uniqueFriends)
                    listUniqueFriends.append(temp)
                    uniqueFriends = temp
            uniqueFriends.add(i[1])


    print listUniqueFriends


if __name__ == '__main__':

    inp = [['Y','Y','Y','N','N','N'],
           ['Y', 'Y', 'Y', 'N', 'N', 'N'],
           ['Y', 'Y', 'Y', 'N', 'Y', 'N'],
           ['N', 'N', 'N', 'Y', 'N', 'N'],
           ['N', 'N', 'Y', 'N', 'Y', 'Y'],
           ['N', 'N', 'N', 'N', 'Y', 'Y'],]

    # inp = [['Y','Y','N', 'N'],
    #        ['Y', 'Y', 'Y', 'N'],
    #        ['N', 'Y', 'Y', 'N'],
    #        ['N', 'N', 'N', 'Y']]


    friendCircles(inp)

