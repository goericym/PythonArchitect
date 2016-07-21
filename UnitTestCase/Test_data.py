# -*- coding: utf-8 -*-
import unittest

from ..ClassDir.data import DATA


class DATATest(unittest.TestCase):

    def test_endata(self):
        target = DATA()
        expected = 0x3  # 預期值
        actual = target.dedata(0x3)  # 實際值
        self.assertEqual(expected, actual)

    def test_dedata(self):
        target = DATA()
        expected = 0x3  # 預期值
        actual = target.dedata(0x3)  # 實際值
        self.assertEqual(expected, actual)        

if __name__ == '__main__':
    unittest.main()
