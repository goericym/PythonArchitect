# -*- coding: utf-8 -*-
from ClassDir.action import ACTION
import os,time

if __name__ == '__main__':# pragma: no cover
    a = ACTION('CAN')
    a.dojob()
    b = ACTION('RS232')
    b.dojob()