# -*- coding: utf-8 -*-
from communication import SelectComm
from data import DATA


class ACTION(object):

    def __init__(self, args):
        # print args
        o = SelectComm(args)
        self.obj = o.GetComm()

    def dojob(self):
        self.obj.write(0x2, 0x5)
        v1 = self.obj.read(0x2)
        print 'V1=' + str(v1)
        format = DATA()
        v2 = format.dedata(v1)
        print 'V2=' + str(v2)
        return True


if __name__ == '__main__':# pragma: no cover
    a = ACTION('CAN')
    a.dojob()
    a = ACTION('RS232')
    a.dojob()
