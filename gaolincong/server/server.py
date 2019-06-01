# -*-encoding:utf-8-*-

from gaolincong.util.log import debug,info
class Table():

    def table_name(self,name,desc=None):
        self.name=name
        self.name_desc=desc
        msg_name="姓名:%s控件收到了值：%s" % (self.name_desc,self.name)
        debug(msg_name)
    def table_tel(self,tel,desc=None):
        self.tel=tel
        self.tel_desc=desc
        msg_tel="电话:%s控件收到了值：%s" % (self.tel_desc, self.tel)
        debug(msg_tel)


    def table_email(self, email,desc=None):
        self.email = email
        self.email_desc=desc
        msg_email="邮箱:%s控件收到了值：%s" % (self.email_desc, self.email)
        debug(msg_email)

    def table_address(self, address,desc=None):
        self.address = address
        self.address_desc=desc
        msg_address="地址:%s控件收到了值：%s" % (self.address_desc, self.address)
        debug(msg_address)
