import os
import platform
import sys

from main.appData import AppData
from util.helper import Helper


class OsUtils:
    def __init__(self, app_data: AppData, helper: Helper):
        self.appData = app_data
        self.helper = helper

    def check_platform(self):
        system = platform.system()
        if self.helper.string_equals_ignore_case(system, 'Linux'):
            if self.helper.string_contains_ignore_case('Microsoft', platform.release()):
                self.helper.print_text('Keep in mind that', self.appData.appName, 'was not tested under WSL.')
            else:
                self.helper.print_text(self.appData.appName, 'is running under *Unix... good.')
        elif self.helper.string_equals_ignore_case(system, 'Windows'):
            self.helper.print_text(self.appData.appName, 'is running under Windows. This is not a really smart idea.')
            sys.exit(0)
        else:
            self.helper.print_text('Unknown operating system detected. Bye.')
            sys.exit(0)

    def check_privileges(self):
        if os.geteuid() != 0:
            self.helper.print_text('Information:', self.appData.appName, 'is not running as root. Good.')
            self.helper.print_text('You will be asked for a password when privileges are needed.')
        else:
            self.helper.print_text("You don't need to run this as root ;)")
