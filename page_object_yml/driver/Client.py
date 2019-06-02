#! /usr/bin/python
# coding=utf-8


import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from page_object_yml.populater.DriverConfig import DriverConfig
from page_object_yml.common.PlatForm import PlatForm



class Client:

    driver: WebDriver

    @classmethod
    def initDriver(cls, platForm = PlatForm.Android) -> WebDriver:
        file = open('..\config\driver.yml', "r")
        config: DriverConfig = yaml.load(file)
        if PlatForm.Android == platForm:
            cls.driver = webdriver.Remote(config.url, config.android.__dict__)
        else:
            cls.driver = webdriver.Remote(config.url, config.android.__dict__)
        cls.driver.implicitly_wait(config.implicitly_wait)
        return cls.driver

