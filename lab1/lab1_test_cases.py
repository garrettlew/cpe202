import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    """Max Iter Tests"""
    def test_max_list_iter01(self):
        """None test"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter02(self):
        """Empy test"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter03(self):
        """1 element test"""
        tlist = [10]
        self.assertEqual(max_list_iter(tlist), 10)

    def test_max_list_iter04(self):
        """Max at front test"""
        tlist = [7, 1, 6, 3, 4]
        self.assertEqual(max_list_iter(tlist), 7)

    def test_max_list_iter05(self):
        """Max at end test"""
        tlist = [1, 1, 6, 3, 8]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_max_list_iter06(self):
        """Max at end test"""
        tlist = [1, 1, 1, 1, 8]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_max_list_iter07(self):
        """Neg test"""
        tlist = [-11, -31, 1, 0, -3]
        self.assertEqual(max_list_iter(tlist), 1)

    """ Reverse Rec Tests """
    def test_reverse_rec01(self):
        ''' Fliperoni 3 elements '''
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec02(self):
        ''' None input '''      
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec03(self):
        ''' Fliperoni 1 elements '''
        self.assertEqual(reverse_rec([100]),[100])

    def test_reverse_rec04(self):
        ''' Fliperoni 0 elements '''
        self.assertEqual(reverse_rec([]),[])

    def test_reverse_rec05(self):
        ''' Fliperoni 2 elements '''
        self.assertEqual(reverse_rec([5, 2]),[2, 5])

    def test_reverse_rec06(self):
        ''' Fliperoni 5 elements out of order '''
        self.assertEqual(reverse_rec([6, -8, 1, 24, 2]),[2, 24, 1, -8, 6])

    """ Binary Search Tests """
    def test_bin_search01(self):
        ''' Target init at middle '''
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )

    def test_bin_search02(self):
        ''' None input '''      
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 6, tlist)

    def test_bin_search03(self):
        ''' None input 2 '''      
        tlist = None
        low = 0
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(2, low, 0, tlist)

    def test_bin_search04(self):
        ''' Target 404 '''
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(400, low, high, list_val), None )

    def test_bin_search05(self):
        ''' Empty list '''
        list_val =[]
        low = 0
        self.assertEqual(bin_search(1, low, 5, list_val), None )

    def test_bin_search06(self):
        ''' Target at end '''
        list_val =[7,1,6,3,4,5,8,91,20]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(20, low, high, list_val), 8 )

    def test_bin_search07(self):
        ''' Target at beginning '''
        list_val =[-1,12,6,3,4,5,8,91,20,100]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-1, low, high, list_val), 0 )

    def test_bin_search08(self):
        ''' Target at beginning but out of scope '''
        list_val =[-1,12,6,3,4,5,8,91,20,100]
        low = 1
        high = len(list_val)-1
        self.assertEqual(bin_search(-1, low, high, list_val), None )

    def test_bin_search09(self):
        ''' Target at end but out of scope '''
        list_val =[-1,12,6,3,4,5,8,91,20,100,11]
        low = 2
        high = 9
        self.assertEqual(bin_search(11, low, high, list_val), None )

    def test_bin_search10(self):
        ''' Target one left from center '''
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, low, high, list_val), 2)

    def test_bin_search11(self):
        ''' Target one right from center '''
        list_val = [8, 7, 6, 5, 4, 3, 2, 1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search12(self):
        ''' Target left from center '''
        list_val = [8, 7, 6, 9, 4, 20, 2, 1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(7, low, high, list_val), 1)

    def test_bin_search13(self):
        ''' Target right from center '''
        list_val = [1, 20, 3, 4, 50, 6, 7]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(6, low, high, list_val), 5)

if __name__ == "__main__":
        unittest.main()

    
