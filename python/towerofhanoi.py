def MoveTower(disc, so, dest, temp):
    if disc == 1:
        print 'Moving disc ', disc , 'from '+ so + ' to ' + dest
        return
    else:
        MoveTower(disc -1 , so, temp, dest)
        print 'Moving disc ', disc, 'from ' + so + ' to ' + dest
        MoveTower(disc - 1, temp, dest, so)

if __name__ == '__main__':
    discs = 2
    MoveTower(discs,'A', 'C', 'B')