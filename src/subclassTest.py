#coding=utf-8

class InventoryItem(object):
    def __init__(self, title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, other):
        if self.store_id == other.store_id:
            return True
        else:
            return False

    def change_description(self, description = ""):
        if not description:
            description = raw_input("Please give me a description: ")
            self.description = description

    def change_price(self, price = -1):
        while price<0:
            price = raw_input("Please give me the new price [x.xx]: ")
            try:
                price = float(price)
                break
            except:
                print "I'm sorry. but {} is not valid.".format(price)
        self.price = price

    def change_title(self, title = ""):
        if not title:
            title = raw_input("Please give me a new title:")
        self.title = title


class Software(InventoryItem):
    def __init__(self, title, description, price, store_id, os, ESRB):
        super(Software,self).__init__(title = title, description = description, price = price, store_id =  store_id)
        self.os = os
        self.ESRB = ESRB

    def __str__(self):
        software_info = "{} for {} with {}".format(self.title, self.os, self.ESRB)
        return software_info

    def __eq__(self, other):
        if self.title == other.title and self.os == other.os and self.ESRB == other.ESRB:
            return True
        else:
            return False

    def change_os(self,os = ""):
        if not os:
            os = raw_input("Please give me the osinfo:")
        self.os = os

    def change_ESRB(self,ESRB = ""):
        if not ESRB:
            ESRB = raw_input("Please give the ESRB:")
        self.ESRB = ESRB


def main():
    pycharm = Software(title = "pycharm", description="a python IDE", price=5, store_id= "55555555", os="windows", ESRB="A")
    pycharm2 = Software(title="pycharm", description="a python IDE", price=20, store_id="1111111", os="windows",ESRB="A")
    pyIDE = Software(title = "pycharm", description="a python IDE", price=20, store_id= "6666666", os="linux", ESRB="B")
    print pycharm
    print pycharm2
    print pyIDE
    print pycharm == pycharm2
    print pycharm == pyIDE
    pycharm2.change_os()
    print pycharm2
    pyIDE.change_ESRB()
    print pyIDE


if __name__ == "__main__":
    main()


