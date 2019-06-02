#! /usr/bin/python
# coding=utf-8


class AndroidCapability:

    def __init__(self, platformName: str,
                    deviceName: str,
                    appPackage: str,
                    appActivity: str,
                    autoGrantPermissions: bool,
                    noReset: bool,
                    chromedriverExecutableDir: str,
                    unicodeKeyboard: bool,
                    resetKeyboard: bool):
        self.platformName = platformName
        self.deviceName = deviceName
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.autoGrantPermissions = autoGrantPermissions
        self.noReset = noReset
        self.chromedriverExecutableDir = chromedriverExecutableDir
        self.unicodeKeyboard = unicodeKeyboard
        self.resetKeyboard = resetKeyboard