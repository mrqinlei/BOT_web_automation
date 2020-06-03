# coding=utf-8
from framework.base_page import BasePage

class HomePage(BasePage):

    #主页button
    homepage_link = "class_name=>header__logo"
    prime_link = "xpath=>//a[@class='header__nav-link'][contains(text(),'PRIME')]"

    def click_prime(self):
        self.click(self.prime_link)
        self.sleep(2)