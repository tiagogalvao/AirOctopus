from main.appData import AppData
from util.helper import Helper


class IwTool:
    def __init__(self, params: AppData):
        self.appData = params
        self.helper = Helper(params)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'monitor']
        self.helper.execute_command(command)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iw', iface, 'set', 'type', 'managed']
        self.helper.execute_command(command)
