# -*- coding: utf-8 -*-
from interface import IInterface


class CAN(IInterface):
    v = 0

    def read(self, address):
        return self.v

    def write(self, address, data):
        self.v = data
        # self.v='wc'
        return self.v

if __name__ == '__main__':# pragma: no cover
    i = CAN()
    i.write(0x2, 0x45)
    i.read(0x2)