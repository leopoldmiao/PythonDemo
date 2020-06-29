#coding=utf-8

print "Welcome to the receipt program!"
total =0.0
price =0.0
while True:
    price_str = raw_input("Enter the value for the seat ['q' for quit]:")
    if price_str == "q":
        break
    if not price_str.replace(".", "", 1).isdigit():  #判断输入是否为数字
        print "I'm sorry, but {} isn't valid. Please try again.".format(price_str)
    else:
        price = float(price_str)
        total = total + price
print "*"*5
print "Total: ${}".format(total)



#其实上面对price的转化可以直接用下面的代码
#try:
#    price = float(price)
#    break
#except:
#    print "I'm sorry. but {} is not valid.".format(price)
