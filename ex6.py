# -*- coding:utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y
#���x��y����ͬһ��print ��䣬��û�лس���ֱ�����仰����һ�������

print "I said: %r." % x
print "I also said: '%s'." % y
#%r��%s������r�ǽ�����һ�����������Ϊ��ȫ����s��ֻ��ȡ���е��ַ������֡����������š�
#ע��ڶ���������Ǽ���ȥ��


hilarious = False
#��python�� False ��false��ͬ��False��ר�����ʡ�
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# print ��Isn't that joke so funny?! %r�� % False


w = "This is the left side of..."
e = "a string with a right side."

print w+e
# + ���������ַ������ӷ�
