# coding=utf-8


from nose.tools import *
import NAME
# from name import color


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"


# def test_paint():
#     color.paint("blue")