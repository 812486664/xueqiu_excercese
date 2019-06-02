#! /usr/bin/python
# coding=utf-8
from page_object_yml.page.BasePage import BasePage
from page_object_yml.page.LoginPage import LoginPage


class ProfilePage(BasePage):

    def goto_login(self):
        self.performAction('profile', 'login')
        return LoginPage()