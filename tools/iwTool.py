import re

from util.helper import Helper


class IwTool:
    def __init__(self, helper: Helper):
        self.helper = helper

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'managed']
        self.helper.execute_command(command)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'monitor']
        self.helper.execute_command(command)

    def list_interfaces(self):
        command = ['iw', 'dev']
        output = self.helper.execute_command_with_result(command)
        iw_interfaces = re.findall(r'Interface (.*?)\n', output)
        return sorted(set(iw_interfaces))
