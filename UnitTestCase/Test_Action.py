# -*- coding: utf-8 -*-

import unittest
from ..ClassDir.action import ACTION


class ActionTest(unittest.TestCase):

    def test_Action_ToDo_OnlyRead_Display(self):
        target = ACTION('CAN')
        expected = False  # 預期值
        actual = target.dojob()  # 實際值
        self.assertEqual(expected, actual)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
