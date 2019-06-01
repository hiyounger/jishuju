# -*- encoding:utf-8 -*-
import unittest

from laijunchen.client.classinfo import ClassInfoWJ

class TestClassInfoWJ(unittest.TestCase):

    def test_get_current_wj_counter(self):
        print ("当前已发放问卷数量： %s" % ClassInfoWJ.get_total_counter())
        print ("收回已发放问卷数量： %s" % ClassInfoWJ.get_valid_counter())
        print ("当前已发放问卷数量列表： %s" % ClassInfoWJ.get_total_counter_list())


        ljc = ClassInfoWJ()
        ljc.answer('赖俊晨', '17740500814', '382135230@qq.com')
        print ("当前已发放问卷数量： %s" % ClassInfoWJ.get_total_counter())
        print ("收回已发放问卷数量： %s" % ClassInfoWJ.get_valid_counter())
        print ("当前已发放问卷数量列表： %s" % ClassInfoWJ.get_total_counter_list())

        cx_wj = ClassInfoWJ
        print ("当前已发放问卷数量： %s" % ClassInfoWJ.get_total_counter())
        print ("收回已发放问卷数量： %s" % ClassInfoWJ.get_valid_counter())
        print ("当前已发放问卷数量列表： %s" % ClassInfoWJ.get_total_counter_list())
    def test_something(self):
        #获取问卷表格
        wj = ClassInfoWJ()
        #填写问卷
        wj.answer('赖俊晨', '17740500814', '382135230@qq.com')
        #获取信息
        answer_msg = wj.get_answer()

        exp_wj = {'name':'赖俊晨',"tel": '17740500814', "email":'382135230@qq.com'}
        act_wj = answer_msg
        self.assertEqual(exp_wj, act_wj)





if __name__ == '__main__':
    unittest.main()
