# -*- encoding=utf-8 -*-
from kane.server.server import Server

class ClassInfo(Server):

    total_counter = 0

    valid_counter = 0

    total_answer = []

    def __init__(self):
        print ("我是构造方法，只要发一份问卷，我就执行一次")
        ClassInfo.total_counter += 1

    def answer(self,name,tel,email):
        self.get_name(name)
        self.get_tel(tel)
        self.get_email(email)
        self.anser_list = {
            "name": self.name,
            "tel": self.tel,
            "email": self.email
        }
        ClassInfo.valid_counter +=1
        ClassInfo.total_answer.append(self.anser_list)

    def get_answer(self):

        return self.anser_list