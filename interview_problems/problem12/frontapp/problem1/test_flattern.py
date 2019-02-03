import unittest
from flattern import flattern

class FlatternTestCase(unittest.TestCase):
    """Tests for `flattern.py`."""

    def test_no_need_flat(self):
        """When there are no nested lists in the given input"""
        temp = []
        inp = [1,2,3,4,5]
        output = [1,2,3,4,5]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_empty_list(self):
        """Empty list as input"""
        temp = []
        inp = []
        output = []
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_one_elem_list(self):
        """One element list as input"""
        temp = []
        inp = [1]
        output = [1]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_null_list(self):
        """null list as input"""
        temp = None
        inp = None
        output = None
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_single_element_list(self):
        """each element is list"""
        temp = []
        inp = [[1],[2],[3],[4],[5]]
        output = [1,2,3,4,5]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_random_empty_list(self):
        """any item is empty list"""
        temp = []
        inp = [[1],[],[2,3,4,5]]
        output = [1,2,3,4,5]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_nested_list(self):
        """nested list"""
        temp = []
        inp = [1,[2,[3,4]], 5]
        output = [1,2,3,4,5]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

    def test_more_deep_nested_list(self):
        """Deep nested list"""
        temp = []
        inp = [1,[2,[3,4],[5,[[[6]],[7,[8]]]]], 9]
        output = [1,2,3,4,5,6,7,8,9]
        flattern(inp, temp)
        print('Given input {}, output {} '.format(inp, temp))
        self.assertEqual(temp, output)

if __name__ == '__main__':
    unittest.main()