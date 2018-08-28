import re
import logging
import unittest

logging.basicConfig(format='%(asctime)s %(message)s')

def process_object(input_string):

    course_regex = r'([a-zA-Z]+)[-" ":]?([0-9]+)'
    year_regex = r'([2][0-9]{3}|[0-9]{2})'
    sem_regex = r'(Fall|Winter|Spring|Summer|fall|winter|spring|summer|F|W|S|Su)'

    # sem_year = year+sem or sem+year
    sem_year_regex1 = r'(' + year_regex + r'[" "]?' + sem_regex + r')$'
    sem_year_regex2 = r'(' + sem_regex + r'[" "]?' + year_regex + r')$'

    full_regex1 = course_regex + r'[" "]' + sem_year_regex1
    full_regex2 = course_regex + r'[" "]' + sem_year_regex2

    output_course_object = None

    match1 = re.match(full_regex1, input_string)
    if match1:
        logging.debug(match1.group(0))
        department = match1.group(1)
        course_number = match1.group(2)
        year = match1.group(4)
        semester = match1.group(5)
        output_course_object = Course(department, course_number, semester, year)
    else:
        match2 = re.match(full_regex2, input_string)
        if match2:
            logging.debug(match2.group(0))
            department = match2.group(1)
            course_number = match2.group(2)
            year = match2.group(5)
            semester = match2.group(4)
            output_course_object = Course(department, course_number, semester, year)
        else:
            logging.debug("INVALID COURSE OBJECT")

    return output_course_object

class Course(object):

    def __init__(self, department, course_number,semester, year):
        self.department = department
        self.course_number = course_number
        self.year = year
        self.semester = semester

    def print_course(self):
        print 'Department:', self.department
        print 'Course Number:', self.course_number
        print 'Year:', self.year
        print 'Semester:', self.semester

    def compare_courses(self, course):

        if course is None or self is None:
            logging.debug("Course object is None")
            return False

        if (self.department == course.department and
           self.course_number == course.course_number and
           self.year == course.year and
           self.semester == course.semester):
           return True
        else:
            logging.debug("courses did not match")
            return False

# class to do unit testing of Course Object
class Test_Course(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS-101 Fall2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

    def test_2(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS-101 Fall 2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

    def test_3(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS-101 F2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

    def test_4(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS-101 F2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

    def test_5(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS,101 F2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

    def test_6(self):
        c1 = Course('CS', '101', 'Fall', '2010')
        c2 = process_object('CS:101 Fall2010')
        if c2 is not None:
            c2.print_course()
            self.assertEqual(c1.compare_courses(c2), True)
        else:
            raise Exception('Invalid Object')

if __name__ == '__main__':
    unittest.main()