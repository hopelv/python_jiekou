import unittest
from hope_jiegou.common import logger


def add( x, y):
    # if x.isdigit() and y.isdigit():

    # else:
    #     return '类型不对'
    return x + y

class Testfun(unittest.TestCase):



    def test_Add(self):
         self.assertEqual(11,11,'错误')


log = logger.Log()
log.info('----------测试开始-------')
fun=Testfun()
fun.test_Add()
log.info('-------测试结束---------')




