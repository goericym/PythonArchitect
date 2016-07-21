# -*- coding: utf-8 -*-


class DATA(object):

    def endata(self,args):
        return args

    def dedata(self,args):
        return args
if __name__ == '__main__':# pragma: no cover
    d=DATA()
    print d.dedata(0x3)
    print d.endata(0x3)