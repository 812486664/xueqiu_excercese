#! /usr/bin/python
# coding=utf-8


from page_object_yml.populater.AndroidCapability import AndroidCapability


class DriverConfig:

    def __init__(self, android: AndroidCapability,
                    implicitly_wait: int,
                    url: str):
        self.android = android
        self.implicitly_wait = implicitly_wait
        self.url = url
