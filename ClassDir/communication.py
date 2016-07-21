# -*- coding: utf-8 -*-
from rs232 import RS232
from can import CAN


class SelectComm(RS232, CAN):

    def __init__(self, args):  # init不能回傳值
        self.obj = None
        if args == 'CAN':
            self.obj = CAN()
        else:
            self.obj = RS232()

    def GetComm(self):
        return self.obj

if __name__ == '__main__':# pragma: no cover
    i = SelectComm('CAN')
    c = i.GetComm()
    print c
    print c.write(0x2, 0x45)
    print c.read(0x2)
    i = SelectComm('RS232')
    r = i.GetComm()
    print r
    print r.write(0x2, 0x45)
    print r.read(0x2)
