# coding=utf-8
from unittest import TestSuite

from .import HTMLTestRunner
import os
import unittest
import time
test_dir = './'

#设置报告文件保存格式
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,"wb")

#构建suite
suite = unittest.TestLoader().discover(test_dir,pattern='test*.py')

if __name__=='__main__':

    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title='Test',description='测试报告')
    runner.run(suite)