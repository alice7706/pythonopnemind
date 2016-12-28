# -*- coding:utf-8 -*-
formatter = "%s %s %s %s"
#观察%s 和%r的区别。
print formatter % (1,2,3,4)
print formatter % ("ond","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
#这里不会形成潜逃吗？不知道会是什么样的效果？

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So i said goodnight."
)
#我想应该会变成一个长长的句子，中间用空格分开。
#没有发现第三句的显示中，会和1、2、4句不同，主要是引号。1、2、4显示是单引号，但是3句显示是双引号
#为什么呢？因为句子3里有单引号吗？
