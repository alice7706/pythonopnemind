# -*- coding:utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"
# ���庯���������ģ��������������������ڶ����ʱ��һ������
# %d ��ʾ������

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#���õ�ʱ��ֱ�Ӹ��������ֵ��

print "OR, we can use variables from our script:"
amount_of_cheese = int(raw_input(">:"))
amount_of_crackers = int(raw_input(">:"))
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#���õ�ʱ��ͨ���������Ĳ���ֵ��������ú�������ֵ��

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#Ҳ����ֱ�ӽ���ѧ����ʽ�Ľ�����躯���Ĳ���ֵ��

print "And we can combine the two, varialbes and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#Ҳ���Խ������ķ�ʽ�������ʹ��
