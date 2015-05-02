import unittest
from  src.Main import Main


class testMain(unittest.TestCase):
    
    def test_return_1(self):
        obj = Main()
        self.assertEqual(obj.return_one(),1)




