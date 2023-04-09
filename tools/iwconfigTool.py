from main.appData import AppData
from util.helper import Helper


class IwconfigTool:
    def __init__(self, app_data: AppData):
        self.appData = app_data
        self.helper = Helper(app_data)

    def enable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'monitor']
        self.helper.execute_command(command)

    def disable_mode_monitor(self, iface):
        command = ['sudo', 'iwconfig', iface, 'mode', 'managed']
        self.helper.execute_command(command)
