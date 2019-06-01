# encoding:utf-8
from zyq.server.server import Server
from zyq import log

class ClassInifWJ(Server):

    total_counter= 0
    valid_counter = 0

    def __init__(self):
        log.debug("发一个问卷我执行一次")
        ClassInifWJ.total_counter += 1


    def answer(self, name, tel, email):
        self.get_name(name)
        self.get_tel(tel)
        self.get_email(email)
        self.current_answer = {
            'name': self.name,
            'tel': self.tel,
            'email': self.emial
        }
        ClassInifWJ.valid_counter += 1

    def get_answer(self):


        return self.current_answer