#!/usr/bin/python
# -*- coding: utf-8 -*-

# from sys import argv

# this one is linke your scipts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that "args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %s" % arg1

# this jusn takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1


# this one take no arguments
def print_none():
    print "I got nothing."

print_two("aaa", "bbb")
print_two_again("ccc", "ddd")
print_one("First!")
print_none()
