#! /usr/bin/python
# coding=utf-8


import pytest
from page_object_yml.driver.Client import Client
from page_object_yml.common.PlatForm import PlatForm
from page_object_yml.page.BasePage import BasePage


@pytest.fixture(scope='module', autouse=True)
def appOption():
    Client.initDriver(platForm=PlatForm.Android)
    BasePage.loadConfigFromFile('../config/action.yml')
    yield
    Client.driver.quit()