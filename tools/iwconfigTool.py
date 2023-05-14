import re

from util.helper import Helper


class IwconfigTool:
    def __init__(self, helper: Helper):
        self.helper = helper

    def change_channel(self, iface, channel: int):
        command = ['sudo', 'iwconfig', iface, 'channel', channel]
        self.helper.execute_command(command)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'managed']
        self.helper.execute_command(command)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'monitor']
        self.helper.execute_command(command)

    def list_interfaces(self):
        command = ['iwconfig']
        output = self.helper.execute_command_with_result(command)
        matches = re.findall(r'^([a-zA-Z0-9]+)\s+', output, re.MULTILINE)
        return sorted(set(matches))
