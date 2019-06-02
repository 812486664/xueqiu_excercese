#! /usr/bin/python
# coding=utf-8


import pytest
from page_object_yml.driver.Client import Client
from page_object_yml.common.PlatForm import PlatForm


@pytest.fixture(scope='module', autouse=True)
def appOption():
    Client.initDriver(platForm=PlatForm.Android)
    yield
    Client.driver.quit()