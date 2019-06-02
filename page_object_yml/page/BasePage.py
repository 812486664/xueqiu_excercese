#! /usr/bin/python
# coding=utf-8


from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object_yml.driver.Client import Client
import yaml


class BasePage:

    actionConfig: dict

    @classmethod
    def loadConfigFromFile(cls, filePath):
        file = open(filePath, 'r')
        cls.actionConfig = yaml.load(file)

    def find(self, kv) -> WebElement:
        return Client.driver.find_element(*kv)

    def findByText(self, text: str):
        return self.find((By.XPATH, "//*[contains(@text, %s)]" % text))

    def performAction(self, page: str, key: str, *text):
        # Todo 把读取文件的操作放入的公共的地方，测试用例执行的过程中只执行一次

        by = self.actionConfig[page][key]['by']
        locator = self.actionConfig[page][key]['locator']
        action = self.actionConfig[page][key]['action']
        element = self.find((by, locator))
        if action == 'click':
            element.click()
        elif action == 'sendKey':
            if len(text) == 1:
                element.send_keys(text[0])