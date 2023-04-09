import subprocess

from main.appData import AppData


class IwTool:
    def __init__(self, params: AppData):
        self.appData = params

    def enable_mode_monitor(self, iface):
        # print('sudo iw wlan1 set monitor control')
        command = ['sudo', 'iw', iface, 'set', 'type', 'monitor']
        print(command)
        subprocess.run(command)

    def disable_mode_monitor(self, iface):
        # print('sudo iw wlan1 set monitor control')
        command = ['sudo', 'iw', iface, 'set', 'type', 'managed']
        print(command)
        subprocess.run(command)
