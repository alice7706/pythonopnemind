# -*- coding:utf-8 -*-
from sys import argv
#��ȡargv�����ݡ�ȡ��һ���ַ�����sys�ǵ����ڲ�ģ�顣

script, filename =argv
#argv������������ɣ���һ�����ֶ���Ĭ�ϵģ����ǽű������ƣ��ű�ָ����.py���������
#argv�ĵڶ���������������ַ�����

txt = open(filename)
#openģ����һ���ļ�����������ļ�����txt�������txt��˾ʹ���ex_sample.txt
#����ļ�

print "Here is your script:%r" % script
#������Ϊ�˸㶮scriptָ����ʲô��������ġ�

print "Here is your file %r:" % filename


print txt.read()
txt.close()
#ִ��read()������txt��һ���ļ����������õĺ���
#txt.write("hello,world!")
#txt.close()

#print "Type the filename again:"
#file_again = raw_input(">")

#txt_again = open(file_again)

#print txt_again.read()
#txt_again.close()
