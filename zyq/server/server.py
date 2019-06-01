# encoding:utf-8
from zyq.log import debug,info
class Server():

    def get_name(self, name, desc=None):
        self.name = name
        self.name_desc = desc
        debug("姓名(%s)控件收到了值：%s"%(self.name_desc, self.name))

    def get_add(self, add, desc=None):
        self.add = add
        self.add_desc = desc
        debug("地址(%s)控件收到了值：%s" % (self.add_desc, self.add))

    def get_tel(self,tel, desc=None):
        self.tel = tel
        self.tel_desc = desc
        debug("电话(%s)控件收到了值：%s" % (self.tel_desc, self.tel))

    def get_email(self, email, desc=None):
        self.emial = email
        self.emial_desc = desc
        debug("邮箱(%s)控件收到了值：%s" % (self.emial_desc, self.emial))