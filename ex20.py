# -*- coding:utf-8 -*-
from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def  rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline(),
    #有没有最后一个，是有差异的。没有，的情况下，ｐｒｉｎｔ语句结束的时候会打印一个＼ｎ
    #如果有，则ｐｒｉｎｔ挂住，停留在原地，不回车。
    #ｒｅａｄｌｉｎｅ（），会输出，直到遇到＼ｎ后。所以如果没有，则每次调用这个函数，
    #会打印２个回车，而如果有，则只打印１个回车。




current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)
