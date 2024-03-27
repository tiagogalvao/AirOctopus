import re

from src.tools.base_tool import BaseTool
from src.util.helper import Helper


class IwlistTool(BaseTool):
    def __init__(self, helper: Helper):
        self.helper = helper
        self.assembly_name = 'iwlist'

    def check_channels(self, iface):
        command = ['sudo', 'iwlist', iface, 'channel']
        output = self.helper.execute_command_with_result(command, 1)
        regex = r'Channel\s+(\d{2,3})'
        return re.findall(regex, output)
