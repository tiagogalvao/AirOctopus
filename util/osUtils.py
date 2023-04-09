import os
import platform
import sys

from main.appData import AppData
from util.helper import Helper
from util.stringUtils import StringUtils


class OsUtils:
    def __init__(self, app_data: AppData, helper: Helper):
        self.appData = app_data
        self.helper = helper

    def check_platform(self):
        system = platform.system()
        if StringUtils.equals_ignore_case(system, 'Linux'):
            if StringUtils.contains_ignore_case('Microsoft', platform.release()):
                self.helper.output_text('Keep in mind that', self.appData.appName, 'was not tested under WSL.')
            else:
                self.helper.output_text(self.appData.appName, 'is running under *Unix... good.')
        elif StringUtils.equals_ignore_case(system, 'Windows'):
            self.helper.output_text(self.appData.appName, 'is running under Windows. This is not a really smart idea.')
            sys.exit(0)
        else:
            self.helper.output_text('Unknown operating system detected. Bye.')
            sys.exit(0)

    def check_privileges(self):
        if os.geteuid() != 0:
            self.helper.output_text('Information:', self.appData.appName, 'is not running as root. Good.')
            self.helper.output_text('You will be asked for a password when privileges are needed.')
        else:
            self.helper.output_text("You don't need to run this as root ;)")
