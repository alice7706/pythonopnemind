# -*- coding:utf-8 -*-
tabby_cat = "\tI'm tabbed in."
#\t һ��tabλ
persian_cat = "I'm split \non a line."
#\n ����
backslash_cat = "i'm \\ a \\ cat."
#\\��\" \' һ���ķ������á�����������һ��\
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* CAtnip\n\t* Grass\n\t\r*hello world
'''
#"""��ʾ������һ�������ı���ֱ����һ��"""���֡�
#\f��ֽ������ҳ������Ҫֽ���������ʱ����ܿ��õ�Ч����


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","~","|","\\","|"]:
        print "%s\r" % i,
