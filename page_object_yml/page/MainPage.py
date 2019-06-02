#! /usr/bin/python
# coding=utf-8


from page_object_yml.page.BasePage import BasePage
from page_object_yml.page.ProfilePage import ProfilePage


class MainPage(BasePage):

    def goto_profile(self):
        self.performAction('main', 'profile')
        return ProfilePage()