# -*- encoding=utf-8 -*-
import unittest
from kane.client.classinfo import ClassInfo


class TestClassInfo(unittest.TestCase):
    def test_anwer(self):
        wj = ClassInfo()
        wj.answer("kane","123","qwd@qq.com")

        act_answer = wj.get_answer()
        exp_anser = {
            "name" : "kane",
            "tel" : "123",
            "email" : "qwd@qq.com"
        }
        self.assertEqual(exp_anser, act_answer)

    def test_counter(self):
        print ("当前已发放的问卷：%s"%ClassInfo.total_counter)
        print ("当前有效的问卷：%s" % ClassInfo.valid_counter)
        print ("当前填写问卷内容：%s" % ClassInfo.total_answer)

        kane = ClassInfo()
        kane.answer("kane","123","qwd@qq.com")
        print ("当前已发放的问卷：%s" % ClassInfo.total_counter)
        print ("当前有效的问卷：%s" % ClassInfo.valid_counter)
        print ("当前填写问卷内容：%s" % ClassInfo.total_answer)

        jack = ClassInfo()
        print ("当前已发放的问卷：%s" % ClassInfo.total_counter)
        print ("当前有效的问卷：%s" % ClassInfo.valid_counter)
        print ("当前填写问卷内容：%s" % ClassInfo.total_answer)




if __name__ == '__main__':
    unittest.main()
