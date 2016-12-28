# -*- coding:utf-8 -*-
tabby_cat = "\tI'm tabbed in."
#\t 一个tab位
persian_cat = "I'm split \non a line."
#\n 换行
backslash_cat = "i'm \\ a \\ cat."
#\\和\" \' 一样的反义引用。代表这里有一个\
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* CAtnip\n\t* Grass\n\t\r*hello world
'''
#"""表示这里又一串长的文本，直到下一个"""出现。
#\f进纸键，跳页，可能要纸张输出的是时候才能看得到效果。


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","~","|","\\","|"]:
        print "%s\r" % i,
