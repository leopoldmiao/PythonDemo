#coding=utf-8


a = "x\n"
print a,  #没有逗号print会自动换行，有逗号就不换行了，但是我把a的赋值加了一个\n，就抵消了，还是会换行。
print "hello"




b = "**x*y*z"
c = b.strip("*")
print c


print "*"*20
mystr = "I like thethethe dog"
print mystr.count("the")
num = mystr.find("y")
if num != -1:
    print "pos is {}".format(num)
else:
    print "not found"
print mystr.replace("the","a")
print mystr

print "*"*20

#print help(type(b))

email1 = "xxx yyy emergency"
email2 = "xxx  yyy  joke"
email3 = "emergency xxx yyy "
if email1.find("emergency"):   #find返回的是位置0，1，2.。。。。
    print "Do you want to make this email urgent?"
if email2.find("joke"):
    print "Do you want to set this email as non-urgent?"
if email3.find("emergency"):   #find返回的是位置0，1，2.。。。。,此刻返回的是位置0，而数字0代表假，所以打印不出来。
    print "33333333Do you want to make this email urgent?"

#结论，应该使用下面的方式
if email3.find("emergency") != -1:   #find返回的是位置0，1，2.。。。。,此刻返回的是位置0。     找不到返回的是-1
    print "666666Do you want to make this email urgent?"


print "*"*20
astr = "I like thethethe dog"
ul = astr.split(" ")
print ul
