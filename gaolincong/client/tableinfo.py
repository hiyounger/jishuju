# -*-encoding:utf-8-*-
from gaolincong.server.server import Table
from gaolincong.util import log

class Tableinfo(Table):
    #类变量
    __total_count=0
    __valid_count=0
    __total_answer_list=[]
    def __init__(self):
        log.debug("每初始化一次，就执行一次")
        Tableinfo.__total_count+=1
    @classmethod
    def get_total_count(cls):
        return cls.__total_count
    @classmethod
    def get_valid_count(cls):
        return cls.__valid_count
    @classmethod
    def get_total_answer_list(cls):
        return cls.__total_answer_list
    def answer(self,name,tel,email,address):
        self.table_name(name)
        self.table_tel(tel)
        self.table_email(email)
        self.table_address(address)
        self.current_list = {"name": self.name,
                        "tel": self.tel,
                        "email": self.email,
                        "address": self.address}
        Tableinfo.__total_answer_list.append(self.current_list)
        Tableinfo.__valid_count+=1
    def get_answer(self):

        return self.current_list

