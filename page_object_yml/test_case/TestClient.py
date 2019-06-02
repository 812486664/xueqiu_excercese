#! /usr/bin/python
# coding=utf-8


import pytest
from page_object_yml.page.MainPage import MainPage


class TestClient:

    def test_main(self):
        MainPage().goto_profile().goto_login().goto_phone_others().goto_pwd_input().input_account_pwd('15731112345', '123456')
