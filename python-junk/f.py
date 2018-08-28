from collections import deque
import Queue

class My_Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if self.is_empty() != True:
            item = self.stack[-1]
            return item
        return None

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.is_empty() != True:
            return self.stack.pop()
        return None

class My_Queue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, item):
        self.queue.append(item)

    def peek(self):
        if self.is_empty() != True:
            item = self.stack[0]
            return item
        return None

    def size(self):
        return len(self.queue)

    def dequeue(self):
        if self.is_empty() != True:
            # remove first element of the list
            return self.queue.pop(0)
        return None

class Job(object):

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:', description
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

if __name__ == '__main__':

    # s = My_Stack()
    # s.push(10)
    # s.push(20)
    # s.push(30)
    # print s.size()
    # print s.pop()
    # print s.pop()
    # print s.pop()
    # print s.size()
    # print s.pop()
    # print s.size()

    # q = My_Queue()
    # q.enqueue(10)
    # q.enqueue(20)
    # q.enqueue(30)
    # print q.size()
    # print q.dequeue()
    # print q.size()
    # print q.dequeue()
    # print q.dequeue()
    # print q.dequeue()
    # print q.size()

    # https://pymotw.com/2/Queue/
    # Using Queue module as Queue
    # q = Queue.Queue()
    # for i in xrange(5):
    #     q.put(i+1)
    # print q
    # print q.qsize()
    # while not q.empty():
    #     print q.get()

    # Using Queue module as stack
    # stack = Queue.LifoQueue()
    # for i in xrange(5):
    #     stack.put(i+1)
    # print stack
    # print stack.qsize()
    # while not stack.empty():
    #     print stack.get()
    # print stack.qsize()

    # Using Queue module as Priority queue
    q = Queue.PriorityQueue()

    q.put(Job(3, 'Mid-level job'))
    q.put(Job(10, 'Low-level job'))
    q.put(Job(1, 'Important job'))

    while not q.empty():
        next_job = q.get()
        print 'Processing job:', next_job.description


    # double ended queue
    # https://pymotw.com/2/collections/deque.html
    dq = deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    print dq

    while True:
        try:
            print dq.pop()
        except IndexError:
            break

    dq.appendleft(10)
    dq.appendleft(20)
    dq.appendleft(30)
    print dq

    while True:
        try:
            print dq.popleft()
        except IndexError:
            break