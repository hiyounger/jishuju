# -*- encoding=utf-8 -*-
import unittest
from kane.server.server import Server


class TestServer(unittest.TestCase):


    def test_get_name(self):
        wenjuan = Server()
        wenjuan.get_name("kane")
        act_name = wenjuan.name
        act_desc = wenjuan.name_desc
        exp_name = "kane"
        exp_desc = None
        eorry_msg_1 = "问卷中的值：%s 与期望的值：%s 不一致" % (act_name, exp_name)
        eorry_msg_2 = "问卷中的描述值：%s 与期望的值：%s 不一致" % (act_desc, exp_desc)
        self.assertEqual(exp_name, act_name,
                         eorry_msg_1)
        self.assertEqual(exp_desc, act_desc,
                        eorry_msg_2)

    def test_get_name_by_desc(self):
        wenjuan = Server()
        wenjuan.get_name("kane","name")
        act_name = wenjuan.name
        act_desc = wenjuan.name_desc
        exp_name = "kane"
        exp_desc = "name"
        eorry_msg_1 = "问卷中的值：%s 与期望的值：%s 不一致" % (act_name, exp_name)
        eorry_msg_2 = "问卷中的描述值：%s 与期望的值：%s 不一致" % (act_desc, exp_desc)
        self.assertEqual(exp_name, act_name,
                         eorry_msg_1)
        self.assertEqual(exp_desc, act_desc,
                        eorry_msg_2)


    def test_get_tel(self):
        wenjuan = Server()
        wenjuan.get_tel("123")
        act_tel = wenjuan.tel
        exp_tel = "123"
        eorry_msg = "问卷中的值：%s 与期望的值：%s 不一致" % (act_tel, exp_tel)
        self.assertEqual(exp_tel, act_tel,
                         eorry_msg)

    def test_get_email(self):
        wenjuan = Server()
        wenjuan.get_email("1@qq.com")
        act_email = wenjuan.email
        exp_email = "1@qq.com"
        eorry_msg = "问卷中的值：%s 与期望的值：%s 不一致" % (act_email, exp_email)
        self.assertEqual(exp_email, act_email,
                         eorry_msg)

    def test_get_addr(self):
        wenjuan = Server()
        wenjuan.get_addr("wuhan")
        act_addr = wenjuan.addr
        exp_addr = "wuhan"
        eorry_msg = "问卷中的值：%s 与期望的值：%s 不一致" % (act_addr, exp_addr)
        self.assertEqual(exp_addr, act_addr,
                         eorry_msg)


if __name__ == '__main__':
    unittest.main()
