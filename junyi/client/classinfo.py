# -*- encoding:utf-8 -*-

from junyi.server.server import Server
from junyi.utils import log

class ClassInfoWJ(Server):

    # 类变量：发放的总问卷数量
    total_counter = 0
    # 类变量：回收的有效问卷数量
    valid_counter = 0
    # 类变量，所有存储的数据
    total_answers_list = []

    def __init__(self):
        log.debug("我是ClassInfoWJ的构造方法，只要发一份问卷，我就会执行一次")
        ClassInfoWJ.total_counter += 1

    def answer(self, name, tel, email):
        '''
        用户填写问卷
        :return:
        '''
        self.get_name(name)
        self.get_tel(tel)
        self.get_email(email)
        self.current_wj_anwser = {
            'name': self.name,
            'tel': self.tel,
            'email': self.email
        }
        ClassInfoWJ.valid_counter += 1
        ClassInfoWJ.total_answers_list.append(self.current_wj_anwser)



    def get_answer(self):
        '''
        用户查看所填写的问卷答案
        :return: 用户答案字典
        '''
        return self.current_wj_anwser