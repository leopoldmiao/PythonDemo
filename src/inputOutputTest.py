#coding=utf-8
import getpass


a = raw_input("input your age: ")
age = int(float(a))
print age

#user = getpass.getuser()
#print "your name is {}".format(user)
#pwd = getpass.getpass("input your pwd")
#pycharm不支持getpass模块。。。。。。。。


print "*"*30


name_in = raw_input("Give me your name, please:")
name = name_in.strip()
number_in = raw_input("How many widgets are you buying?")
number = int(float(number_in))
price_in = raw_input("How much do they cost, per item?")
price = float(price_in)
total = number*price
print "Your total is ${}\nThanks for shopping with us today, {}!".format(total,name)

