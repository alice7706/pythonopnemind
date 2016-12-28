# -*- coding:utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
#raw_input()输入的默认为字符串，不做其他操作。


print "So,you're %r old,%r tall and %r heavy." % (age,height,weight)

print "So,you're %s old,%s tall and %s heavy." % (age,height,weight)

#如果输入的时候有单引号和双引号，那么%s和%r会是两种不同的输出效果。%r会自动加上\来区别

#print  raw_input("where r u")
print "6'2\""
