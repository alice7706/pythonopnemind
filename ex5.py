# -*- coding:utf-8 -*-
name =  'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
g_height = height*100
g_weight = weight*3.1

print "Let's talk about %r." % name
#%r 和 %s 最后出来的效果是不同的。%r输出的是'Zed A.Shaw'
#%s 输出的是 Zed A.Shaw。有引号和没有引号。目前还是不太明白两者有什么差别。

print "He's %r inches tall." % g_height
#这里的%r和%d的效果是一样的。

print "He's %d pounds heavy." % g_weight
print "Actually that's not too heavy."
print "He's got %s eyes and  %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth
#this line is tricky, try to get it exactly right
print "If I add %d,%d, and %d I get %d." % (age,height,weight,age + height + weight)
