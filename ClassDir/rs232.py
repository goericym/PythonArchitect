# -*- coding: utf-8 -*-
from interface import IInterface


class RS232(IInterface):
    v = 0

    def read(self, address):
        return self.v
        
    def write(self, address, data):
        self.v = 'wr'
        return self.v

if __name__ == '__main__':
    i = RS232()
    print i
    print i.write(0x2, 0x45)
    print i.read(0x2)
