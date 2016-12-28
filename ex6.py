# -*- coding:utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y
#如果x，y放在同一个print 语句，将没有回车，直接两句话连在一起输出。

print "I said: %r." % x
print "I also said: '%s'." % y
#%r和%s的区别，r是将引号一起输出，它认为是全部。s则只是取其中的字符串部分。不包括引号。
#注意第二句里，引号是加上去，


hilarious = False
#在python中 False 和false不同。False是专有名词。
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# print “Isn't that joke so funny?! %r” % False


w = "This is the left side of..."
e = "a string with a right side."

print w+e
# + 在这里是字符串连接符
