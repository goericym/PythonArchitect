# -*- coding: utf-8 -*-
import unittest

from ..ClassDir.can import CAN


class CanTest(unittest.TestCase):

    def test_read(self):
        target = CAN()
        expected = 0  # 預期值
        address = ''
        actual = target.read(address)  # 實際值
        self.assertEqual(expected, actual)

    def test_write(self):
        target = CAN()
        expected = 'abc'  # 預期值
        address = ''
        data = 'abc'
        actual = target.write(address, data)  # 實際值
        self.assertEqual(expected, actual)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
