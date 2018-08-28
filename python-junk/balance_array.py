def merge(intervals):

    intervals = sorted(intervals, key = lambda x: x[0])
    print intervals

    stack = []
    stack.append(intervals[0])


    for item in xrange(1, len(intervals)):
        stack_elem = stack.pop()

        if stack_elem[1] >= intervals[item][0]:
            low = min(stack_elem[0], intervals[item][0])
            high = max(stack_elem[1], intervals[item][1])
            stack.append((low, high))
        else:
            stack.append(stack_elem)
            stack.append(intervals[item])

    ans = []
    for item in stack:
        ans.append(item)

    return ans

if __name__ == '__main__':

    intervals = [(1,4), (4,5)]
    print merge(intervals)