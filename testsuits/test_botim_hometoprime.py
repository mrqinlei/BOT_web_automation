#coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
import pageobjects.botim_home

class BotimPrime(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()代码，测试前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作,基本上是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_botim_prime(self):
        """
        test开头，吧测试逻辑代码封装到test开头的方法里
        点击botim首页prime btn，并校验url
        :return:
        """
        homepage = pageobjects.botim_home.HomePage(self.driver)
        homepage.click_prime()
        time.sleep(2)
        homepage.get_windows_img()
        try:
            assert homepage.get_current_url() == 'https://botim.me/prime/'
            print("Test Pass")
        except Exception as e:
            print("Test Fail",format(e))

#   def test_prime_rules(self):
        """
        点击prime页面 rules of uses，并校验url
        :return: 
        """
#        primepage = pageobjects

if __name__=="__main__":
    unittest.main()
