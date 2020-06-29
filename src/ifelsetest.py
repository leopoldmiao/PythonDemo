#coding=utf-8


user_account = 100

if user_account > 0:
    print "You have money!"
elif user_account ==0:
    print "You are out!"
else:
    print "You seem to be in debt!"


a = ""
#a = 100
#a = "haha"
a = None
if a:
    print type(a)
    print "haha"
print type(a)