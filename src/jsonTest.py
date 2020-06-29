#coding=utf-8
import os
import json

class Items(object):
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self,name="", num=0):
       '''
       add item to items
       :param name:
       :param num:
       :return:
       '''
       #get correct name and num of new item
       c_name = name
       c_num = num
       while not name:
           name = raw_input("Please give me the item's name:")
           c_name = name

       while num <= 0:
           while True:
               num = raw_input("Please give me {}'s number:".format(c_name))
               try:
                   num = int(num)
                   c_num = num
                   break
               except:
                   print "I'm sorry. but {} is not valid.".format(num) #不想打印的话，就用pass直接过也可以。

       # already has the item, just add the num of the item
       if self.items.has_key(c_name):
           self.items[c_name] = self.items[c_name] + c_num
       # don't has the item, add the item and its num to the dictionary
       else:
           self.items[c_name] = c_num
       # add the number of all things
       self.total = self.total + c_num

def main():
    my_store = Items()
    my_store.add_item(name = "book", num = 5)
    my_store.add_item(name = "book", num = 1)
    my_store.add_item(name = "food",num = 20)
    my_store.add_item(name = "dfsljflajdslfjaljfdlajlfjaljflakj",num = 1)

    keys = my_store.items.keys()
    keys.sort()
    for key in keys:
        item_str = "{}\t{}".format(key,my_store.items[key])
        print item_str

    cwd = os.getcwd()
    print "*"*30
    print "current directory is {}".format(cwd)

    try:
        os.makedirs("D:\\Test\\hello")
    except:
        print "direction is already existec"

    f = open("D:\\Test\hello\\t2.json", "w+")

    print json.dumps(my_store.items, indent = 2)

    json.dump(my_store.items, f, indent = 2)

    f.close()

    f = open("D:\\Test\hello\\t3.json", "w+")

    print json.dumps(vars(my_store), indent=2) #用vars能够将对象的属性构成一个字典，但是仅限于属性值为简单的非对象或非对象列表。
    # 如果是对象或对象列表，则需要将其转化为字典，然后用vars才能获得整体的字典，或者干脆写一个函数替代vars的功能，自己转化整个对象为字典。

    json.dump(vars(my_store), f, indent=2)

    f.close()

if __name__ == "__main__":
    main()
