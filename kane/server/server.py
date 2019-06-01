# -*- encoding=utf-8 -*-
from kane.until.log import debug,info

class Server():

    def get_name(self,name,desc=None):
        self.name = name
        self.name_desc = desc
        debug("姓名(%s)控件收到值%s"%(self.name_desc,self.name))


    def get_tel(self,tel,desc=None):
        self.tel = tel
        self.tel_desc = desc
        debug("姓名(%s)控件收到值%s" % (self.tel_desc, self.tel))

    def get_addr(self,addr,desc=None):
        self.addr = addr
        self.addr_desc = desc
        debug("姓名(%s)控件收到值%s" % (self.addr_desc, self.addr))

    def get_email(self,email,desc=None):
        self.email = email
        self.email_desc = desc
        debug("姓名(%s)控件收到值%s" % (self.email_desc, self.email))



