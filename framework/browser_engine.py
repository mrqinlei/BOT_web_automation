# _*_ coding:utf-8 _*_


from selenium import webdriver
from framework.logger import Logger
import configparser
import os.path

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.')) #相对路径
    chrome_driver_path = dir + '/tools/chromedriver'
    firefox_driver_path = dir + '/tools/geckodriver'

    def __init__(self,driver):
        self.driver = driver
    # read the browser type from config.ini file,return the driver
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is : %s"% url)

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")

        driver.get(url)
        logger.info("Open url: %s"% url)
        driver.maximize_window()
        logger.info("Maxmize the current window")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser")
        self.driver.quit()