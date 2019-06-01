# -- encoding:utf-8 --
import unittest
from zhang_c_m.server.servers import Server

class TestServer(unittest.TestCase):
    def test__get_name(self):
        wenjuan = Server()
        wenjuan.get_name("Mr.zhang")

        exp_name = "Mr.zhang"
        act_name = wenjuan.name
        fail_mag = "问卷中的name值：%s，与期望的值：%s 不相等" % (act_name, exp_name)
        self.assertEqual(exp_name, act_name,
                         fail_mag)

    def test__get_tel(self):
        wenjuan = Server()
        wenjuan.get_name("17683905332")

        exp_tel = "17683905332"
        act_tel = wenjuan.name
        fail_mag = "问卷中的name值：%s，与期望的值：%s 不相等" % (act_tel, exp_tel)
        self.assertEqual(exp_tel, act_tel,
                         fail_mag)

    def test__get_email(self):
        wenjuan = Server()
        wenjuan.get_name("17683905332@163.com")

        exp_email = "17683905332@163.com"
        act_email = wenjuan.name
        fail_mag = "问卷中的name值：%s，与期望的值：%s 不相等" % (act_email, exp_email)
        self.assertEqual(exp_email, act_email,
                         fail_mag)

    def test__get_adress(self):
        wenjuan = Server()
        wenjuan.get_name("湖北武汉")

        exp_adress = "湖北武汉"
        act_adress = wenjuan.name
        fail_mag = "问卷中的name值：%s，与期望的值：%s 不相等" % (act_adress, exp_adress)
        self.assertEqual(exp_adress, act_adress,
                         fail_mag)


if __name__ == '__main__':
    unittest.main()
