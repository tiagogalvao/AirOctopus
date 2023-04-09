import os
import platform
import sys

from main.appData import AppData
from util.stringUtils import StringUtils


class OsUtils:
    def __init__(self, params: AppData):
        self.appData = params

    def check_platform(self):
        system = platform.system()
        if StringUtils.equals_ignore_case(system, 'Linux'):
            if StringUtils.contains_ignore_case('Microsoft', platform.release()):
                print('Keep in mind that', self.appData.appName, 'was not tested under WSL.')
            else:
                print(self.appData.appName, 'is running under *Unix... good.')
        elif StringUtils.equals_ignore_case(system, 'Windows'):
            print(self.appData.appName, 'is running under Windows. This is not a really smart idea.')
            sys.exit(0)
        else:
            print('Unknown operating system detected. Bye.')
            sys.exit(0)

    def check_privileges(self):
        if os.geteuid() != 0:
            print('Information:', self.appData.appName, 'is not running as root. Good.')
            print('You will be asked for a password when privileges are needed.')
        else:
            print("You don't need to run this as root ;)")
