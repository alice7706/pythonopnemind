# -*- coding:utf-8 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
#观察一下，双引号和单引号的差别在哪里？结果是单引号和双引号没有差别
print "And everywhere that Mary went."
print "."*10
#*号表示，连续做10次这个动作。

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


#watch that comma at the end. try removing it to see what happens.
print end1 + end2 + end3 + end4 + end5 + end6,
#多了一个逗号，会如何呢？
#还记得在上一个练习中，
#print x,y
#print x
#pirnt y
#就是这两者的不同。而用逗号，也可以把两行分开写，但是效果是连接在一起。好像多了一个空格。验证一下吧

print end7 + end8 + end9 + end10 +end11 + end12

print end1,end2
print end1,
print end2
#验证，发现，python输出一个空格
