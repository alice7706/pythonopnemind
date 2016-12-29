# -*- coding:utf-8 -*-
# this one is like your scripts with argv
def printtwo(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def printtwoagain(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


printtwo("Zed","Shaw")
printtwoagain("Zed","Shaw")
print_one("First!")
print_none()
