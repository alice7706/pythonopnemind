# -*- coding:utf-8 -*-
from sys import argv
#获取argv的内容。取得一段字符串。sys是调用内部模块。

script, filename =argv
#argv由两个部分组成，第一个部分都是默认的，就是脚本的名称，脚本指的是.py这个东东。
#argv的第二个部分是输出的字符串。

txt = open(filename)
#open模块会打开一个文件，并将这个文件赋予txt这个对象。txt因此就打开了ex_sample.txt
#这个文件

print "Here is your script:%r" % script
#这是我为了搞懂script指的是什么，而输出的。

print "Here is your file %r:" % filename


print txt.read()
txt.close()
#执行read()函数，txt是一个文件对象，有内置的函数
#txt.write("hello,world!")
#txt.close()

#print "Type the filename again:"
#file_again = raw_input(">")

#txt_again = open(file_again)

#print txt_again.read()
#txt_again.close()
