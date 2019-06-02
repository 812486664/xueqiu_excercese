#! /usr/bin/python
# coding=utf-8
from page_object_yml.page.BasePage import BasePage


class LoginPage(BasePage):

    def goto_phone_others(self):
        self.performAction('login', 'phone_other')
        return self

    def goto_pwd_input(self):
        self.performAction('login_input', 'pwd')
        return self

    def input_account_pwd(self, account, pwd):
        self.performAction('login_input', 'account_input', account)
        self.performAction('login_input', 'pwd_input', pwd)
        self.performAction('login_input', 'login')
        return self
