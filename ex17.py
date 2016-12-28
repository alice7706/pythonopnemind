# -*- coding:utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s:" % (from_file,to_file)

#we could do these two on one line,how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bye long" % len(indata)
#%d 打印整数
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done"

#out_file.close()
#in_file.close()
#为什么文件要close。从网上看到的答案是python认为，打开的文件对象就是应该用完后关闭的
#这是一种好的行为习惯。当项目很大的时候，这种习惯会帮到你大忙。
