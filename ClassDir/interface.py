# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): print "1.0"

    @abstractmethod  # 一定要實作
    def read(self, arg):
        pass

    @abstractmethod  # 一定要實作
    def write(self, arg):
        pass


class fakeforTest(IInterface):
    v = 0

    def read(self, address):
        print self.v

    def write(self, address, data):
        self.v = data
        print self.v
if __name__ == '__main__':
    i = fakeforTest()
    i.write(0x2, 0x45)
    i.read(0x2)
