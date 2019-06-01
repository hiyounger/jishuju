# encoding:utf-8
import unittest
from zyq.server.server import Server

class TestServer(unittest.TestCase):

    def test_get_name_without_desc(self):
        wenjuan = Server()
        wenjuan.get_name("zyq")

        exp_name = "zyq"
        exp_name_desc = None
        act_name = wenjuan.name
        atc_name_desc = wenjuan.name_desc

        fail_list = []
        if exp_name != act_name:
            fail_msg_1 = "问卷中的name值：%s,与期望值:%s不相等" % (act_name, exp_name)
            fail_list.append(fail_msg_1)

        if exp_name_desc != atc_name_desc:
            fail_msg_2 = "问卷中的name描述值：%s,与期望值:%s不相等" % (atc_name_desc, exp_name_desc)
            fail_list.append(fail_msg_2)
        self.assertEqual(0 ,len(fail_list), str(fail_list))

if __name__ == '__main__':
    unittest.main()
