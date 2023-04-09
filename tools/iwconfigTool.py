from main.appData import AppData
from util.helper import Helper


class IwconfigTool:
    def __init__(self, params: AppData):
        self.appData = params
        self.helper = Helper(params)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'monitor']
        self.helper.execute_command(command)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'managed']
        self.helper.execute_command(command)
