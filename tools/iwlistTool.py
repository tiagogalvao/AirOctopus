import re

from util.helper import Helper


class IwlistTool:
    def __init__(self, helper: Helper):
        self.helper = helper

    def check_channels(self, iface):
        command = ['sudo', 'iwlist', iface, 'channel']
        output = self.helper.execute_command_with_result(command, 1)
        regex = r'Channel\s+(\d{2,3})'
        return re.findall(regex, output)
