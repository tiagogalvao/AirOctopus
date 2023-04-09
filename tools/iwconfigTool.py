import subprocess

from main.appData import AppData


class IwconfigTool:
    def __init__(self, params: AppData):
        self.appData = params

    def enable_mode_monitor(self, iface):
        print('sudo iwconfig wlan1 mode monitor')
        command = ['sudo', 'iwconfig', iface, 'mode', 'monitor']
        subprocess.run(command)

    def disable_mode_monitor(self, iface):
        print('sudo iwconfig wlan1 mode managed')
        command = ['sudo', 'iwconfig', iface, 'mode', 'managed']
        subprocess.run(command)
