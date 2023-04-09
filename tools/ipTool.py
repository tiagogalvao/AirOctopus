from main.appData import AppData
from util.helper import Helper


class IpTool:
    def __init__(self, app_data: AppData):
        self.appData = app_data
        self.helper = Helper(app_data)

    def set_iface_up(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'up']
        self.helper.execute_command(command)

    def set_iface_down(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'down']
        self.helper.execute_command(command)
