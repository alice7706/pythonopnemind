# -*- coding:utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"
# 定义函数。函数的ａｒｇｕｍｅｎｔ（参数），在定义的时候一并定义
# %d 显示整数。

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#调用的时候，直接赋予参数数值。

print "OR, we can use variables from our script:"
amount_of_cheese = int(raw_input(">:"))
amount_of_crackers = int(raw_input(">:"))
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#调用的时候，通过主函数的参数值，赋予调用函数参数值。

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#也可以直接将数学运算式的结果赋予函数的参数值。

print "And we can combine the two, varialbes and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#也可以将上述的方式结合起来使用
