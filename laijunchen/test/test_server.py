# -*- encoding:utf-8 -*-
import unittest

from laijunchen.server.server import Server
from laijunchen.until.log import error

class TestServer(unittest.TestCase):

    def test_gei_name_without_desc(self):
        wenjuan = Server()
        wenjuan.get_name("赖俊晨")

        exp_name = "赖俊晨"
        exp_name_desc = None
        act_name = wenjuan.name
        act_name_desc = wenjuan.name_desc
        fail_list = []
        if exp_name != act_name:
            fail_msg_1 = ("问卷中的name的值：%s ，我们期望的值：%s 不相等" % (act_name, exp_name))
            error(fail_msg_1)
            fail_list.append(fail_msg_1)

        if exp_name_desc != act_name_desc:
            fail_msg_2 = ("问卷中的name的描述值：%s ，我们期望的值：%s 不相等" % (act_name_desc, exp_name_desc))
            error(fail_msg_2)
            fail_list.append(fail_msg_2)

        self.assertEqual(0, len(fail_list), str(fail_list))

    def test_gei_name_with_desc(self):
        wenjuan = Server()
        wenjuan.get_name("赖俊晨", "请输入名字")

        exp_name = "赖俊晨"
        exp_name_desc = "请输入名字"
        act_name = wenjuan.name
        act_name_desc = wenjuan.name_desc
        fail_list = []
        if exp_name != act_name:
            fail_msg_1 = ("问卷中的name的值：%s ，我们期望的值：%s 不相等" % (act_name, exp_name))
            error(fail_msg_1)
            fail_list.append(fail_msg_1)

        if exp_name_desc != act_name_desc:
            fail_msg_2 = ("问卷中的name的描述值：%s ，我们期望的值：%s 不相等" % (act_name_desc, exp_name_desc))
            error(fail_msg_2)
            fail_list.append(fail_msg_2)

        self.assertEqual(0, len(fail_list), str(fail_list))

    def test_gei_tel(self):
        wenjuan = Server()
        wenjuan.get_tel("17740500814")

        exp_tel = "17740500814"
        act_tel = wenjuan.tel
        fail_msg = ("问卷中的tel的值：%s ，我们期望的值：%s" % (act_tel, exp_tel ))
        print (fail_msg)
        self.assertEqual(exp_tel, act_tel,fail_msg )
if __name__ == '__main__':
    unittest.main()
