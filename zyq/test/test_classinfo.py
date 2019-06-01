# encoding:utf-8
import unittest
from zyq.client.classinfo import ClassInifWJ

class TestClassInfoWJ(unittest.TestCase):


    def test_get_current_wj_counter(self):
        print ("当前已发问卷数量:%s"% ClassInifWJ.total_counter)
        print ("收回有效问卷数量:%s"%ClassInifWJ.valid_counter)

        zyq_wj = ClassInifWJ()
        zyq_wj.answer('zyq', '177777777', '123@qq.com')
        print ("当前已发问卷数量:%s" % ClassInifWJ.total_counter)
        print ("收回有效问卷数量:%s" % ClassInifWJ.valid_counter)

        liufan_wj = ClassInifWJ()
        print ("当前已发问卷数量:%s" % ClassInifWJ.total_counter)
        print ("收回有效问卷数量:%s" % ClassInifWJ.valid_counter)

    # def test_get_name_without(self):
    #     #1.获取了一个问卷实例:(扫描，在页面打开的一个问卷)
    #     wj = ClassInifWJ()
    #     #2.填写问卷的问题(在页面填写了信息并提交）
    #     wj.answer('zyq', '17777777777', '123@qq.com')
    #     #3.获取问卷所填写的信息，(页面给出已填写的信息的展示)
    #     answer = wj.get_answer()
    #
    #     exp_anwser = {"name":"zyq", "tel":"17777777777", "email":"123@qq.com"}
    #     self.assertEqual(exp_anwser,answer)



if __name__ == '__main__':
    unittest.main()
