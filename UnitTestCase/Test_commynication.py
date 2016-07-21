# -*- coding: utf-8 -*-

import unittest
from ..ClassDir.communication import SelectComm
from ..ClassDir.can import CAN
from ..ClassDir.rs232 import RS232
class SelectCommTest(unittest.TestCase):

    def test_GetComm_Can(self):
        target = SelectComm('CAN')
        expected = CAN()  # 預期值
        actual = target.GetComm()  # 實際值
        self.assertEqual(type(expected), type(actual))

    def test_GetComm_Rs232(self):
        target = SelectComm('RS232')
        expected = RS232()  # 預期值
        actual = target.GetComm()  # 實際值
        self.assertEqual(type(expected), type(actual))

if __name__ == '__main__':
    unittest.main()
