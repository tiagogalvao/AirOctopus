import re

from tools.base_tool import BaseTool
from util.helper import Helper


class IwconfigTool(BaseTool):
    def __init__(self, helper: Helper):
        self.helper = helper
        self.assembly_name = 'iwconfig'

    def change_channel(self, iface, channel: int):
        command = ['sudo', 'iwconfig', iface, 'channel', channel]
        self.helper.execute_command(command, 2)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'managed']
        self.helper.execute_command(command, 1)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'monitor']
        self.helper.execute_command(command, 1)

    def list_interfaces(self):
        command = ['iwconfig']
        output = self.helper.execute_command_with_result(command, 1)
        matches = re.findall(r'^([a-zA-Z0-9]+)\s+', output, re.MULTILINE)
        return sorted(set(matches))
