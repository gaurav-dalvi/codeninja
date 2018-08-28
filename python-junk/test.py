class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x=' + str(self.x) + ' ' + 'y=' + str(self.y)


def slope_of_line(point1, point2):
    y = abs(round(float(point1.y), 1) - round(float(point2.y), 1))
    x = abs(round(float(point1.x), 1) - round(float(point2.x), 1))
    if x == 0:
        return -1
    return round((y / x), 1)


def check_if_slope_same(my_set, slope, points, index):
    flag = True
    my_set = list(my_set)
    for i in xrange(len(my_set)):
        if slope_of_line(points[my_set[i]], points[index]) != slope:
            flag = False
            break
    if flag == False:
        return False

    return True


def create_sets(my_set, slope, points):
    '''
        Given set of points,
        find list of points who are in same line
        Merging of points of either x or y co-ordinate is in set
    '''

    # convert into list
    my_set = list(my_set)
    my_set.sort(key=lambda x: x[0])
    print my_set
    set_list = []
    dummy_set = set()
    dummy_set.add(my_set[0][0])
    dummy_set.add(my_set[0][1])
    for i in xrange(1, len(my_set)):
        if my_set[i][0] in dummy_set:
            if check_if_slope_same(dummy_set, slope, points, my_set[i][1]) == True:
                dummy_set.add(my_set[i][1])
        elif my_set[i][1] in dummy_set:
            if check_if_slope_same(dummy_set, slope, points, my_set[i][0]) == True:
                dummy_set.add(my_set[i][0])
        else:
            set_list.append(dummy_set)
            dummy_set = set()
            dummy_set.add(my_set[i][0])
            dummy_set.add(my_set[i][1])

    set_list.append(dummy_set)

    #  return a set_list whose sets are more than 2 in size (as per o/p requirement)
    for item in set_list:
        if len(item) <= 2:
            set_list.remove(item)

    print set_list
    return set_list


def gen_op_file(slope_map, points):
    count = 1
    file_name = 'test_output.csv'
    for key in slope_map.keys():
        if len(slope_map[key]) > 2:
            # print key, slope_map[key]
            create_sets(slope_map[key], key, points)


def parse_file(filename):
    if filename is None:
        raise Exception('Filename can not be empty')

    points = []
    with open(filename) as f:
        data = f.readlines()

    data = [x.strip() for x in data]

    for line in data:
        parsed = line.split(',')
        points.append(Point(parsed[0], parsed[1]))

    slope_map = {}
    for i in xrange(len(points)):
        for j in xrange(i + 1, len(points)):
            slope = slope_of_line(points[i], points[j])
            if slope in slope_map.keys():
                slope_map[slope].add((i, j))
            else:
                slope_map[slope] = set()
                slope_map[slope].add((i, j))

    gen_op_file(slope_map, points)


if __name__ == '__main__':
    parse_file('s.csv')
