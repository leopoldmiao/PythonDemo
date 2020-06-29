#coding=utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

x = u"哈哈"    #u加在前面表示将字符串先转化为unicode码
print x

#########################################中文处理的方式

print "Hello World!"

a = 5
print a
b = type(a)
print b
print 5+3
price = 10.0
num = 5
discount = 0.7
tax_rate = 0.05
carriage = 7.5
total = price*discount*num*(1+0.05)+7.5
print u"Total cost is {}, 含税，税率为 {} ".format(total,tax_rate) #用format提供输出变量。
