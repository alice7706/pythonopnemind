# -*- coding:utf-8 -*-
prompt = "input the filename:"
filename = raw_input(prompt)
txt = open(filename)
print "Here is you file:\n %s" % txt.read()
