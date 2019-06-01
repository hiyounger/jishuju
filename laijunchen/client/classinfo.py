# -*- encoding:utf-8 -*-

from laijunchen.server.server import Server
from laijunchen.until import log

class ClassInfoWJ(Server):

    #类变量:发放的总数
    __total_counter = 0
    #类变量：回收的有效问卷数
    __valid_counter = 0
    #类变量：总列表
    __total_counter_list = []

    @classmethod
    def get_total_counter(cls):
        return cls.__total_counter

    @classmethod
    def get_valid_counter(cls):
        return cls.__valid_counter

    @classmethod
    def get_total_counter_list(cls):
        return cls.__total_counter_list

    def __init__(self):
        log.debug("我是ClassInfoWJ的构造方法，只要发放一次，我就会执行一次")
        ClassInfoWJ.__total_counter += 1

    def answer(self, name, tel, email):
        #从Server中选取所需要的模板，并附定义
        self.get_name(name)
        self.get_tel(tel)
        self.get_email(email)
        #用户填写的问题
        self.wj_answer = {
            "name":self.name,
            "tel":self.tel,
            "email":self.email
        }
        ClassInfoWJ.__total_counter += 1
        ClassInfoWJ.__total_counter_list.append(self.wj_answer)

    def  get_answer(self):
        return self.wj_answer