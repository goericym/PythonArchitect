# -*- coding: utf-8 -*-
# pip install -U selenium
import unittest
from ..ClassDir.rs232 import RS232


class RS232Test(unittest.TestCase):

    def test_Rs232_Read(self):
        target = RS232()
        expected = 0  # 預期值
        actual = target.read(0x3)  # 實際值
        self.assertEqual(expected, actual)

    def test_Rs232_write(self):
        target = RS232()
        expected = 'wr'  # 預期值
        actual = target.write(0x3,0x45)  # 實際值
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
