from main.appData import AppData
from util.helper import Helper


class IpTool:
    def __init__(self, params: AppData):
        self.appData = params
        self.helper = Helper(params)

    def set_iface_up(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'up']
        self.helper.execute_command(command)

    def set_iface_down(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'down']
        self.helper.execute_command(command)
