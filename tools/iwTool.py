import re

from util.helper import Helper


class IwTool:
    def __init__(self, helper: Helper):
        self.helper = helper

    def change_channel(self, iface, channel: int):
        command = ['sudo', 'iw', 'dev', iface, 'set', 'channel', channel]
        self.helper.execute_command(command, 2)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'managed']
        self.helper.execute_command(command, 1)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'monitor']
        self.helper.execute_command(command, 1)

    def list_interfaces(self):
        command = ['iw', 'dev']
        output = self.helper.execute_command_with_result(command, 1)
        iw_interfaces = re.findall(r'Interface (.*?)\n', output)
        return sorted(set(iw_interfaces))
