#coding=utf-8

def add(mylist):
    mylist[0]=mylist[0]+1
    print "list in function is{}".format(mylist)

a = [1,2,3]
print "list before function is {}".format(a)
add(a)
#print "list out of function is {}".format(mylist)
print "list after function is {}".format(a)

print "*"*30
########################################################

def add(x):
    x=x+1
    print "int in function is{}".format(x)

x = 5
print "int before function is {}".format(x)
add(x)
print "int after function is {}".format(x)

print "*"*30
########################################################

namelist = ["a", "b", "c", "d"]
def check(name):
    if name in namelist:
        return True
    else:
        return False

def main():
    print "Welcome to the student checker!"
    while True:
        name = raw_input("Please give me the name of a student (enter 'q' to quit):")
        if name == 'q':
            print "Goodbye!"
            break
        if check(name):
            print "Yes, that student is enrolled in the class!"
        else:
            print "No, that student is not in the class."

if __name__ == "__main__":
    main()




