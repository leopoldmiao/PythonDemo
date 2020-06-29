#coding=utf-8

a = [3, 9, 8, 0]
a.sort()
a.reverse()
print a


b = [3, 9, "china", 8, 0, "beijing"]
b.sort()
b.reverse()
print b


c1 = a+b
c2 = b+a
c1.sort()
c2.sort()
if c1 == c2:
    print "c1 == c2"


print "*"*30
inventory = ["pepperoni", "sausage", "cheese", "peppers"]
shopping_cart = []
item = raw_input("Please give me a topping:")
if item in inventory:
    print "We have {}!".format(item)
    shopping_cart.append(item)
else:
    print "Sorry, we don't have {}".format(item)
item = raw_input("Please give me one more topping:")
if item in inventory:
    print "We have {}!".format(item)
    shopping_cart.append(item)
else:
    print "Sorry, we don't have {}".format(item)
print "Here are your toppings:\n{}".format(shopping_cart)
