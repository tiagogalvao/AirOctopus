import subprocess

from main.appData import AppData


class IpTool:
    def __init__(self, params: AppData):
        self.appData = params

    def set_iface_up(self, iface):
        print('sudo ip link set wlan1 up')
        command = ['sudo', 'ip', 'link', 'set', iface, 'up']
        subprocess.run(command)

    def set_iface_down(self, iface):
        print('sudo ip link set wlan1 down')
        command = ['sudo', 'ip', 'link', 'set', iface, 'down']
        subprocess.run(command)
