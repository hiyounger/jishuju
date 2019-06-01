# -*- encoding:utf-8 -*-
import unittest

from junyi.client.classinfo import ClassInfoWJ

class TestClassInfoWJ(unittest.TestCase):

    def test_get_current_wj_counter(self):
        print("当前已发放问卷数量: %s" % ClassInfoWJ.total_counter)
        print("收回有效问卷数量: %s" % ClassInfoWJ.valid_counter)
        print("收回有效问卷答案列表: %s" % ClassInfoWJ.total_answers_list)

        glc_wj = ClassInfoWJ()
        glc_wj.answer('glc', '19987654321', 'wrhew@qq.com')
        print("当前已发放问卷数量: %s" % ClassInfoWJ.total_counter)
        print("收回有效问卷数量: %s" % ClassInfoWJ.valid_counter)
        print("收回有效问卷答案列表: %s" % ClassInfoWJ.total_answers_list)

        hx_wj = ClassInfoWJ()
        print("当前已发放问卷数量: %s" % ClassInfoWJ.total_counter)
        print("收回有效问卷数量: %s" % ClassInfoWJ.valid_counter)
        print("收回有效问卷答案列表: %s" % ClassInfoWJ.total_answers_list)

        kjp_wj = ClassInfoWJ()
        kjp_wj.answer('kjp', '19987687990', 'kjp@qq.com')
        print("当前已发放问卷数量: %s" % ClassInfoWJ.total_counter)
        print("收回有效问卷数量: %s" % ClassInfoWJ.valid_counter)
        print("收回有效问卷答案列表: %s" % ClassInfoWJ.total_answers_list)

    def test_customer_answer(self):
        #1. 获取了问卷的一个实例：（扫描，在页面打开的一个问卷）
        wj = ClassInfoWJ()
        #2. 填写问卷的问题(在页面填写了信息，并提交)
        wj.answer('glc', '19987654321', 'wrhew@qq.com')
        #3. 获取问卷所填写的信息（页面给出已填写信息的展示）
        answer = wj.get_answer()

        exp_answer = {"name":"glc", "tel":"19987654321", "email":"wrhew@qq.com"}
        self.assertEqual(exp_answer, answer)

if __name__ == '__main__':
    unittest.main()
