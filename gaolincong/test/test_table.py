# -*-encoding:utf-8-*-
import unittest
from gaolincong.server.server import Table
from gaolincong.util.log import error


class MyTestTable(unittest.TestCase):
    def test_table01_without_desc(self):
        table01=Table()
        table01.table_name("张三")
        act_name=table01.name
        act_name_desc=table01.name_desc
        exp_name_desc=None
        exp_name="张三"
        fail_list=[]
        if exp_name!=act_name:
            fail_msg_01 = "表中的name值：%s与期望值:%s不相等" % (act_name, exp_name)
            error(fail_msg_01)
            fail_list.append(fail_msg_01)
        if exp_name_desc!=act_name_desc:
            fail_msg_02 = "表中的name描述值：%s与期望值:%s不相等" % (act_name_desc, exp_name_desc)
            error(fail_msg_02)
            fail_list.append(fail_msg_02)
        self.assertEqual(0,len(fail_list),fail_list)
    def test_table01_with_desc(self):
        table01=Table()
        table01.table_name("张三","Please input your name")
        act_name=table01.name
        act_name_desc=table01.name_desc
        exp_name="张三"
        exp_name_desc="Please input your name"
        fail_list = []
        if exp_name != act_name:
            fail_msg_01 = "表中的name值：%s与期望值:%s不相等" % (act_name, exp_name)
            error(fail_msg_01)
            fail_list.append(fail_msg_01)
        if exp_name_desc != act_name_desc:
            fail_msg_02 = "表中的name描述值：%s与期望值:%s不相等" % (act_name_desc, exp_name_desc)
            error(fail_msg_02)
            fail_list.append(fail_msg_02)
        self.assertEqual(0, len(fail_list), fail_list)
    def test_table02(self):
        table02=Table()
        table02.table_tel("13016489455")
        act_tel=table02.tel
        exp_tel="13016489455"
        self.assertEqual(act_tel, exp_tel)
    def test_table03(self):
        table03=Table()
        table03.table_email("1690344964@qq.com")
        act_email=table03.email
        exp_email="1690344964@qq.com"
        self.assertEqual(act_email, exp_email)
    def test_table04(self):
        table04=Table()
        table04.table_address("光谷广场b座1602")
        act_address=table04.address
        exp_address="光谷广场b座1602"
        self.assertEqual(act_address, exp_address)


if __name__ == '__main__':
    unittest.main()
