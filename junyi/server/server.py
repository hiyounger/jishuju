# -*- encoding:utf-8 -*-

from junyi.utils.log import debug, info

class Server():

    def get_name(self, name, desc=None):
        # 实例变量
        self.name = name
        self.name_desc = desc
        debug("姓名(%s)控件收到了值: %s" % (self.name_desc, self.name))

    def get_tel(self, tel, desc=None):
        self.tel = tel
        self.tel_desc = desc
        debug("电话(%s)控件收到了值:  %s" % (self.tel_desc, self.tel))

    def get_email(self, email, desc=None):
        self.email = email
        self.email_desc = desc
        debug("邮件(%s)控件收到了值:  %s" % (self.email_desc, self.email))

    def get_address(self, address, desc=None):
        self.address = address
        self.address_desc = desc
        debug("地址(%s)控件收到了值:  %s" % (self.address_desc, self.address))