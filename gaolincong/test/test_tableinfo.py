# -*-encoding:utf-8-*-
import unittest
from gaolincong.client.tableinfo import Tableinfo

class MyTestTableinfo(unittest.TestCase):
    def test_table_count(self):
        table_glc=Tableinfo().answer("glc","13016489455","1690344964@qq.com","光谷大道b座1602")
        print ("发放数量：" + str(Tableinfo.get_total_count))
        print ("有效数量" + str(Tableinfo.get_valid_count))
        print ("已有数据" + str(Tableinfo.get_total_answer_list))
        table_glc02 = Tableinfo()
        print ("发放数量：" + str(Tableinfo.get_total_count))
        print ("有效数量" + str(Tableinfo.get_valid_count))
        print ("已有数据" + str(Tableinfo.get_total_answer_list))
    def test_tableinfo(self):
        tableinfo=Tableinfo()
        tableinfo.answer("glc","13016489455","1690344964@qq.com","光谷大道b座1602")
        act_info=tableinfo.get_answer()
        exp_info={"name":"glc","tel":"13016489455","email":"1690344964@qq.com","address":"光谷大道b座1602"}
        self.assertEqual(exp_info, act_info)


if __name__ == '__main__':
    unittest.main()
